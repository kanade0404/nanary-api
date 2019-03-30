import requests
import json
import logging

logger = logging.getLogger(__name__)


class OpenBD:
    def __init__(self):
        pass

    def get_json(self, isbn: str) -> dict:
        """
        find a book info by ISBN Code
        :param isbn: ISBN Code
        :return: A found book info if a book info is exist. A Empty Object unless a book info is not found.
        """
        api_data = self.__call_api(isbn)
        if api_data == {}:
            return {}
        if api_data[0] == None:
            return {}
        json_data = {}
        json_data['isbn'] = api_data[0]['summary']['isbn']
        json_data['title'] = api_data[0]['summary']['title']
        json_data['series'] = api_data[0]['summary']['series']
        json_data['publisher'] = api_data[0]['summary']['publisher']
        json_data['pubdate'] = self.modify_datetime(api_data[0]['summary']['pubdate'])
        json_data['cover'] = api_data[0]['summary']['cover']
        json_data['author'] = self.clean_author(api_data[0]['summary']['author'])
        return json_data

    def __call_api(self, isbn: str) -> dict:
        url = 'https://api.openbd.jp/v1/get?isbn=' + isbn
        response = requests.get(url)
        if response.status_code != 200:
            return {}
        return json.loads(response.text)

    def modify_datetime(self, date: str) -> str:
        """
        format a publish date that get by OpenBD API.
        :param date: publish date
        :return: a formated publish date
        """
        return date.replace('c', '')

    def clean_author(self, author: str) -> str:
        """
        fix an author name that get by OpenBD API.
        :param author: an author name
        :return: a fixed author name
        """
        return author.replace('／著', '')
