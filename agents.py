from crewai import Agent
from langchain_community.tools import DuckDuckGoSearchRun

search_tool = DuckDuckGoSearchRun()

def get_agents():
    idea_generator = Agent(
        role="Startup Idea Generator",
        goal=(
            "Generate 3 unique, creative, and viable AI-based startup ideas "
            "based on the user's domain or interest. Focus on novelty and feasibility."
        ),
        backstory=(
            "You are a serial entrepreneur with deep knowledge of AI/ML trends. "
            "You have launched 5 startups and have a sharp eye for market gaps."
        ),
        tools=[search_tool],
        verbose=True,
        allow_delegation=False,
    )

    market_researcher = Agent(
        role="Market Researcher",
        goal=(
            "For each startup idea provided, research the market size, key competitors, "
            "target audience, and current trends. Provide data-backed insights."
        ),
        backstory=(
            "You are an expert market analyst who has consulted for Fortune 500 companies "
            "and understands how to evaluate market opportunities with precision."
        ),
        tools=[search_tool],
        verbose=True,
        allow_delegation=False,
    )

    business_strategist = Agent(
        role="Business Strategist",
        goal=(
            "Create a Go-To-Market strategy, revenue model, and execution roadmap "
            "for the best startup idea. Include cost estimates and timeline."
        ),
        backstory=(
            "You are a McKinsey-trained strategist with expertise in scaling startups "
            "from zero to revenue in under 12 months."
        ),
        tools=[],
        verbose=True,
        allow_delegation=False,
    )

    pitch_creator = Agent(
        role="Investor Pitch Creator",
        goal=(
            "Create a compelling, structured investor pitch deck outline for the startup. "
            "Include hook, problem, solution, traction, team, and ask."
        ),
        backstory=(
            "You are a pitch coach who has helped startups raise over $50M in funding. "
            "You know exactly what investors want to hear."
        ),
        tools=[],
        verbose=True,
        allow_delegation=False,
    )

    return idea_generator, market_researcher, business_strategist, pitch_creator