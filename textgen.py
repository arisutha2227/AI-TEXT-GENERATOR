import streamlit as st
from transformers import pipeline
# page settings 
st.set_page_config (
    page_title="AI Text Generator",
    page_icon="🤖"
)
#title
st.title("🤖 AI Text Generator")
st.write("✨ Enter a sentence and let AI complete it!")
#load model
@st.cache_resource
def load_model():
    return pipeline(
        "text-generation",
        model="distilgpt2"
    )
generator=load_model()
#user input
prompt= st.text_area(
    "✍ Enter your text:",
    placeholder="Artificial Intelligence is... "
)
#generotor button
if st.button("✨ Generate Text"):
    if prompt:
        with st.spinner("🤖 Generating..."):
            result=generator(
                prompt,
                max_new_tokens=50,
                num_return_sequences=1,
            )
        generated_text=result[0]["generated_text"]
        st.subheader("📝 Generated Text")
        st.write(generated_text)
    else:
        st.warning("⚠ please enter some text first!")
