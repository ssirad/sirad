import requests
import urllib.parse
from guizero import App, TextBox, PushButton, Combo, Text

app = App("Comandante Sonos")

def send(room, textbox):
    encodedMessage = urllib.parse.quote(textbox.value)
    command = f"http://192.168.69.232:5005/{room.value}/say/{encodedMessage}/it-it"
    x = requests.get(command)
    return x.status_code

room = Combo(app, options=["sirad", "keynan", "soggiorno", "studio"], height=5, width="fill", align="top")
textbox = TextBox(app, multiline=True, height="fill", width=30, align="left", text="Scrivi qui il tuo messaggio :) ")

button = PushButton(app, command=send, text="Clicca qui per far parlare il sonos", args=[room, textbox], align="bottom", width=60, height="fill")

app.display()
