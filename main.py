import streamlit as st
from agent.agent_chain import run_agent


# Access the API key stored in Streamlit secrets

st.set_page_config(page_title="Football Agent", layout="centered")

st.title("⚽ Football Performance Agent")
st.markdown("Ask me about any football team's recent performance!")
import streamlit as st
st.write("Football API Key Loaded:", bool(st.secrets.get("FOOTBALL_API_KEY")))
st.write("Football API Key Preview:", st.secrets.get("FOOTBALL_API_KEY")[:5])  # Only preview 5 chars

# Debug: check if secrets are being read
st.write("OpenAI Key Loaded:", bool(st.secrets.get("OPENAI_API_KEY")))
st.write("Football API Key Loaded:", bool(st.secrets.get("FOOTBALL_API_KEY")))

# Input box
user_input = st.text_input("Enter your prompt (e.g. 'How did Barcelona perform recently?')")

if st.button("Ask") and user_input:
    with st.spinner("Thinking..."):
        response = run_agent(user_input)
        st.markdown("### 📊 Response")
        st.write(response)