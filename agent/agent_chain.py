import os
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.agents import initialize_agent, AgentType
from agent.tools import team_stats_tool

load_dotenv()

# Set up OpenAI LLM
llm = ChatOpenAI(
    model="gpt-3.5-turbo",  # Or gpt-4 if you have access
    temperature=0.3,
    openai_api_key=os.getenv("OPENAI_API_KEY")
)

# Register your tools
tools = [team_stats_tool]

# Initialize the agent
agent_executor = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True  # Useful for debugging
)


def run_agent(prompt: str) -> str:
    """Main function to be used by the app or CLI to get a response."""
    try:
        result = agent_executor.run(prompt)
        return result
    except Exception as e:
        return f"Error: {e}"