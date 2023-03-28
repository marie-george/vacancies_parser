import json
import os
from datetime import datetime


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
