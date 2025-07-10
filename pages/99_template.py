import streamlit as st

st.title("Title")

st.header("Subtitle")

st.subheader("Header")

st.markdown("""text""", unsafe_allow_html=True)

st.info("""centererd highlight text""")

st.image("content/images/Inicio.png", caption="image")

st.markdown("[mimufs.com](https://mimufs.com)", unsafe_allow_html=True)

st.video("https://www.youtube.com/watch?v=n3k-dIykQaw")

st.markdown(
    """<!-- <iframe src="videos/Timeline_1.mp4" frameborder="0"></iframe> -->""",
    unsafe_allow_html=True,
)
