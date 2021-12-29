import requests
from bs4 import BeautifulSoup
import datetime
import sys

def hotArticlesWykop(url, today):
    base_url = 'https://www.wykop.pl/hity/' + url
    r = requests.get(base_url)
    soup = BeautifulSoup(r.text)
    content = soup.select('div[class*="article"]')

    wykoplist = []

    #get hity from wykop
    for article in content:
        try:
            article_rating = article.span.contents[0]
            article_header = article.h2.a.contents[0]
            article_link = article.h2.a.get("href")
            article_date = article.time.contents[0]
            row = [article_rating, article_date, article_header, article_link]
            wykoplist.append(row)
        except AttributeError:
            continue

    #print result

    print("Best 10 articles for date: " + today.strftime("%d %B, %Y") + "\n")
    for rows in wykoplist[:10]:
        print("Upvotes:" + rows[0] + " / " + rows[1] + " / " + rows[2] + " / " + rows[3])
    print("")

today = datetime.date.today()

articlerange = {
    'y': "roku/"+today.strftime("%Y"),
    'm': "miesiaca/"+today.strftime("%Y/%m"),
    'w': "tygodnia",
    'd': "dnia"
}

while True: 
    #url = input("Give me range of date articles, that are you interested in (y - yearly, m - monthly, w - weekly, d - daily, q to quit program): ")
    url = sys.argv[1]



    if url == 'y' or url == 'm' or url == 'w' or url == 'd':
            range = articlerange[url]
            hotArticlesWykop(range, today)
    else:
        if url == 'q':
            print("Bye bye!")
            break
        else:
            print("Give me value form printed range!")
    
    input()