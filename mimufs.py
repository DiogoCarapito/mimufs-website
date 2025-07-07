import streamlit as st
import os

from utils.utils import page_config  # , render_pages_menu
from utils.style import main_title

# from utils.utils import render_markdown_with_media, render_pages_menu
# from scripts.create_pages import create_pages


def load_css(file_name):
    with open(file_name, encoding="utf-8") as f:
        css_content = f.read()

    # Apply theme-specific styles based on session state
    if st.session_state.get("dark_mode", False):
        # Dark theme styles
        dark_theme_css = """
        /* Dark theme overrides */
        .stApp {
            background-color: #0e1117;
            color: #fafafa;
        }
        .stSidebar {
            background-color: #262730;
        }
        .stSidebar .sidebar-content {
            background-color: #262730;
        }
        /* Dark theme for navigation */
        .stNavigation {
            background-color: #262730;
        }
        /* Dark theme for markdown content */
        .stMarkdown {
            color: #fafafa;
        }
        /* Dark theme for text elements */
        p, li, div, span {
            color: #fafafa !important;
        }
        /* Dark theme for headers */
        h1, h2, h3, h4, h5, h6 {
            color: #fafafa !important;
        }
        /* Dark theme for buttons and widgets */
        .stButton > button {
            background-color: #262730;
            color: #fafafa;
            border: 1px solid #4a4a4a;
        }
        .stButton > button:hover {
            background-color: #3a3a3a;
            border-color: #6a6a6a;
        }
        """
        css_content += dark_theme_css

    st.markdown(f"<style>{css_content}</style>", unsafe_allow_html=True)


def main():
    page_config()

    # Initialize theme in session state
    if "dark_mode" not in st.session_state:
        st.session_state.dark_mode = False

    # Add theme toggle in sidebar
    with st.sidebar:
        st.session_state.dark_mode = st.toggle(
            "🌙 Dark Mode",
            value=st.session_state.dark_mode,
            help="Toggle between light and dark themes",
        )

    css_file = os.path.join(os.path.dirname(__file__), "style/style.css")
    load_css(css_file)

    main_title("mimufs")

    sidebar_menu_structure = [
        {
            "menu": "Conceitos fundamentais",
            "page": "pages/01_Introdução.py",
            "title": "a) Introdução ✅",
        },
        {
            "menu": "Conceitos fundamentais",
            "page": "pages/02_Workflow.py",
            "title": "b) Workflow 🏗️",
        },
        {
            "menu": "Conceitos fundamentais",
            "page": "pages/03_Query.py",
            "title": "c) Query 🏗️",
        },
        {
            "menu": "Conceitos fundamentais",
            "page": "pages/04_Pós_Query.py",
            "title": "d) Pós-Query 🏗️",
        },
        {
            "menu": "Conceitos fundamentais",
            "page": "pages/05_Exportação.py",
            "title": "e) Exportação",
        },
        {
            "menu": "Conceitos fundamentais",
            "page": "pages/06_Processamento.py",
            "title": "f) Processamento",
        },
        {
            "menu": "Módulos",
            "page": "pages/11_P01_Inscritos.py",
            "title": "P01. Inscritos",
        },
        {
            "menu": "Módulos",
            "page": "pages/12_P02_Indicadores.py",
            "title": "P02. Indicadores",
        },
        {
            "menu": "Módulos",
            "page": "pages/13_P03_Consultas.py",
            "title": "P03. Consultas",
        },
        {
            "menu": "Módulos",
            "page": "pages/14_P04_Problemas_e_P05_Doenças.py",
            "title": "P04. Problemas e P05. Doenças",
        },
        {
            "menu": "Módulos",
            "page": "pages/15_P06_Medicamentos.py",
            "title": "P06. Medicamentos",
        },
        {"menu": "Módulos", "page": "pages/16_P07_MCDTs.py", "title": "P07. MCDTs"},
        {"menu": "Módulos", "page": "pages/17_P09_Vacinas.py", "title": "P09. Vacinas"},
        {
            "menu": "Módulos",
            "page": "pages/18_P10_Biometrias.py",
            "title": "P10. Biometrias",
        },
        # {"menu": "Probelmas especificos", "page":"pages/19_P11_Probelmas_Especificos.py", "title": "P11. Problemas Específicos"},
        {
            "menu": "Currículo",
            "page": "pages/29_Introdução_ao_curriculo.py",
            "title": "0. Introdução ao currículo 🏗️",
        },
        {
            "menu": "Currículo",
            "page": "pages/30_Lista_consultas_realizadas.py",
            "title": "1. Lista de consultas realizadas 🏗️",
        },
        {
            "menu": "Currículo",
            "page": "pages/31_Lista_utentes_inscritos.py",
            "title": "2. Lista de utentes inscritos",
        },
        {
            "menu": "Currículo",
            "page": "pages/32_Nacionalidade_profissão_habilitações.py",
            "title": "3. Nacionalidade, profissão e habilitações",
        },
        {
            "menu": "Currículo",
            "page": "pages/33_Agregados_familiares.py",
            "title": "4. Agregados familiares ",
        },
        {
            "menu": "Currículo",
            "page": "pages/34_Indicadores_Unidade.py",
            "title": "5. Indicadores Unidade",
        },
        {
            "menu": "Currículo",
            "page": "pages/35_Indicadores_por_Médico.py",
            "title": "6. Indicadores por Médico",
        },
        {
            "menu": "Currículo",
            "page": "pages/36_Lista_problemas_utente.py",
            "title": "7. Lista de Problemas por utente",
        },
        {
            "menu": "Currículo",
            "page": "pages/37_Top_problemas.py",
            "title": "8. Top Problemas",
        },
        {
            "menu": "Currículo",
            "page": "pages/38_Novos_problemas_por_utente.py",
            "title": "9. Novos problemas por utente",
        },
        {
            "menu": "Currículo",
            "page": "pages/39_Problemas_agudos_por_médico.py",
            "title": "10. Problemas agudos por médico",
        },
        {
            "menu": "Currículo",
            "page": "pages/40_Risco_diabetes.py",
            "title": "11. Risco Diabetes",
        },
        {
            "menu": "Currículo",
            "page": "pages/41_Medicamentos_prescritos_utente.py",
            "title": "12. Medicamentos prescrito por utente",
        },
        {
            "menu": "Currículo",
            "page": "pages/42_Medicamentos_prescritos_médico.py",
            "title": "13. Medicamentos prescrito por Médico",
        },
        {
            "menu": "Outros",
            "page": "pages/98_sobre.py",
            "title": "Sobre",
        },
    ]

    pages = {}
    for item in sidebar_menu_structure:
        menu = item["menu"]
        page = item["page"]
        title = item["title"]

        if menu not in pages:
            pages[menu] = []

        pages[menu].append(st.Page(page, title=title))

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
