from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.duckduckgo import DuckDuckGo
from phi.tools.yfinance import YFinanceTools
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
os.environ["PHI_API_KEY"] = os.getenv("PHI_API_KEY")

# Set up model
llm_model = Groq(id="meta-llama/llama-4-scout-17b-16e-instruct")

# Web search agent
web_search_agent = Agent(
    name="Web Search",
    role="Search the web and provide external context",
    model=llm_model,
    tools=[DuckDuckGo()],
    instructions=[
        "Always include sources in your answer.",
        "Summarize information clearly using markdown."
    ],
    show_tool_calls=True,
    markdown=True
)

# Financial data agent
finance_agent = Agent(
    name="Finance Expert",
    role="Analyze stock data, company news, and analyst recommendations.",
    model=llm_model,
    tools=[YFinanceTools(
        stock_price=True,
        stock_fundamentals=True,
        company_news=True,
        analyst_recommendations=True
    )],
    instructions=[
        "Use tables to show stock data.",
        "Summarize financial indicators and news concisely."
    ],
    show_tool_calls=True,
    markdown=True
)

# Master agent that coordinates sub-agents
master_agent = Agent(
    name="Chief Analyst AI",
    role="Analyze the user's request, delegate subtasks to the right agents, and return a combined answer.",
    model=llm_model,
    team=[web_search_agent, finance_agent],
    instructions=[
        "Break the task into logical steps.",
        "Use the right agent for each step.",
        "Combine the results clearly using markdown and tables.",
        "Include source links where available."
    ],
    show_tool_calls=True,
    markdown=True
)


if __name__ == "__main__":
    while True:
        user_input = input("\n Ask your Chief Analyst AI something (or type 'exit'): ")
        if user_input.lower() in ["exit", "quit"]:
            print("Exiting.")
            break

        print("\n AI is thinking...\n")
        try:
            response = master_agent.run(user_input, additional_information="", stream=False)
            print(response.content)
        except Exception as e:
            print("Error occurred:", e)
