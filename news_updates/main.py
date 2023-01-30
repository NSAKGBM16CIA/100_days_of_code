import jwnews
import hackernews
import stocks_news
import crypto_news
import world_news
import dev_news
import requests
import os
from dotenv import load_dotenv
import time
from datetime import datetime as dt


load_dotenv()

WHATSAPP_ENDPOINT = os.environ.get('WHATSAPP_ENDPOINT')
WHATSAPP_NUMBER = os.environ.get('WHATSAPP_NUMBER')
API_KEY = os.getenv('API_KEY')


def send_alert(text):
    # data = {"phone": WHATSAPP_NUMBER ,
    #         "text": "test",
    #         "apikey": API_KEY
    #         }

    send_alert = requests.post(f"{WHATSAPP_ENDPOINT}phone={WHATSAPP_NUMBER}&text={text}&apikey={API_KEY}")
    send_alert.raise_for_status()
    # print('Sent successful')

def get_news():
    current_time = dt.now()
    greeting = f'Hie Gardener\n Getting news at {current_time}'
    # requests.post(f"{WHATSAPP_ENDPOINT}&phone={WHATSAPP_NUMBER}&text='{greeting}'&apikey={API_KEY}")

    # getting the news and send
    for news in jwnews.get_latest_news():
        send_alert(news)
        time.sleep(3)
    #     print(news)
    # for news in hackernews.get_news_list():
    #     send_alert(news)
    #     time.sleep(3)
    # for news in stocks_news.get_stocknews():
    #     send_alert(news)
    #     time.sleep(3)
    # for news in crypto_news.get_crypto_news():
    #     send_alert(news)
    #     time.sleep(3)
    # for news in world_news.get_world_news():
    #     send_alert(news)
    #     time.sleep(3)
    # for news in dev_news.get_dev_news():
    #     send_alert(news)
    #     time.sleep(3)



# run the engine
get_news()
