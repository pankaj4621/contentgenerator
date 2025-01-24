"""
This module defines the tools used in the News AI project.
Tools provide additional capabilities to the agents, such as internet searching.
"""

from dotenv import load_dotenv
load_dotenv()
import os

# Set the SERPER API key from the environment variables
os.environ['SERPER_API_KEY'] = os.getenv('SERPER_API_KEY')

from crewai_tools import SerperDevTool

# Initialize the tool for internet searching capabilities
tool = SerperDevTool()