from crewai import Task
from tools import yt_tool
from agents import blog_researcher, blog_writer


#Researcher task
reesearch_task = Task(
    description="Uncover cutting-edge advancements in {topic}",
    expected_output="List of top 5 cutting-edge advancements in {topic}",
    tools=[yt_tool],
    agent=blog_researcher,
)

#Writer task
writer_task = Task(
    description="Write a blog post on {topic}",
    expected_output="Write a blog post on {topic}",
    tools=[yt_tool],
    agent=blog_writer,
    async_execution=False,
    output_file='new-blog-post.md'
)