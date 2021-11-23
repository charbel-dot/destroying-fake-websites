import requests

def spam():
    url = ''
    data = {
        'Stop': 'creating',
        'fake' : 'websites',
        'that\'s': 'not',
        'good' : 'man!'
        }

    send = requests.post(url, data=data, allow_redirects=False)

    print(f"Response code: {send.status_code}")