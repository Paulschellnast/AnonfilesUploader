import PySimpleGUI as sg
import requests


layout = [  [sg.Text('Path to file'), sg.FileBrowse()],
            [sg.Button('Upload!'), sg.Button('Cancel')] ]


window = sg.Window('Anonfiles Uploader', layout, size=(290, 90))

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': 
        break
    response = requests.post('https://api.anonfiles.com/upload', files = {'file': open(values["Browse"],'rb')})
    
    sg.Print("DOWNLOAD LINK: " + response.json()["data"]["file"]["url"]["full"])

window.close()