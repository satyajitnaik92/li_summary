import os
from dotenv import load_dotenv
from linkedIn.linkedin import get_li_data
load_dotenv()
data = get_li_data('https://www.linkedin.com/in/satyajit-naik-8140a495/')
print(data)
