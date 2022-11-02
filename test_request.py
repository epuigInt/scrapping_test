from urllib.request import urlopen

quote_page = "https://padellands.com/europa/pistas/pistas-en-suecia/"

page = urlopen(quote_page)
print(page)