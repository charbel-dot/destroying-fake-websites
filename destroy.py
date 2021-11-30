import requests
import threading

def spam():
    url = 'http://aidcash.site/1/'
    data = {
        'Stop': 'creating',
        'fake' : 'websites',
        'that\'s': 'not',
        'good' : 'man!'
        }

    sending_data = requests.post(url, data=data, allow_redirects=False)

    print(f"\nResponse code: {sending_data.status_code}")

threads = []

for _ in range(100):
    t = threading.Thread(target=spam)
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()