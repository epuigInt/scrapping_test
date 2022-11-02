import requests
from bs4 import BeautifulSoups
from urllib.request import urlopen

headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '3600',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
    }
url = 'https://padellands.com/europa/pistas/pistas-en-suecia/'
page = requests.get(url, headers)



soup = BeautifulSoup(page.content, 'html.parser')
print(soup.prettify())
# Create top_items as empty list
clubs = []

# Extract and store in top_items according to instructions on the left
products = soup.contents.index(3).select('sabai-entity sabai-entity-type-content sabai-entity-bundle-name-sueciapistas-listing sabai-entity-bundle-type-directory-listing sabai-entity-mode-summary sabai-clearfix')
for club in products:
    title = club.select('sabai-directory-title > a.title')[0].text
    location_label = club.select('div.sabai-directory-location')[0].text
    contact_label = club.select('div.sabai-directory-contact')[0].text
    city_label = club.select('div.sabai-field-label')[0].text
    ncourts_label = club.select('div.sabai-field-value')[0].text
    info = {
        "title": title.strip(),
        "location": location_label.strip(),
        "contact": contact_label.strip(),
        "city": city_label.strip(),
        "ncourts": ncourts_label()
    }
    clubs.append(info)

print(clubs)