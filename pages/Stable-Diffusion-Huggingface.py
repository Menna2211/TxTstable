import streamlit as st
import torch
import time
from optimum.onnxruntime import ORTStableDiffusionPipeline

@st.cache_resource(show_spinner=False ,ttl=3600) 
def get_model():
    model_id = "runwayml/stable-diffusion-v1-5"
    pipe = ORTStableDiffusionPipeline.from_pretrained(model_id, framework="pt")
    return pipe
    return pipe

pipe=get_model()

st.title("Stable Diffusion App")
# define the layout of your app

# Define the Streamlit app layout
prompt = st.text_input("Write your sentence:")
submit_button = st.button("Compute")
if not submit_button:
  time.sleep(3)
  st.warning('Please Press Compute....')
  st.stop()

# Display the generated text
if submit_button:
    progress_text = "Operation in progress. Please wait."
    bar = st.progress(0, text=progress_text)
    for percent_complete in range(100):
        generated_img=pipe(prompt).images[0]
        time.sleep(0.1)
        bar.progress(percent_complete + 1, text=progress_text)

    st.write("Generated Image:")
    st.image(generated_img)
    time.sleep(5)
    st.success('Congratulations task is done ', icon="✅")
    st.balloons()
