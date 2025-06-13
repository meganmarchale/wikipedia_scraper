import requests

def get_leaders():
    root_url = "https://country-leaders.onrender.com"
    cookie_url = "https://country-leaders.onrender.com/cookie"
    leaders_url = "https://country-leaders.onrender.com/leaders"

    cookies = requests.get(cookie_url)
    cookies = cookies.cookies
    print(f"This is the cookie: {cookies}.")

    countries = requests.get(f"{root_url}/countries", cookies=cookies).json()
    print(f"The countries are: {countries}.")

    leader_per_country = {}
    for country in countries:
        leader_per_country[country] = requests.get(leaders_url, cookies=cookies, params={"country":country}).json()
    return leader_per_country

get_leaders()




leaders_per_country = get_leaders()
for leader in leaders_per_country:
    print(leaders_per_country[leader])



def get_text():
    root_url = "https://country-leaders.onrender.com"
    cookie_url = "https://country-leaders.onrender.com/cookie"
    leaders_url = "https://country-leaders.onrender.com/leaders"
    cookies = requests.get(cookie_url)
    cookies = cookies.cookies

    leaders_fr = requests.get(leaders_url, cookies=cookies, params={"country":"fr"}).json()
    #print(leaders_fr)

    url_list = []
    for elem in leaders_fr:
        url_list.append(elem["wikipedia_url"])
        #print(url_list)

    wikipedia_display = requests.get(url_list[0])
    return wikipedia_display.text
        
get_text()




# 10 lines
import requests
from bs4 import BeautifulSoup
import re

def get_first_paragraph(wikipedia_url: str):
    req = requests.get(wikipedia_url)
    soup = BeautifulSoup(req.text, "html.parser")
    content = soup.select("#mw-content-text > div.mw-parser-output > p")    
    paragraphs = []
    for p in content:
        if len(p.getText(strip=True)) > 0:
            paragraphs.append(p)
        else:
            continue
    first_paragraph = paragraphs[0].get_text(strip=True)
    
    patterns = [r"/[^/]*/\s*;\s*", r"r\/.*\/", r"\[.*?\]", r"ⓘ"]
    
    for pattern in patterns:
        first_paragraph = re.sub(pattern, "", first_paragraph)

    return first_paragraph.strip()

# Test
print(get_first_paragraph("https://fr.wikipedia.org/wiki/Fran%C3%A7ois_Hollande"))