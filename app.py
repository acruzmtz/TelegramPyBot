from bs4 import BeautifulSoup  #del módulo bs4, necesitamos BeautifulSoup
import requests
import schedule


def send_btc_price(message):
    """ create the message structure to send the btc price to the telegram """

    bot_token = '1771876298:AAE3Rorty_4HcQQGdYCVIrAuPeA6qmrp2sU'
    chat_id = '865636056'
    sendText = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + chat_id + '&parse_mode=Markdown&text=' + message

    response = requests.get(sendText)

    return response


def btc_scraping():
    """ this function gets the actual btc price from the url and returns the price """

    url_btc_web = requests.get('https://awebanalysis.com/es/coin-details/bitcoin/')
    soup = BeautifulSoup(url_btc_web.content, 'html.parser')

    # we need the class html
    result = soup.find('td', {'class': 'wbreak_word align-middle coin_price'})
    btc_price = result.text

    return btc_price
