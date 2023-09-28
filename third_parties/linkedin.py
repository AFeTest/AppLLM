import os
import requests

def scrape_linkedin_profile(linkedin_profile_url: str):
    """
    scrape information from linkedin profile,
    Manually scrape the information from the linkedin profile"""

    proxycurl_api_key = os.getenv("PROXYCURL_API_KEY")
    api_endpoint = 'https://nubela.co/proxycurl/api/v2/linkedin'
    header_dic = {'Authorization': f'Bearer {proxycurl_api_key}'}
    response = requests.get(
        api_endpoint, params={"url": linkedin_profile_url}, headers=header_dic
    )
    # Remove empty fields:
    response_clean_data = clean_data(response)

    return response_clean_data

def clean_data(res):
    data = res.json()
    data = {
        k: v
        for k, v in data.items()
        if v not in ([], "", "", None)
           and k not in ["people_also_viewed","certifications"]
    }
    if data.get("groups"):
        for group_dict in data.get("groups"):
            # remove profile_picture from the data
            group_dict.pop("profile_pic_url")

    return data