from google.adk.agents.llm_agent import Agent


job_searchs_agent = Agent(
    model='gemini-3.5-flash',
    name='job_searchs_agent',
    description='Agent that helps users search for jobs based on their CV and preferences',
    instruction='Answer user questions to the best of your knowledge',
)
