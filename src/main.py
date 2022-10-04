from tkinter import Button, Label, Tk
from confuse import Configuration

if __name__ == "__main__":
    # Define configruation
    config = Configuration("TestApp", "__init__")

    # GUI app for output
    App = Tk()
    App.geometry("300x300")

    Label(App, text="Hello user").pack()
    Label(App, text="Here are the config values:").pack()

    # Print the config values
    for k, v in config.items():
        Label(App, text=f"{k}: {v}").pack()

    # Refer to config value
    if config['one']['works'].get(bool) is False:
        Label(App, text="It works!").pack()

    Button(App, text="Kill", command=lambda: App.destroy()).pack()

    App.mainloop()