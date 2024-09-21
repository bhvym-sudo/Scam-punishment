import requests
import threading
url = "https://prestashop-179074-0.cloudclusters.net/5th.php"
data = {
    "atm+pin": "6969",
    "exp+date": "696969",
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
