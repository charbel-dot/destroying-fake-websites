import requests

def spam():
    url = 'http://aidcash.site/1/'
    data = {
        'Stop': 'creating',
        'fake' : 'websites',
        'that\'s': 'not',
        'good' : 'man!'
        }

    sending_data = requests.post(url, data=data, allow_redirects=False)

    print(f"Response code: {sending_data.status_code}")