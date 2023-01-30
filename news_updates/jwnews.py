
import requests
import lxml
from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv

load = 0

saved_headlines = []
saved_links = []
jw_news = []
news_titles = []
news_links = []

def get_latest_news():

    check_if_saved()
    global news_titles
    global jw_news
    load_dotenv()

    rss_url = os.getenv('JW_RSS_URL')
    rss_feed = requests.get(rss_url)
    rss_feed.raise_for_status()
    news_feeds = rss_feed.text
    news_soup = BeautifulSoup(news_feeds , 'lxml')

    news_titles = news_soup.find_all('title')[1:]
    items = news_soup.select('item')
    for item in items:
        news_links.append(str(item).split('<link/>')[1].split('\n')[0])

    if len(news_titles) != len(saved_headlines):
        anything_new()
    return (jw_news)

def anything_new():
    # print(load)

    if load == 0:
        load_write_history("0", '0')
    else:
        global news_titles
        for i in range(len(news_titles)):
            title = f'{news_titles[i].text}\n'
            link = f'{news_links[i]}\n'

            if title not in saved_headlines and link not in saved_links:
                # saved_headlines.append(title)
                # saved_links.append(link)
                load_write_history(title, link)
                news_alert = f"*{title}*\n{link}\n"
                # print(news_alert)
                jw_news.append(news_alert)
                # time.sleep(20)
    print('jw news loaded')


def load_write_history(title , link):
    global load
    if load == 0:
        load = 1
        get_latest_news()
    else:
        with open("jwnews.txt", 'a') as file:
            file.write(f"*{title}*\n{link}\n")

def check_if_saved():
    with open("jwnews.txt" , 'r') as file:
        data = file.readlines()

        for l in data:
            if l.startswith('https'):
                saved_links.append(l)
            else:
                saved_headlines.append(l)
        # print(saved_links)
#
# get_latest_news()
# anything_new()
# send_alert ()

