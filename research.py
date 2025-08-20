from langchain.agents import initialize_agent,Tool 
# from langchain.chat_models import ChatGoogleGenerativeAI 
from langchain_google_genai import ChatGoogleGenerativeAI
# from langchain_community.tools.duckduckgo_search.tool import DuckDuckGoSearchRun/
from langchain_community.tools import DuckDuckGoSearchRun


# from langchain.utilities import SerpAPIWrapper,WikipediaAPIWrapper
from langchain_community.utilities import SerpAPIWrapper, WikipediaAPIWrapper

from dotenv import load_dotenv 
load_dotenv()
from langchain.agents import create_react_agent,AgentExecutor
from langchain import hub 
prompt=hub.pull("hwchase17/react") 

llm=ChatGoogleGenerativeAI(
    model="gemini-1.5-flash"
)

# search=SerpAPIWrapper() 
search = DuckDuckGoSearchRun()

wiki=WikipediaAPIWrapper() 
tools=[
    Tool(name="Search",func=search.run,description="Useful for current events and factual web search"),
    Tool(name="Wikipedia",func=wiki.run,description="useful for historical or general topic summaries") 

]

agent=create_react_agent(
    llm=llm,
    tools=tools,
    prompt=prompt
)
agent_executor=AgentExecutor(agent=agent,tools=tools,verbose=True,)
def run_research(topic: str) -> str:
    prompt = f"""
    Conduct detailed research on the topic: "{topic}".
    Summarize it into bullet points with relevant facts, data, and historical context.
    Use trusted sources like Wikipedia or Google Search as needed.
    """
    # return agent_executor.run(prompt)
    return agent_executor.invoke({"input": prompt})["output"]
