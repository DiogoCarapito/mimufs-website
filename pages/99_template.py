import streamlit as st

st.title("Title", anchor=False)

st.header("Subtitle", anchor=False)

st.subheader("Header", anchor=False)

st.markdown("""text""")

st.info("""centererd highlight text""")
st.image("content/images/Inicio.png", caption="image")
st.markdown("[mimufs.com](https://mimufs.com)")

st.video("https://www.youtube.com/watch?v=n3k-dIykQaw")

st.divider()

st.markdown(
    '<div style="text-align: center;">'
    '<p style="font-size: 16px;">Dúvidas, sugestões? Envia-nos um email para <a href="mailto:mgfhub.suporte@gmail.com" style="text-decoration: underline; font-size: 16px;">mgfhub.suporte@gmail.com</a></p>'
    "</div>",
    unsafe_allow_html=True,
)
