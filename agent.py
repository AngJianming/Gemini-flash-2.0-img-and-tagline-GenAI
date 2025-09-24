from google.adk.agents.llm_agent import Agent

root_agent = Agent(
  model='gemini-2.5-flash',  
  name='root_agent',  # this can be any unique name
  description='A helpful assistant for user questions',  
  instruction='Answer user question to the best of your knowledge',  
)