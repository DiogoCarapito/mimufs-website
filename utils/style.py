import streamlit as st


@st.cache_data()
def main_title(text):
    if len(text) > 25:
        fontsize = "2.5em"
    else:
        fontsize = "4em"
    st.markdown(
        "<style>"
        ".gradient-text {"
        "display: inline-block;"  # Changed from inline to inline-block
        f"font-size: {fontsize};"
        "font-weight: bold;"
        "width: 100%;"  # Added to make the span span the entire width
        "text-align: center;}"  # Added to center the text
        ".gradient {"
        "background: linear-gradient(to right, #FF6A00, #FFD800);"
        "-webkit-background-clip: text;"
        "-webkit-text-fill-color: transparent;}"
        "</style>"
        f'<span class="gradient-text"><span class="gradient">{text}</span></span>',
        unsafe_allow_html=True,
    )
    st.write("")


@st.cache_data()
def bottom_suport_email():
    st.divider()

    text = "© mimufs 2025 - Todos os direitos reservados"

    # link politia de privacidade e termos de utilização

    st.markdown(
        '<div style="text-align: center;">'
        '<p style="font-size: 16px;">Dúvidas, sugestões? Envia-nos um email para <a href="mailto:mgfhub.suporte@gmail.com" style="text-decoration: underline; font-size: 16px;">mgfhub.suporte@gmail.com</a></p>'
        f"{text}"
        "</div>",
        unsafe_allow_html=True,
    )
