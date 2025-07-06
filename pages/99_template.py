import streamlit as st

st.title("Title")

st.subheader("Subtitle")

st.header("Header")

st.markdown(
    """text

> centererd highlight text"""
)

st.image("content/images/Inicio.png", caption="image")

st.markdown("[mimufs.com](https://mimufs.com)")

st.video("https://www.youtube.com/watch?v=n3k-dIykQaw")

st.markdown(
    """<!-- <iframe src="videos/Timeline_1.mp4" frameborder="0"></iframe> -->"""
)
