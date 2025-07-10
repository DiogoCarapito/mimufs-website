import streamlit as st
import os
import csv

from utils.utils import page_config  # , render_pages_menu
from utils.style import main_title  # , bottom_suport_email

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

    # run create_pages()  # Create the pages directory if not exists
    # create_pages()

    pages = {}
    with open("sidebar.csv", newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            menu, page, title = row["menu"], row["page"], row["title"]
            if menu not in pages:
                pages[menu] = []
            pages[menu].append(st.Page(page, title=title))

    pg = st.navigation(pages)
    pg.run()

    # bottom_suport_email()


if __name__ == "__main__":
    main()

    # sidebar_menu_structure = [
    #     {
    #         "menu": "Conceitos fundamentais",
    #         "page": "pages/01_Introdução.py",
    #         "title": "a) Introdução ✅",
    #     },
    #     {
    #         "menu": "Conceitos fundamentais",
    #         "page": "pages/02_Workflow.py",
    #         "title": "b) Workflow ✅",
    #     },
    #     {
    #         "menu": "Conceitos fundamentais",
    #         "page": "pages/03_Query.py",
    #         "title": "c) Query 🏗️",
    #     },
    #     {
    #         "menu": "Conceitos fundamentais",
    #         "page": "pages/04_Refinamento.py",
    #         "title": "d) Refinamento 🏗️",
    #     },
    #     {
    #         "menu": "Conceitos fundamentais",
    #         "page": "pages/05_Exportação.py",
    #         "title": "e) Exportação 🏗️",
    #     },
    #     {
    #         "menu": "Conceitos fundamentais",
    #         "page": "pages/06_Processamento.py",
    #         "title": "f) Processamento ✅",
    #     },
    #     # {
    #     #     "menu": "Módulos",
    #     #     "page": "pages/11_P01_Inscritos.py",
    #     #     "title": "P01. Inscritos",
    #     # },
    #     # {
    #     #     "menu": "Módulos",
    #     #     "page": "pages/12_P02_Indicadores.py",
    #     #     "title": "P02. Indicadores",
    #     # },
    #     # {
    #     #     "menu": "Módulos",
    #     #     "page": "pages/13_P03_Consultas.py",
    #     #     "title": "P03. Consultas",
    #     # },
    #     # {
    #     #     "menu": "Módulos",
    #     #     "page": "pages/14_P04_Problemas_e_P05_Doenças.py",
    #     #     "title": "P04. Problemas e P05. Doenças",
    #     # },
    #     # {
    #     #     "menu": "Módulos",
    #     #     "page": "pages/15_P06_Medicamentos.py",
    #     #     "title": "P06. Medicamentos",
    #     # },
    #     # {"menu": "Módulos", "page": "pages/16_P07_MCDTs.py", "title": "P07. MCDTs"},
    #     # {"menu": "Módulos", "page": "pages/17_P09_Vacinas.py", "title": "P09. Vacinas"},
    #     # {
    #     #     "menu": "Módulos",
    #     #     "page": "pages/18_P10_Biometrias.py",
    #     #     "title": "P10. Biometrias",
    #     # },
    #     # {"menu": "Probelmas especificos", "page":"pages/19_P11_Probelmas_Especificos.py", "title": "P11. Problemas Específicos"},
    #     {
    #         "menu": "Currículo",
    #         "page": "pages/29_Introdução_ao_curriculo.py",
    #         "title": "0. Introdução ao currículo 🏗️",
    #     },
    #     {
    #         "menu": "Currículo",
    #         "page": "pages/30_Lista_consultas_realizadas.py",
    #         "title": "1. Lista de consultas realizadas 🏗️",
    #     },
    #     {
    #         "menu": "Currículo",
    #         "page": "pages/31_Lista_utentes_inscritos.py",
    #         "title": "2. Lista de utentes inscritos",
    #     },
    #     {
    #         "menu": "Currículo",
    #         "page": "pages/32_Nacionalidade_profissão_habilitações.py",
    #         "title": "3. Nacionalidade, profissão e habilitações",
    #     },
    #     {
    #         "menu": "Currículo",
    #         "page": "pages/33_Agregados_familiares.py",
    #         "title": "4. Agregados familiares ",
    #     },
    #     {
    #         "menu": "Currículo",
    #         "page": "pages/34_Indicadores_Unidade.py",
    #         "title": "5. Indicadores Unidade",
    #     },
    #     {
    #         "menu": "Currículo",
    #         "page": "pages/35_Indicadores_por_Médico.py",
    #         "title": "6. Indicadores por Médico",
    #     },
    #     {
    #         "menu": "Currículo",
    #         "page": "pages/36_Lista_problemas_utente.py",
    #         "title": "7. Lista de Problemas por utente",
    #     },
    #     {
    #         "menu": "Currículo",
    #         "page": "pages/37_Top_problemas.py",
    #         "title": "8. Top Problemas",
    #     },
    #     {
    #         "menu": "Currículo",
    #         "page": "pages/38_Novos_problemas_por_utente.py",
    #         "title": "9. Novos problemas por utente",
    #     },
    #     {
    #         "menu": "Currículo",
    #         "page": "pages/39_Problemas_agudos_por_médico.py",
    #         "title": "10. Problemas agudos por médico",
    #     },
    #     {
    #         "menu": "Currículo",
    #         "page": "pages/40_Risco_diabetes.py",
    #         "title": "11. Risco Diabetes",
    #     },
    #     {
    #         "menu": "Currículo",
    #         "page": "pages/41_Medicamentos_prescritos_utente.py",
    #         "title": "12. Medicamentos prescrito por utente",
    #     },
    #     {
    #         "menu": "Currículo",
    #         "page": "pages/42_Medicamentos_prescritos_médico.py",
    #         "title": "13. Medicamentos prescrito por Médico",
    #     },
    #     {
    #         "menu": "Outros",
    #         "page": "pages/98_sobre.py",
    #         "title": "Sobre",
    #     },
    # ]
