from google.adk.agents.llm_agent import Agent

def read_cv_file(file_path : str) -> str:
    """
    Reads the content of a CV file and returns it as a string.
    
    Args:
        file_path (str): The path to the CV file.

    Returns:
        str: The content of the CV file.
    """
    with open(file_path, 'r') as f:
        return f.read()

job_searchs_agent = Agent(
    model='gemini-3.5-flash',
    name='job_searchs_agent',
    description='Agent that helps users search for jobs based on their CV and preferences',
    instruction='Answer user questions to the best of your knowledge',
)
