import json
import os
from datetime import datetime


class JSONDegaradationException(Exception):
    """Класс обработки ошибки в случае деградации файла"""

    def __init__(self, *args):
        self.message = args[0] if args else 'Файл потерял актуальность в структуре данных'

    def __str__(self):
        return self.message


class Connector:
    """Класс коннектор к файлу в json формате"""

    __data_file = None

    def __init__(self, filename):
        self.data_file = filename

    @property
    def data_file(self):
        return self.__data_file

    @data_file.setter
    def data_file(self, value):
        self.__data_file = value
        self.__connect()

    def __connect(self):
        """Проверка на существование файла с данными и создание его при необходимости. Проверка на деградацию"""
        with open(self.__data_file, 'a+', encoding='utf8') as f:
            f.seek(0)
            first_line = f.readline()
            if first_line:
                try:
                    f.seek(0)
                    data = json.load(f)
                    assert type(data) == list
                    for item in data:
                        assert type(item["name"]) == str
                        assert type(item["company_name"]) == str
                        assert type(item["url"]) == str
                        assert type(item["description"]) == str
                        assert type(item["remote_work"]) == str
                        assert type(item["salary"]) == int
                except:
                    raise JSONDegaradationException()
            else:
                json.dump([], f)
        #Проверка на актуальность файл по времени
        if (datetime.now() - datetime.fromtimestamp(os.path.getmtime(self.__data_file))).days >= 1:
            raise JSONDegaradationException()