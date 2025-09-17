# agents
from crewai import Agent
from model import llm
from tools import search_web_tool

# Agent to refine startup ideas
idea_expert = Agent(
    role="Startup Idea Expert",
    goal="Generate creative startup ideas",
    backstory="You specialize in coming up with innovative ideas for entrepreneurs.",
    llm=llm
)

# Agent to analyze the market using the web search tool
market_expert = Agent(
    role="Market Research Expert",
    goal="Analyze competitors and market gaps",
    backstory="You help entrepreneurs understand the market landscape.",
    llm=llm,
    allow_delegation=False,
    max_iterations=2   # prevents infinite loops

)

# Agent to create a launch plan
plan_expert = Agent(
    role="Planning Expert",
    goal="Build actionable business plans",
    backstory="You create step-by-step business plans based on validated ideas.",
    llm=llm
)
