import os
from dotenv import load_dotenv
from tools.tools import get_li_url
from linkedIn.linkedin import get_li_data
from langchain_openai import ChatOpenAI
from langchain.prompts.prompt import PromptTemplate
from langchain.chains import LLMChain
from langchain import hub
import sys
load_dotenv()

import warnings
warnings.filterwarnings("ignore")

def helpUsage():
    print("Specify Params: <name and employer name>")
    print("Specify Param: --help for usage")

def driver_function(name):
    linkedIn_url = get_li_url(name)
    linkedIn_data = get_li_data(linkedIn_url)
    summary_template = """
        given the Linkedin information {information} about a person I want you to create:
        1. A short summary
        2. two interesting facts about them
        """
    summary_prompt_template = PromptTemplate(
            input_variables=["information"], template=summary_template
        )

    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

    chain = LLMChain(llm=llm, prompt=summary_prompt_template)

    res = chain.invoke(input={"information": linkedIn_data})

    return res['text']
if __name__ == '__main__':
    args = sys.argv
    name = args[1]
    print(name)
    if args[1] == '--help':
        helpUsage()
    elif len(args) == 2 :
        summary=driver_function(name)
        print(summary)
    else:
        helpUsage()
    


