from crewai import Task

def get_tasks(agents, user_input, context=""):
    idea_generator, market_researcher, business_strategist, pitch_creator = agents

    context_block = f"\n\nConversation context:\n{context}" if context else ""

    idea_task = Task(
        description=(
            f"The user wants startup ideas related to: '{user_input}'{context_block}\n\n"
            "Generate exactly 3 distinct AI-powered startup ideas. For each idea provide:\n"
            "- Startup name\n"
            "- One-line description\n"
            "- Core AI technology used\n"
            "- Problem it solves\n"
            "Format clearly with headers."
        ),
        agent=idea_generator,
        expected_output="3 structured startup ideas with name, description, AI tech, and problem.",
    )

    market_task = Task(
        description=(
            "Take the 3 startup ideas from the previous task and research each one:\n"
            "- Estimated market size (TAM/SAM)\n"
            "- Top 3 existing competitors\n"
            "- Primary target audience\n"
            "- Key trend supporting this idea\n"
            "Format each idea as a separate research report."
        ),
        agent=market_researcher,
        expected_output="Market research report for all 3 ideas with market size, competitors, audience, and trends.",
        context=[idea_task],
    )

    strategy_task = Task(
        description=(
            "Based on the market research, select the BEST startup idea and create:\n"
            "1. Go-To-Market strategy (3 phases)\n"
            "2. Revenue model (pricing, streams)\n"
            "3. 6-month execution roadmap with milestones\n"
            "4. Initial budget estimate (low-cost if previous context mentions it)\n"
            "Be specific and actionable."
        ),
        agent=business_strategist,
        expected_output="Full GTM strategy, revenue model, roadmap, and budget for the best idea.",
        context=[idea_task, market_task],
    )

    pitch_task = Task(
        description=(
            "Create a complete investor pitch deck OUTLINE for the chosen startup:\n"
            "Slide 1: Hook + Company Name\n"
            "Slide 2: Problem (with data)\n"
            "Slide 3: Solution\n"
            "Slide 4: Market Opportunity\n"
            "Slide 5: Business Model\n"
            "Slide 6: Traction / Roadmap\n"
            "Slide 7: Team\n"
            "Slide 8: The Ask (funding amount + use of funds)\n"
            "Make it compelling and investor-ready."
        ),
        agent=pitch_creator,
        expected_output="8-slide investor pitch deck outline with content for each slide.",
        context=[idea_task, market_task, strategy_task],
    )

    return [idea_task, market_task, strategy_task, pitch_task]