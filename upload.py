import requests
import pyfiglet
ascii_banner = pyfiglet.figlet_format("ANONFILES UPLOADER")
print(ascii_banner)
print("1: Getting information from a file")
print("2: Upload a file")
y = input("Choose option: ")
if y == "2":
    filepath = input("Enter filepath:")
    print("filepath is: " + filepath)
    x = requests.post(url, files = {'file': open(filepath,'rb')},)
    print("DOWNLOAD LINK: " + x.json()["data"]["file"]["url"]["full"])
if y == "1":
    fileinfo = input("Enter file ID: ")
    print('https://api.anonfiles.com/v2/file/'+fileinfo+'/info')
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Brave Chrome/91.0.4472.124 Safari/537.36',
    'From': 'petersars@gmail.com'  
    }
    z = requests.get('https://api.anonfiles.com/v2/file/'+fileinfo+'/info', headers=headers)
    print(z.json())