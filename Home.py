import streamlit as st

st.set_page_config(
    page_title="Home",
    page_icon="👋",
)

st.title("Welcome to My TxTStable! 👋")

st.markdown(
    """
    ### TxTStable using Stable Diffusion:
    The application allows users to input a piece of text and generate an image that is related to the input text. 
    - Hugging Face Model: [stable-diffusion-v1-5](https://huggingface.co/runwayml/stable-diffusion-v1-5)
    - Github model: [github](https://github.com)
"""
)
