# GET NEWS FROM TWO API POINTS
import requests
import os
from dotenv import load_dotenv

def write_to_text(text):
    with open("world_news.txt", 'a') as file:
        file.write(text)

def get_world_news():
    load_dotenv()

    API_KEY = os.getenv('NEWS_DATA_API_KEY')
    NEWS_KEY = os.getenv('NEWS_API_KEY')
    NEWSDATA_ENDPOINT = os.getenv('NEWSDATA_ENDPOINT')
    NEWSAPI_ENDPOINT = os.getenv('NEWSAPI_ENDPOINT')

    url = f"{NEWSDATA_ENDPOINT}{API_KEY}&q=harare&language=en"
    url_2 = f'{NEWSAPI_ENDPOINT}{NEWS_KEY}'

    world_news = []

    page = requests.get(url)

    news_list = page.json()['results']

    for news in news_list:
        text = (f"*{news['title']}*\n"
            f"_{news['source_id']} - {news['country']}_\n"
            f"{news['link']}\n")
        world_news.append(text)
        # print(text)
        write_to_text(text)


    page2 = requests.get(url_2)
    news_list = page2.json()['articles']
    print(news_list)
    for news in news_list:
        # print(news)
        text = (f"*{news['title']}*\n"
            f"_{news['source']['name']}_\n"
            f"{news['url']}\n")
        world_news.append(text)
        write_to_text(text)
        # print(text)
    print('world news news loaded')
    return world_news

# get_world_news()