import streamlit as st
import os

from utils.utils import page_config  # , render_pages_menu
from utils.style import main_title

# from utils.utils import render_markdown_with_media, render_pages_menu
# from scripts.create_pages import create_pages


def load_css(file_name):
    with open(file_name, encoding="utf-8") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


def main():
    page_config()

    css_file = os.path.join(os.path.dirname(__file__), "style/style.css")
    load_css(css_file)

    main_title("mimufs")

    pages = {
        "Conceitos fundamentais": [
            st.Page("pages/01_Introdução.py", title="1. Introdução"),
            st.Page("pages/02_Query.py", title="2. Query"),
            st.Page("pages/03_Pós-Query.py", title="3. Pós-Query"),
            st.Page("pages/04_Exportação.py", title="4. Exportação"),
            st.Page("pages/05_Processamento.py", title="5. Processamento"),
        ],
        "Módulos": [
            st.Page("pages/06_P01_-_Inscritos.py", title="P01. Inscritos"),
            st.Page("pages/07_P02_-_Indicadores.py", title="P02. Indicadores"),
        ],
        "Probelmas especificos": [],
        "Currículo": [],
    }

    pg = st.navigation(pages)  # , position="top")
    pg.run()

    # text = "Tutoriais para MIM@UF"

    # st.markdown(
    #     f'<p style="text-align: center; font-size: 32px;">{text}</p>',
    #     unsafe_allow_html=True,
    # )

    # st.divider()

    # render_pages_menu()

    # # get all the markdown files in the content folder
    # folder_path = "content/"
    # markdown_files = [f for f in os.listdir(folder_path) if f.endswith(".md")]

    # #sort the files
    # markdown_files = markdown_files.sort()

    # # create a dictionary to store the file names and their corresponding titles
    # markdown_files_dict = {f.replace(".md", "").replace("-", " ").replace("_", " "): f for f in markdown_files}

    # # create a selectbox with the markdown files
    # selected_file = st.segmented_control("Select a tutorial", list(markdown_files_dict.keys()), selection_mode="single", default=list(markdown_files_dict.keys())[0])

    # st.divider()

    # if selected_file:
    #     # render the markdown file with media
    #     render_markdown_with_media(f"{folder_path}{markdown_files_dict[selected_file]}")

    # else:
    #     st.write("No file selected")


if __name__ == "__main__":
    main()
