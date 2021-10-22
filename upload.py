import random
import requests

print("1: Getting information from a file\n2: Upload a file")
choice = input("Choose option: ")

if choice == "1":

    ID = input("Enter file ID: ")
    random_ua = str(random.choice(list(set(requests.get("https://raw.githubusercontent.com/DavidWittman/requests-random-user-agent/master/requests_random_user_agent/useragents.txt").content.decode().splitlines()))))
    headers = {'User-Agent': random_ua, 'From': 'petersars@gmail.com'}
    response = requests.get(f'https://api.anonfiles.com/v2/file/{ID}/info', headers=headers)
    print(response.json())

elif choice == "2":

    filepath = input("Enter filepath: ")
    response = requests.post('https://api.anonfiles.com/upload', files = {'file': open(filepath,'rb')})
    print("DOWNLOAD LINK: " + response.json()["data"]["file"]["url"]["full"])