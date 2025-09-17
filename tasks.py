from crewai import Task

def idea_task(agent, raw_idea: str):
    return Task(
        description=f"""
        Your task is to take a raw, possibly vague startup idea {raw_idea} and refine it into a strong and investable business concept.
        You must structure your output into the following:
        1. **Startup Name**
        2. **Unique Value Proposition** : What makes it different from others.
        3. **Target Market** : Who it's for.
        4. **Revenue Model** : How it will make money.
        5. **Competitive Advantage** : Why it can win in this space.
        This refined concept will be used in the next tasks for market and launch planning.
        """,
        agent=agent,
        expected_output="""
        A bullet-point structured markdown output with the refined startup idea:
        - **Startup Name**:
        - **Unique Value Proposition**:
        - **Target Market**:
        - **Revenue Model**:
        - **Competitive Advantage**:
        """,
        output_file="outputs/refined_idea.md"        
        )

def market_task(agent, startup_idea: str, target_audience: str):
    return Task(
        description=f"""
        "Use this query: 'Top 3 competitors, unique oppurtunities and market gap for {startup_idea}' and summarize the result. DO NOT perform additional searches."
        Focus on the following target audience: **{target_audience}**
        Instructions:
        - Use the web search tool **ONLY ONCE**.
        - DO NOT perform a second search under any circumstance.

        Your final output should include:
        1. Top 3 direct competitors (briefly describe each)
        2. 2-3 market gaps or unmet needs
        3. 2-3 unique opportunities the startup can pursue

        Keep it concise, focused, and DO NOT re-search.
        """,
        agent=agent,
        expected_output="""
        A markdown report:
        ## Market Analysis
        ### Top 3 Competitors
        ### Market Gaps
        ### Opportunities
        """,
        output_file="outputs/market_analysis.md"
        
        )

def plan_task(agent, startup_idea: str, target_audience: str, budget: str):
    return Task(
        description=f"""
        Your task is to generate a **weekly launch roadmap** to build and launch the startup idea below.
        Startup idea: {startup_idea}
        Target Audience: {target_audience}
        Your total budget is in Indian currency rupees: {budget}.
        Your launch plan should be realistic within the stated budget and highly relevant to the audience.
        Output:
        1. the refined startup type.
        2. Why this startup can succeed (based on gaps & competition).
        3. A step-by-step launch plan (5-7 concise steps).
        4. A few ideas for scaling the startup post-launch.
        Make sure the plan feels tailored to the actual startup idea above - avoid generic business advice.
        """,
        agent=agent,
        expected_output="""
        ### Your AI-Powered Startup Plan for: [Startup Name]
        ## Type of Startup: 
        ## Why It Can Succeed: 
        ## Step-by-Step Launch Plan:
        ## Scaling Suggestions:
        """,
        output_file="outputs/startup_plan.md"
        )
