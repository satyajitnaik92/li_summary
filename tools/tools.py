from langchain_community.tools.tavily_search import TavilySearchResults
from dotenv import load_dotenv
from langchain_core.tools import Tool
from langchain_openai import ChatOpenAI
from langchain.prompts.prompt import PromptTemplate
from langchain import hub
load_dotenv()

search = TavilySearchResults()

def find_url(query):
    result = search.run(query)
    return result[0]['url']

li_url_tool = Tool.from_function(name="Google crawler for linkedin profile page",func=find_url,description="useful for when you need to get the Linkedin page URL")

from langchain.agents import create_react_agent, AgentExecutor

llm = ChatOpenAI(model="gpt-3.5-turbo",temperature=0)
react_prompt = hub.pull("hwchase17/react")

def get_li_url(name):
    agent = create_react_agent(llm,tools=[li_url_tool],prompt=react_prompt)
    agent_executor = AgentExecutor(agent=agent,tools=[li_url_tool],verbose=True)
    template = """given the full name and employer name {name_and_employer_name} i want you to find the url to their linkedin profile page. You should return only a url. Don't return public url for all matched profiles. It should be a URL to their linkedin profile page."""
    prompt_template = PromptTemplate(template=template,input_variables=['name_and_employer_name'])
    result = agent_executor.invoke({"input":prompt_template.format_prompt(name_and_employer_name=name)})
    return result['output']