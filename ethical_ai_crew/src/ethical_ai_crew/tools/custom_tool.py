from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
from crewai_tools import SerperDevTool
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class MyCustomToolInput(BaseModel):
    """Input schema for MyCustomTool."""
    argument: str = Field(..., description="Description of the argument.")

class MyCustomTool(BaseTool):
    name: str = "Name of my tool"
    description: str = (
        "Clear description for what this tool is useful for, your agent will need this information to use it."
    )
    args_schema: Type[BaseModel] = MyCustomToolInput

    def _run(self, argument: str) -> str:
        # Implementation goes here
        return "this is an example of a tool output, ignore it and move along."

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
