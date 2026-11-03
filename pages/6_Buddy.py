import streamlit as st
import ollama

st.title("🤖 Study Buddy")

MODEL = "qwen2.5:3b"
SYSTEM_PROMPT = (
    "You are a friendly study buddy for Indian college students. "
    "Keep answers short and encouraging. "
    "Never do math yourself; if asked for CGPA or attendance numbers, "
    "say you will check with the calculator."
)

if "messages" not in st.session_state:
    st.session_state.messages = []

# Show earlier messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# New message
if prompt := st.chat_input("Ask your study buddy..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            reply = ollama.chat(
                model=MODEL,
                messages=[{"role": "system", "content": SYSTEM_PROMPT}]
                + st.session_state.messages,
            )
            answer = reply["message"]["content"]
        st.write(answer)

    st.session_state.messages.append({"role": "assistant", "content": answer})