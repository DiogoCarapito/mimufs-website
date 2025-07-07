# delete all content on pages/ folder
import os
import re
import subprocess


def delete_all_content_in_pages_folder():
    # check if pages/ folder exists
    if not os.path.exists("pages/"):
        os.makedirs("pages/")

    folder_path = "pages/"
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        try:
            if os.path.isfile(file_path):
                os.remove(file_path)
            elif os.path.isdir(file_path):
                os.rmdir(file_path)
        except Exception as e:
            print(f"Error deleting {file_path}: {e}")
    # delete all content on pages/ folder


# def slugify(text):
#     import re
#     return re.sub(r'[^a-zA-Z0-9_-]', '', text.replace(' ', '-')).lower()


def write_streamlit_code_from_markdown(md_path, py_path):
    root_path = md_path.split("/")[0]

    with open(md_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    image_pattern = r"!\[([^\]]*)\]\(([^)]+)\)"
    link_pattern = r"\[([^\]]+)\]\(([^)]+)\)"
    iframe_pattern = r'<iframe[^>]*src="([^"]+)"[^>]*>.*?</iframe>'

    with open(py_path, "w", encoding="utf-8") as f:
        f.write("import streamlit as st\n\n")

        buffer = ""
        for line in lines:
            line = line.rstrip("\n")

            if re.match(r"^# (.*)", line):
                if buffer.strip():
                    f.write(f'st.markdown("""{buffer.strip()}""")\n\n')
                    buffer = ""
                f.write(
                    # f'st.title("{re.sub(r"^# ", "", line).strip()}", anchor=False)\n\n'
                    f'st.title("{re.sub(r"^# ", "", line).strip()}")\n\n'
                )
            elif re.match(r"^## (.*)", line):
                if buffer.strip():
                    f.write(f'st.markdown("""{buffer.strip()}""")\n\n')
                    buffer = ""
                f.write(
                    # f'st.subheader("{re.sub(r"^## ", "", line).strip()}", anchor=False)\n\n'
                    f'st.subheader("{re.sub(r"^## ", "", line).strip()}")\n\n'
                )
            elif re.match(r"^### (.*)", line):
                if buffer.strip():
                    f.write(f'st.markdown("""{buffer.strip()}""")\n\n')
                    buffer = ""
                f.write(
                    # f'st.header("{re.sub(r"^### ", "", line).strip()}", anchor=False)\n\n'
                    f'st.header("{re.sub(r"^### ", "", line).strip()}")\n\n'
                )
            elif re.match(iframe_pattern, line):
                if buffer.strip():
                    f.write(f'st.markdown("""{buffer.strip()}""")\n\n')
                    buffer = ""
                iframe_src = re.search(iframe_pattern, line).group(1)
                if iframe_src.startswith("http"):
                    if "youtube.com/embed/" in iframe_src:
                        video_id = iframe_src.split("embed/")[-1].split("?")[0]
                        watch_url = f"https://www.youtube.com/watch?v={video_id}"
                        f.write(f'st.video("{watch_url}")\n\n')
                    else:
                        f.write(f'st.video("{iframe_src}")\n\n')
                else:
                    f.write(f'st.video("content/{iframe_src}", format="video/mp4")\n\n')
            elif re.match(image_pattern, line):
                if buffer.strip():
                    f.write(f'st.markdown("""{buffer.strip()}""")\n\n')
                    buffer = ""
                m = re.match(image_pattern, line)
                alt_text = m.group(1).strip()
                img_path = f"{root_path}/{m.group(2).strip()}"
                f.write(f'st.image("{img_path}", caption="{alt_text}")\n\n')
            elif re.match(link_pattern, line):
                if buffer.strip():
                    f.write(f'st.markdown("""{buffer.strip()}""")\n\n')
                    buffer = ""
                m = re.match(link_pattern, line)
                link_text = m.group(1).strip()
                link_url = m.group(2).strip()
                f.write(f'st.markdown("[{link_text}]({link_url})")\n\n')
            else:
                buffer += line + "\n"

        # Write any remaining buffer as markdown
        if buffer.strip():
            f.write(f'st.markdown("""{buffer.strip()}""")\n\n')


def create_pages_from_markdown():
    # create __init__.py file
    with open("pages/__init__.py", "w") as f:
        f.write("\n")
    # create pages from markdown files
    folder_path = "content/"
    for filename in os.listdir(folder_path):
        if filename.endswith(".md"):
            file_path = os.path.join(folder_path, filename)
            page_name = filename.replace(".md", "").replace(" ", "_").replace("-", "_")
            write_streamlit_code_from_markdown(file_path, f"pages/{page_name}.py")

            # f.write(f"from utils.utils import render_markdown_with_media\n")
            # #f.write(f"from utils.utils import render_markdown_with_media, render_pages_menu\n")
            # #f.write(f"\n")
            # #f.write(f"render_pages_menu()\n")
            # f.write(f"\n")
            # f.write(f'render_markdown_with_media("{file_path}")\n')
            # print(f"Created page: {page_name}.py")


def create_pages():
    # logging.info("Deleting all older content in pages folder")
    delete_all_content_in_pages_folder()
    # logging.info("Creating pages from markdown")
    create_pages_from_markdown()

    subprocess.run(["make", "format"], check=True)

    # Run make format command
    # try:
    # logging.info("Running make format")
    # subprocess.run(["make", "format"], check=True)
    # logging.info("make format completed successfully")
    # except subprocess.CalledProcessError as e:
    # logging.error(f"make format failed: {e}")


if __name__ == "__main__":
    import logging
    from logging_config import setup_logging

    setup_logging()

    logging.info("Starting creating pages from markdown")
    create_pages()
    logging.info("Finished creating pages from markdown")
