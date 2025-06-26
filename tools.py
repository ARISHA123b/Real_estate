import os
from dotenv import load_dotenv
from crewai_tools import SerperDevTool

# Load environment variables from .env file
load_dotenv()

# Ensure the API key is available
api_key_1 = os.getenv("SERPER_API_KEY")

# Initialize the Serper search tool (it reads the API key from env)
search_tool = SerperDevTool()
