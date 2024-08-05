from crewai import Crew,Process
from agents import blog_researcher, blog_writer
from tasks import reesearch_task, writer_task

#forming the tech focused crew with some enhanced configuraitons
crew = Crew(
    agents=[blog_researcher, blog_writer],
    tasks=[reesearch_task, writer_task],
    Process=Process.sequential,
    memory=True,
    cache=True,
    max_rpm=100,
    share_crew=True
)

##start the task execution process with enhanced feedback
result=crew.kickoff(inputs={'topic':'AI VS ML VS DL VS Data Science'})
print(result)