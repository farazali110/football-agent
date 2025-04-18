import streamlit as st
from agent.agent_chain import run_agent

# Access the API key stored in Streamlit secrets
api_key = st.secrets["api_keys"]["OPENAI_API_KEY"]

st.set_page_config(page_title="Football Agent", layout="centered")

st.title("⚽ Football Performance Agent")
st.markdown("Ask me about any football team's recent performance!")

# Input box
user_input = st.text_input("Enter your prompt (e.g. 'How did Barcelona perform recently?')")

if st.button("Ask") and user_input:
    with st.spinner("Thinking..."):
        response = run_agent(user_input)
        st.markdown("### 📊 Response")
        st.write(response)