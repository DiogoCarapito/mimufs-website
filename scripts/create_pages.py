# delete all content on pages/ folder
import os
import re


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
    quote_pattern = r"^> (.*)"

    comment_pattern = r"<!--(.*?)-->"
    # Remove HTML comments
    lines = [re.sub(comment_pattern, "", line) for line in lines]

    with open(py_path, "w", encoding="utf-8") as f:
        f.write("import streamlit as st\n\n")
        # add a navigation bar, a next and previous page as well as home page

        # # Get all .py files in pages/ and sort them
        # page_files = sorted([file for file in os.listdir('pages/') if file.endswith('.py')])
        # page_names = [file.replace('.py', '').replace('_', ' ') for file in page_files]

        # f.write("page_files = " + repr(page_files) + "\n")
        # f.write("page_names = " + repr(page_names) + "\n")
        # f.write("current_file = __file__.split('/')[-1]\n")
        # f.write("current_idx = page_files.index(current_file)\n")
        # f.write("home_idx = 0  # or set to your preferred home page index\n")
        # f.write("prev_idx = (current_idx - 1) % len(page_files)\n")
        # f.write("next_idx = (current_idx + 1) % len(page_files)\n")
        # f.write("nav_labels = [page_names[prev_idx], page_names[home_idx], page_names[next_idx]]\n")
        # f.write("nav_files = [page_files[prev_idx], page_files[home_idx], page_files[next_idx]]\n")
        # f.write("selected = st.segmented_control('Navegação', nav_labels, default=page_names[current_idx], label_visibility=False)\n")
        # f.write("if selected != page_names[current_idx]:\n")
        # f.write("    st.switch_page(f'pages/{nav_files[nav_labels.index(selected)]}')\n\n")

        buffer = ""
        for line in lines:
            line = line.rstrip("\n")

            if re.match(r"^# (.*)", line):
                if buffer.strip():
                    f.write(f'st.markdown("""{buffer.strip()}""")\n\n')
                    buffer = ""
                f.write(
                    f'st.title("{re.sub(r"^# ", "", line).strip()}", anchor=False)\n\n'
                )
                # f.write(f'st.title("{re.sub(r"^# ", "", line).strip()}")\n\n')
            elif re.match(r"^## (.*)", line):
                if buffer.strip():
                    f.write(f'st.markdown("""{buffer.strip()}""")\n\n')
                    buffer = ""
                f.write(
                    f'st.header("{re.sub(r"^## ", "", line).strip()}", anchor=False)\n\n'
                )
                # f.write(f'st.subheader("{re.sub(r"^## ", "", line).strip()}")\n\n')
            elif re.match(r"^### (.*)", line):
                if buffer.strip():
                    f.write(f'st.markdown("""{buffer.strip()}""")\n\n')
                    buffer = ""
                f.write(
                    f'st.subheader("{re.sub(r"^### ", "", line).strip()}", anchor=False)\n\n'
                )
                # f.write(f'st.header("{re.sub(r"^### ", "", line).strip()}")\n\n')

            # Iframe
            elif re.match(iframe_pattern, line):
                if buffer.strip():
                    f.write(f'st.markdown("""{buffer.strip()}""")\n\n')
                    buffer = ""
                iframe_src = re.search(iframe_pattern, line).group(1)
                # YouTube or web video
                if iframe_src.startswith("http"):
                    # If it's a YouTube embed, convert to watch URL for st.video()
                    if "youtube.com/embed/" in iframe_src:
                        video_id = iframe_src.split("embed/")[-1].split("?")[0]
                        watch_url = f"https://www.youtube.com/watch?v={video_id}"
                        f.write(f'st.video("{watch_url}")\n\n')
                    else:
                        # Other web video (mp4, etc.)
                        f.write(f'st.video("{iframe_src}")\n\n')
                else:
                    # Local video file
                    f.write(f'st.video("content/{iframe_src}", format="video/mp4")\n\n')

            # # Iframe
            # elif re.match(iframe_pattern, line):
            #     if buffer.strip():
            #         f.write(f'st.markdown("""{buffer.strip()}""")\n\n')
            #         buffer = ""
            #     iframe_src = re.search(iframe_pattern, line).group(1)
            #     f.write(f'st.video("{iframe_src}")\n\n')

            # Image
            elif re.match(image_pattern, line):
                if buffer.strip():
                    f.write(f'st.markdown("""{buffer.strip()}""")\n\n')
                    buffer = ""
                m = re.match(image_pattern, line)
                alt_text = m.group(1).strip()
                img_path = f"{root_path}/{m.group(2).strip()}"
                f.write(f'st.image("{img_path}", caption="{alt_text}")\n\n')

            # Link (standalone line)
            elif re.match(link_pattern, line):
                if buffer.strip():
                    f.write(f'st.markdown("""{buffer.strip()}""")\n\n')
                    buffer = ""
                m = re.match(link_pattern, line)
                link_text = m.group(1).strip()
                link_url = m.group(2).strip()
                f.write(f'st.markdown("[{link_text}]({link_url})")\n\n')

            elif re.match(quote_pattern, line):
                # mkae it center, bold and italic, font 20
                if buffer.strip():
                    f.write(f'st.markdown("""{buffer.strip()}""")\n\n')
                    buffer = ""
                quote_text = re.sub(quote_pattern, r"\1", line).strip()
                f.write(
                    f"st.markdown(\"<p style='text-align: center; font-size: 20px; font-weight: bold;'> {quote_text} </p>\", unsafe_allow_html=True)\n\n"
                )

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
            page_name = filename.replace(".md", "").replace(
                " ", "_"
            )  # .replace("-", "_")
            write_streamlit_code_from_markdown(file_path, f"pages/{page_name}.py")


def create_pages():
    delete_all_content_in_pages_folder()
    create_pages_from_markdown()


if __name__ == "__main__":
    create_pages()
