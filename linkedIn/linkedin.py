import os
import requests
def get_li_data(linkedin_profile_url,bool=False):
    if bool:
        api_key = os.environ.get('PROXYCURL_API_KEY')
        print(api_key)
        headers = {'Authorization':'Bearer '+ api_key}
        api_endpoint = 'https://nubela.co/proxycurl/api/v2/linkedin'
        respone = requests.get(api_endpoint,params={'url':linkedin_profile_url},headers=headers)
    else:
        linkedin_profile_url = "https://gist.githubusercontent.com/emarco177/0d6a3f93dd06634d95e46a2782ed7490/raw/78233eb934aa9850b689471a604465b188e761a0/eden-marco.json"
        
        response = requests.get(
            linkedin_profile_url,
            timeout=10,
        )
    data = response.json()
    data = {
        k: v
        for k, v in data.items()
        if v not in ([], "", "", None)
        and k not in ["people_also_viewed", "certifications"]
    }
    if data.get("groups"):
        for group_dict in data.get("groups"):
            group_dict.pop("profile_pic_url")
    return data