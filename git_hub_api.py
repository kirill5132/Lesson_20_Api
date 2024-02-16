import pprint

import requests

url = ''
token = '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'
result = requests.get(url, auth=('kirill5132', token))

headers = {
    'Autorization': f'tokenP{token}'

}

result = requests.get(url, headers = headers)

session = requests.session()
session.auth = ('Yusiloid', token)
result = session.get(url)

url = 'https://api.github.com/searh/repositories?q=tetris+language:assembly&sort=stars&order=desc'
result = session.get(url)
pprint.pprint(result.json())