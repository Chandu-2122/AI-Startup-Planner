# AI-Startup-Planner

## Objective
Build a multi-agent AI system that helps founders plan their startups with a refined idea, competitor search, market analysis, and action plan.

## Tech & Requirements
- CrewAI, CrewAI Tools
- LangChain, LangChain Community, LangChain Ollama
- Streamlit
- DuckDuckGo Search

## Project Files
- agents.py → defines agents
- tasks.py → defines roles
- tools.py → definse tasks
- model.py → connects LLM backend
- main_app.py → Streamlit app
- requirements.txt → lists Python dependencies for the project
- startup_kit_YYYYMMDD_HHMMSS.zip → Output folder with files: refined_idea.md, market_analysis.md, startup_plan.md

## Challenges Faced
- Prompt engineering needed for reliable competitor search results.
- Sometimes outputs were too generic or repetitive.

## Learnings
- Multi-agent collaboration improves reasoning quality.
- Trusting AI output requires cross-checking sources, especially in market analysis.

## App Snippet 
![image](https://github.com/Chandu-2122/AI-Startup-Planner/blob/7071112cd16021eb5f7e7068618d2bde08ee2582/Screenshot%202025-09-17%20215630.png)


## Future Improvements
-  Add PDF/Excel export for plans.
-  Enhance competitor search with APIs like Crunchbase.
