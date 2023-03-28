import json


class Vacancy:
    """Организация информации, полученной из вакансии в удобный выыод для пользователя"""
    __slots__ = ('name', 'company_name', 'url', 'description', 'remote_work', 'salary')

    def __init__(self, name, company_name, url, description, remote_work, salary, *args):
        self.name = name
        self.company_name = company_name
        self.url = url
        self.description = description[:200]
        self.remote_work = remote_work
        self.salary = salary
        super().__init__(*args)

    def __repr__(self):
        return f'Наименование вакансии: {self.name}\nРаботодатель: {self.company_name}\nСсылка на вакансию:' \
               f' {self.url}\nОписание вакансии: {self.description}\nМесто работы: {self.remote_work}\nЗарплата:' \
               f' {self.salary}\n'

    def __gt__(self, other):
        return self.salary > other.salary


