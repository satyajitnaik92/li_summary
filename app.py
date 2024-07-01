import os
from dotenv import load_dotenv
from tools.tools import get_li_url
from linkedIn.linkedin import get_li_data
from langchain_openai import ChatOpenAI

from langchain import hub
load_dotenv()

print(get_li_url("satyajit naik bajaj finance"))
# data = get_li_data('https://www.linkedin.com/in/satyajit-naik-8140a495/')
# print(data)
