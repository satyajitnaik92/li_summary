# LinkedIn Summary
This project gives the summary of linkedIn profile by entering the name and employer name of a person.
# Installation Instruction
To run it clone the repository and then navigate to the folder. To run using pipenv package manager
1. Install pipenv package - "pip install pipenv"
2. Creates a environment with required libraries using the pipFile - "pipenv install" (It automatically detects the mentioned libraries and versions using Pipfile and installs them)
3. Activate the environment - "pipenv shell"
4. You can also use requirements.txt file to create the environment.
# Environment Variables
Sign up and get below API keys.
- [OPENAI_API_KEY](https://help.openai.com/en/articles/4936850-where-do-i-find-my-openai-api-key).
- [TAVILY_API_KEY](https://app.tavily.com/sign-in).
- [PROXUCURL_API_KEY](https://nubela.co/proxycurl/linkedin).
# Usage Instruction
To get the results run "pipenv run app.py <name_employer_name>" using pipenv package manager.
You can also run by "python3 app.py <name_employer_name>"
Example- 
1. python3 app.py "satyajit naik bajaj finance"
2. pipenv run app.py "satyajit naik bajaj finance"