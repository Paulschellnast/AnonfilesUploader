import requests
url = 'https://api.anonfiles.com/upload'
filepath = input("Enter filepath:")
print("filepath is: " + filepath)
x = requests.post(url, files = {'file': open(filepath,'rb')},)
print("DOWNLOAD LINK: " + x.json()["data"]["file"]["url"]["full"])