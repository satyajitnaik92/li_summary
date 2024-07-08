# LinkedIn Summary
This project gives the summary of linkedIn profile by entering the name and employer name of a person.
# Installation Instruction
To run it clone the repository and then navigate to the folder. To run using pipenv package manager  
    1. Install pipenv package - "pip install pipenv"  
    2. Creates a environment with required libraries using the pipFile - "pipenv install"  
    3. Activate the environment - "pipenv shell"  
# Usage Instruction
Sign up and get below API keys and save them in .env file.
- [OPENAI_API_KEY](https://help.openai.com/en/articles/4936850-where-do-i-find-my-openai-api-key).
- [TAVILY_API_KEY](https://app.tavily.com/sign-in).
- [PROXUCURL_API_KEY](https://nubela.co/proxycurl/linkedin).

To get the results run "pipenv run app.py <name_employer_name>"