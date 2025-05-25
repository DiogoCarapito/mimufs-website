import streamlit as st
from utils.utils import page_config#, render_pages_menu
from utils.style import main_title

# from utils.utils import render_markdown_with_media, render_pages_menu
from scripts.create_pages import create_pages


def main():
    page_config()

    create_pages()

    main_title("mimufs")
    
    text = "Tutoriais para MIM@UF"
    
    st.markdown(
        f'<p style="text-align: center; font-size: 32px;">{text}</p>',
        unsafe_allow_html=True,
    )


    #st.divider()

    #render_pages_menu()

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
