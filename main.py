import requests
import os
from urllib.parse import urlparse
import argparse 
from dotenv import load_dotenv


def is_bitlink(auth, bitlink):
    check_url = f'https://api-ssl.bitly.com/v4/bitlinks/{bitlink}'
    response = requests.get(check_url, headers=auth)
    return response.ok

        
def get_shorten_link(auth, link):
    short_url = 'https://api-ssl.bitly.com/v4/shorten'
    payload = {'long_url' : link}
    response = requests.post(short_url, json=payload, headers=auth)
    response.raise_for_status()
    bitlink = response.json()["id"]
    return bitlink


def count_clicks(auth, bitlink):
    sum_url = f'https://api-ssl.bitly.com/v4/bitlinks/{bitlink}/clicks/summary'
    payload = {'unit' : 'month', 'units' : '-1'}
    response = requests.get(sum_url, params=payload, headers=auth)
    response.raise_for_status()
    clicks = response.json()['total_clicks']
    return clicks


def main():
    load_dotenv()
    parser = argparse.ArgumentParser(description='Сокращение ссылки и подсчет кликов по ней')
    parser.add_argument('--url', type=str, help='Введите ссылку')
    user_input = parser.parse_args()
    parsed_url = urlparse(user_input.url)
    parsed_url = f"{parsed_url.netloc}{parsed_url.path}"
    bitly_token = os.environ['BITLY_TOKEN']
    authorization = {'Authorization': bitly_token}
    try:
        if is_bitlink(authorization, parsed_url):
            print(count_clicks(authorization, parsed_url))
        else:
            print(get_shorten_link(authorization, user_input.url))
    except requests.exceptions.HTTPError as error:
        print("Неверная ссылка", error)


if __name__ == '__main__':
    main()







































