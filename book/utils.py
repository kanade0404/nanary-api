class BookUtil:

    def pubdate_to_integer(self, pubdate: str) -> int:
        """
        出版年月を整数4桁に修正します
        :param pubdate:
        :return:
        """
        return int(pubdate.replace('-', ''))
