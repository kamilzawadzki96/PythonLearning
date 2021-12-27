import requests
from bs4 import BeautifulSoup

base_url = 'https://www.wykop.pl/hity/dnia/'
r = requests.get(base_url)
soup = BeautifulSoup(r.text)
content = soup.select('li[class*="link iC"]')

wykoplist = []

for article in content:

    article_rating = article.span.contents[0]
    article_header = article.h2.a.contents[0]
    article_link = article.h2.a.get("href")
    row = [article_rating, article_header, article_link]
    wykoplist.append(row)

print(wykoplist)