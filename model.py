# model
from crewai import LLM
from langchain_ollama.llms import OllamaLLM

llm = LLM(
    model="ollama/llama3.2:latest",
    base_url="http://127.0.0.1:11434"
)