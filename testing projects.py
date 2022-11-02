from bs4 import BeautifulSoup
import urllib.request

url = "https://padellands.com/europa/pistas/pistas-en-suecia/"
ourUrl = urllib.request.urlopen(url)

soup = BeautifulSoup(ourUrl, 'html.parser')  # Tenemos la soup: HTML sin formato para la url en cuestión.

review = []
for i in soup.find_all('div', {'class': 'review-content'}):
    per_review = i.find('p')
    print(per_review)
    review.append(per_review)