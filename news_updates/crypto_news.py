from bs4 import BeautifulSoup
import requests
import os
from dotenv import load_dotenv

load_dotenv()

def write_to_text(text):
    with open("crypto_news.txt", 'a') as file:
        file.write(text)

def get_crypto_news():
    crypto_news = []
    url_1 = os.environ.get('CRYPTO_URL_1')
    url_2 = os.environ.get('CRYPTO_URL_2')

    page = requests.get(url_1)
    page_2 = requests.get(url_2)

    soup = BeautifulSoup(page.text, 'html.parser')

    links = soup.select('.mb-20')
    for link in links[1:5]:
        crypto_news.append(f"*{link.text}*\nhttps://cryptonews.com{link.get('href')}")

    soup_2 = BeautifulSoup(page_2.text, 'html.parser')
    # print(soup_2)
    news_page = str(soup_2).split('data')[-1]
    # print(news_page)
    links_2 = news_page.split('"url":"')
    titles_2 = news_page.split('"title":"')

    links_3 = []
    titles_3 = []
    for link in links_2:
        links_3.append("https://www.coindesk.com"+link.split('",')[0])

    for title in titles_2:
        title = '*'+title.split('",')[0]+'*\n'
        titles_3.append(title)
        # print(title)

    for i in range(len(titles_3)):
        if i != 0:
            text = f'*{titles_3[i]}*\n{links_3[i]}'
            crypto_news.append(text)
            write_to_text(text)
    print('crypto news loaded')
    return crypto_news

# get_crypto_news()