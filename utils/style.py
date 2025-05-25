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
