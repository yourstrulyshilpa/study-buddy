import streamlit as st
import ollama

st.title("Study Buddy: smoke test")

if st.button("Say hello to the model"):
    with st.spinner("Thinking..."):
        reply = ollama.chat(
            model="qwen2.5:3b",
            messages=[
                {"role": "user", "content": "Say hello to a college student in one friendly sentence."}
            ],
        )
    st.success(reply["message"]["content"])