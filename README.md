# AI Startup Idea Generator

A multi-agent AI system built with CrewAI and Gradio that generates 
startup ideas, researches markets, builds strategy, and creates investor pitches.

## Agents
- Idea Generator
- Market Researcher  
- Business Strategist
- Pitch Creator

## Setup
1. Clone the repo
2. Create virtual environment: `python3 -m venv venv`
3. Activate: `source venv/bin/activate`
4. Install dependencies: `pip install -r requirements.txt`
5. Add your OpenAI key to `.env`: `OPENAI_API_KEY=sk-...`
6. Run: `python3 app.py`

## Tech Stack
- CrewAI
- Gradio
- OpenAI GPT
- LangChain
- DuckDuckGo Search
