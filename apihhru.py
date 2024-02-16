import requests
import pprint
domain = 'https://api.hh.ru/'

url_vacan = f'{domain}vacancies'

params = {
    'text:' 'NAME:(Python or Java) AND COMPANY_NAME:(1 or 2 OR Yandex) AND (Django OR Spring)'
    'page': 1
}

result = requests.get(url_vacancy, params = params).json()
pprint.pprint(result)