# Financial Analyst Agent

This project is a multi-agent financial assistant built using the `phi` framework and Groq's LLaMA models. It combines web search and real-time stock market data to provide summaries, analyst recommendations, and the latest news for companies like NVDA.

## Features

- Web search using DuckDuckGo
- Real-time stock data using Yahoo Finance
- Uses Groq's LLaMA 4 Scout 17B model
- Multi-agent setup (web + financial agents)
- Optional support for OpenAI GPT-4o

## Folder Structure

- `financial_agent.py` – Main agent script
- `playground.py` – Duplicate or testing script
- `.env` – Environment variables (not included in GitHub)
- `requirements.txt` – Python dependencies

## Setup Instructions

1. Clone the repository:

git clone https://github.com/ashishpathak0933/financial_analyst_agent.git
cd financial_analyst_agent


2. Create and activate a Conda environment:
conda create --prefix ./venv python=3.12
conda activate ./venv

markdown
Copy
Edit


3. Install required Python packages:
pip install -r requirements.txt

## Environment Variables

Create a `.env` file in the root directory and add your API keys:

GROQ_API_KEY=your_groq_key_here
PHI_API_KEY=phi_api_key
OPENAI_API_KEY=your_openai_key_here # Optional, only needed if using OpenAI

## Running the Agent

Run the main script to start the multi-agent:


The agent will respond with analyst recommendations, financial news, and the current stock price.

## Switching to OpenAI (Optional)

To use OpenAI’s GPT-4o instead of Groq:

1. Import OpenAI:

```python
from phi.model.openai import OpenAIChat

model = OpenAIChat(id="gpt-4o")



