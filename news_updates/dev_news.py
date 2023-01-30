from bs4 import BeautifulSoup
import requests

def get_dev_news():
    url = 'https://bloggingfordevs.com/trends/'
    page = requests.get(url)

    soup = BeautifulSoup(page.text, 'html.parser')
    # print(soup)
    headlines = soup.select(".css-1ezvrbm")

    dev_news = []

    if len(headlines) != 0:
        for news in headlines:
            dev_news.append(f"*{news.text}*\n{news.get('href')}")
            # print(news.text)
            # print(news.get('href'))
    return dev_news