from guizero import App, Text

app = App("Va tutto male", bg = "black")
title = Text(app, text="Un testo difficile da leggere", size="14", font="Comic Sans", color="white")

def flash_testo():
    if title.visible:
        title.hide()
    else:title.show()

app.repeat(1000, flash_testo)

app.display()
