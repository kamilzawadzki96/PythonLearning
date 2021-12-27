import requests
from bs4 import BeautifulSoup
import datetime

base_url = 'https://www.wykop.pl/hity/dnia/'
r = requests.get(base_url)
soup = BeautifulSoup(r.text)
content = soup.select('li[class*="link iC"]')

wykoplist = []

#get hity from wykop
for article in content:

    article_rating = article.span.contents[0]
    article_header = article.h2.a.contents[0]
    article_link = article.h2.a.get("href")
    row = [article_rating, article_header, article_link]
    wykoplist.append(row)

#print result
today = datetime.date.today()

print("Best 10 articles for date: " + today.strftime("%d %B, %Y"))
for rows in wykoplist[:10]:
    print("Upvotes: " + rows[0] + " / " + rows[1] + " / " + rows[2])