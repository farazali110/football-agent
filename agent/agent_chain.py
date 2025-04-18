import os
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.agents import initialize_agent, AgentType
from agent.tools import team_stats_tool
import streamlit as st

openai_api_key = st.secrets["OPENAI_API_KEY"]

# Load environment variables
load_dotenv()
# Initialize the LLM
llm = ChatOpenAI(
    model="openrouter/gpt-3.5-turbo",
    temperature=0.3,
    openai_api_key=openai_api_key,
    openai_api_base="https://openrouter.ai/api/v1"  # Custom OpenRouter endpoint
)

# Register your tools
tools = [team_stats_tool]

# Initialize the agent
agent_executor = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True  # Turn off in production if not needed
)

def run_agent(prompt: str) -> str:
    """Main function to get a response from the agent."""
    try:
        return agent_executor.run(prompt)
    except Exception as e:
        return f"Error: {e}"
