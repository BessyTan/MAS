from crewai_tools import SerperDevTool
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def get_research_tools():
    """
    Initialize and return research tools for the agents.
    Currently includes SerperDevTool for web search capabilities.
    """
    serper_tool = SerperDevTool(
        api_key=os.getenv("SERPER_API_KEY"),
        search_type="search"  # Can be "search", "places", or "news"
    )
    
    return [serper_tool] 