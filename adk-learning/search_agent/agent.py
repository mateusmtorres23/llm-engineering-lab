from google.adk.agents import Agent 
from google.adk.tools import google_search
 
root_agent = Agent(
    name="search_agent",
    model="gemini-2.5-pro",
    description="Agent especialized in google adk, always using Google Search to answer correctly.",
    instruction="I can answer your questions by searching the internet. Just ask me anything about google adk!",
    tools=[google_search]
)