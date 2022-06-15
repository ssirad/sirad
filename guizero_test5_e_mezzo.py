from guizero import App, PushButton

app = App(title="pop-ups")

app.info("Applicacion started", "Well done you started an application")
def are_you_sure():
    if app.yesno("Confermation", "Are you sure?"):
        app.info("Thanks", "Button Pressed")

    else:
        app.error("Ok", "Cancelling")

button = PushButton(app, command=are_you_sure)

app.display()
