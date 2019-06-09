import requests
import json
import logging

logger = logging.getLogger(__name__)


class OpenBD:
    def __init__(self):
        pass

    def get_json(self, isbn: str) -> dict:
        """
        ISBNコードから書籍情報を取得
        :param isbn: ISBN Code
        :return: A found book info if a book info is exist. A Empty Object unless a book info is not found.
        """
        api_data = self.__call_api(isbn)
        if api_data == {}:
            return {}
        if api_data[0] == None:
            return {}
        json_data = dict()
        json_data['isbn'] = api_data[0]['summary']['isbn']
        json_data['title'] = api_data[0]['summary']['title']
        json_data['series'] = api_data[0]['summary']['series']
        json_data['publisher'] = api_data[0]['summary']['publisher']
        json_data['pubdate'] = api_data[0]['summary']['pubdate']
        json_data['cover'] = api_data[0]['summary']['cover']
        json_data['author'] = api_data[0]['summary']['author']
        return json_data

    def __call_api(self, isbn: str) -> dict:
        """
        OpenBDのAPIを叩いて書籍情報を取得
        :param isbn:
        :return:
        """
        url = 'https://api.openbd.jp/v1/get?isbn=' + isbn
        response = requests.get(url)
        if response.status_code != 200:
            return {}
        return json.loads(response.text)
