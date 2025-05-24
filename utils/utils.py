import re
import os
import streamlit as st


def func():
    return None


def render_markdown_with_media(file_path):
    root_path = file_path.split("/")[0]
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Patterns for images, links, iframes, and headings
    image_pattern = r"!\[([^\]]*)\]\(([^)]+)\)"
    link_pattern = r"\[([^\]]+)\]\(([^)]+)\)"
    iframe_pattern = r'<iframe[^>]*src="([^"]+)"[^>]*>.*?</iframe>'
    h1_pattern = r"^# (.*)$"
    h2_pattern = r"^## (.*)$"
    h3_pattern = r"^### (.*)$"

    # Combine all patterns, each in its own group
    combined_pattern = (
        f"({image_pattern})"  # groups 1-3
        f"|({link_pattern})"  # groups 4-6
        f"|({iframe_pattern})"  # group 7
        f"|({h1_pattern})"  # group 8
        f"|({h2_pattern})"  # group 9
        f"|({h3_pattern})"  # group 10
    )

    last_end = 0
    for match in re.finditer(combined_pattern, content, re.DOTALL | re.MULTILINE):
        start, end = match.start(), match.end()
        text = content[last_end:start]
        if text.strip():
            st.markdown(text)

        # Image
        if match.group(1):
            alt_text = match.group(2).strip()
            img_path = f"{root_path}/{match.group(3).strip()}"
            st.image(img_path, caption=alt_text if alt_text else None)
        # Link
        elif match.group(4):
            link_text = match.group(5).strip()
            link_url = match.group(6).strip()
            st.markdown(f"[{link_text}]({link_url})")
        # Iframe
        elif match.group(7):
            iframe_src = match.group(7).strip()
            st.components.v1.iframe(iframe_src, height=315)
        # Heading 1
        elif match.group(8):
            st.title(match.group(8).strip())
        # Heading 2
        elif match.group(9):
            st.subheader(match.group(9).strip())
        # Heading 3
        elif match.group(10):
            st.header(match.group(10).strip())

        last_end = end

    # Any remaining text after the last match
    if last_end < len(content):
        rest = content[last_end:]
        if rest.strip():
            st.markdown(rest)


# def render_markdown_with_media(file_path):
#     root_path = file_path.split("/")[0]
#     with open(file_path, "r", encoding="utf-8") as f:
#         content = f.read()

#     # Patterns
#     title_pattern = r'^(#{1,6})\s*(.*)$'
#     subtitle_pattern = r'^(#{2,6})\s*(.*)$'
#     heading_pattern = r'^(#{1,6})\s*(.*)$'

#     image_pattern = r'!\[([^\]]*)\]\(([^)]+)\)'
#     link_pattern = r'\[([^\]]+)\]\(([^)]+)\)'
#     iframe_pattern = r'<iframe[^>]*src="([^"]+)"[^>]*>.*?</iframe>'


#     # Combine all patterns, each in its own group
#     combined_pattern = (
#         f'({image_pattern})'      # groups 1-3
#         f'|({link_pattern})'      # groups 4-6
#         f'|({iframe_pattern})'    # group 7
#     )

#     last_end = 0
#     for match in re.finditer(combined_pattern, content, re.DOTALL):
#         start, end = match.start(), match.end()
#         text = content[last_end:start]
#         if text.strip():
#             st.markdown(text)

#         # Image
#         if match.group(1):
#             alt_text = match.group(2).strip()
#             img_path = f"{root_path}/{match.group(3).strip()}"
#             st.image(img_path, caption=alt_text if alt_text else None)
#         # Link
#         elif match.group(4):
#             link_text = match.group(5).strip()
#             link_url = match.group(6).strip()
#             st.markdown(f"[{link_text}]({link_url})")
#         # Iframe
#         elif match.group(7):
#             #iframe_line = match.group(7).strip()
#             iframe_link = match.group(8).strip()
#             st.video(iframe_link)#, format="video/mp4", start_time=0)

#         last_end = end

#     # Any remaining text after the last match
#     if last_end < len(content):
#         rest = content[last_end:]
#         if rest.strip():
#             st.markdown(rest)


def render_pages_menu():
    folder_path = "pages/"
    pages_links = [f for f in os.listdir(folder_path) if f.endswith(".py")]

    # exclude __init__.py file
    pages_links = [f for f in pages_links if f != "__init__.py"]

    # sort the files
    pages_links.sort()

    for each_file in pages_links:
        st.page_link(
            "pages/" + each_file,
            icon="📄",
            label=each_file.replace(".py", "").replace("_", " ").replace("-", " "),
        )
