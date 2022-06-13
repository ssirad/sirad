rom guizero import App, Text, PushButton
from random import choice

app = App("TOP SECRET")
title = Text(app, "Push the red button to find out your spy name")

nomi = ["leone", "Aristotele", "Dariole", "Helen", "Jiji", "Billy"]
cognomi = ["Piraccini", "Pirazzini", "azzolini", "misterioso", "Scuali", "Rossi", "Bianchi"]

nome_spia = choice(nomi) + " " + choice(cognomi)
#name.value = nome_spia

def choose_name():
    print(nome_spia)

bottone = PushButton(app, choose_name, text="Tell me!")
app.display()

name = Text(app, text="")

app.display()
