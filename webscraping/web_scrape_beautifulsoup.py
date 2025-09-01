import requests
from bs4 import BeautifulSoup

url = "https://www.boxofficemojo.com/chart/top_lifetime_gross/?area=XWW"

response = requests.get(url)
response.raise_for_status()
# print(response.text)
website = response.content

soup = BeautifulSoup(website, 'lxml')
results = soup.select("tr")

for tr in results:
    print(tr.text)