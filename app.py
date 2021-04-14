from bs4 import BeautifulSoup  #del módulo bs4, necesitamos BeautifulSoup
import requests
import schedule


def send_btc_price(message):
    bot_token = '1771876298:AAE3Rorty_4HcQQGdYCVIrAuPeA6qmrp2sU'
    chat_id = '865636056'
    sendText = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + chat_id + '&parse_mode=Markdown&text=' + message

    response = requests.get(sendText)

    return response

test = send_btc_price('Hola, ya estoy para ti')
