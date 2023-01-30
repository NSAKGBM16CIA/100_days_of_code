import time

import requests
from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv
from datetime import datetime as dt

def write_to_text(text):
    with open("stocks_news.txt", 'a') as file:
        file.write(text)

def get_stocknews():
    load_dotenv()

    news_endpoint = os.environ.get('STOCK_NEWS_ENDPOINT')

    NEWS_APIKEY = os.getenv('NEWS_API_KEY')
    companies_url = os.getenv('COMPANY_URL')
    page = requests.get(companies_url)

    soup = BeautifulSoup(page.text, 'html.parser')

    stock_news = []
    companies = []
    symbols = []
    stocks = []

    soup_text = str(soup)
    # print(soup_text)

    symbol_list = soup_text.split('class="ticker-area">')[:20]
    i = 0
    for text in symbol_list:
        s = text.split('<')[0]
        symbols.append(s)
        # print(s)
        if i == 20:
            break
        i += 1

    company_list = soup_text.split('class="title-area">')[:25]
    i = 0
    for text in company_list:
        c = text.split('</div>')[0]
        companies.append(c)
        # print(c)
        if i == 20:
            break
        i += 1


    stock_list = soup_text.split('td><td data-clean="')[1:20]
    i = 0
    for text in stock_list:
        value = text.split('"')[0]
        stocks.append(value)
        # print(value)
        if i == 20:
            break
        i += 1


    for i in range(len(stocks))[1:]:

        # GET RELATED NEWS
        d = dt.now().date()
        date = f'{d.year}-{d.month}-{d.day-1}'

        news_url = f'{news_endpoint}{symbols[i]}&from={date}&sortBy=publishedAt&apiKey={NEWS_APIKEY}'
        # print(news_url)

        page = requests.get(url=news_url)
        time.sleep(3)

        latest_news = []


        try:
            news_list = (page.json()['articles'])

            for news in news_list[:2]:
                latest_news.append(
                    f"\n*{news['title']}*\n"
                    f"_{news['source']['name']}_\n"
                    f"{news['url']}\n"
                    f"-------"
                    f"{news['content']}"
                )
            standing = f'{symbols[i]} | {companies[i]} | {stocks[i]}{latest_news[0]}{latest_news[1]}\n'
            stock_news.append(standing)
            write_to_text(standing)
        except Exception:
            standing = f'{symbols[i]} | {companies[i]} | {stocks[i]}\n'
            stock_news.append(standing)
            write_to_text(standing)
    print('stock news loaded')
    return stock_news

# get_stocknews()