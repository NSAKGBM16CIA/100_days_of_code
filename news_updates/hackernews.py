import requests
from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv
# import lxml

def write_to_text(text):
    with open("hackernews.txt", 'a') as file:
        file.write(text)


def get_news_list():

    load_dotenv()
    url = os.getenv('')
    page = requests.get("https://news.ycombinator.com/news")
    page.raise_for_status()
    news_page = page.text
    # print(news_page)

    soup = BeautifulSoup(news_page, 'html.parser')
    news_titles = []
    news_links = []
    news_scores = []

    titles = soup.select(".titleline")
    # link get(href) title getText()
    scores = soup.select(selector=".score")

    for i in range(len(titles)):

        try:
            title = titles[i].getText()
            print(title)
            link = str(titles[i]).split('"')[3]  #get('a') then get('href')
            print(link)
            print(scores[i].get_text())
            score = int(scores[i].getText())  #.split(' ')[0])  #take the number of a string like 34 Points
            news_titles.append(title)
            news_links.append(link)
            news_scores.append(score)
        except IndexError:   #some dont have scores
            news_scores.append(0)

    news_tablet = []
    for i in range(len(news_titles)):
        text = f" *{news_titles[i]}*\n{news_links[i]}\n{news_scores[i]}\n"
        news_tablet.append([text])
        write_to_text(text)
    print('hacking news loaded')
    return news_tablet