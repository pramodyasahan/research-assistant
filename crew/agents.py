from crewai import Agent
from crewai_tools import SerperDevTool, SpiderTool

# Tools
search_tool = SerperDevTool()
scrape_tool = SpiderTool()


