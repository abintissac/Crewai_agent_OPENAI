from crewai import Agent
from tools import yt_tool

from dotenv import load_dotenv
load_dotenv()
import os

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_MODEL_NAME"] = os.getenv("gpt-4-0125-preview")


##Create a senior blog content researcher 

blog_researcher = Agent(
    role='Senior Researcher',
    goal='Uncover cutting-edge advancements in {topic}',
    verbose=True,
    memory=True,
    backstory=(
        "expert in understanding videos in AI and Data Science"
    ),
    tools=[yt_tool],
    allow_delegation=True
)

#Creating a writer for blog content
blog_writer = Agent(
    role='Writer',
    goal='Write a blog post on {topic}',
    verbose=True,
    memory=True,
    backstory=(
        "expert in writing blogs in AI and Data Science"
    ),
    tools=[],
    allow_delegation=True
)