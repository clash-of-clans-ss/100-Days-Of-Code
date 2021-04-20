import requests
from tkinter import *


def get_quote():
    response = requests.get(url="https://api.kanye.rest")
    response.raise_for_status()
    data = response.json()
    quote = data["quote"]
    if len(quote) > 70:
        canvas.itemconfig(quote_text, text=quote, font=("Arial", 20, "bold"))
    elif len(quote) > 150:
        canvas.itemconfig(quote_text, text=quote, font=("Arial", 10, "bold"))
    else:
        canvas.itemconfig(quote_text, text=quote)


window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=("Arial", 30, "bold"),
                                fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, relief=FLAT, command=get_quote)
kanye_button.grid(row=1, column=0)

label = Label(text="Click the Face Image\nto Generate Quotes", font=("Courier", 10, "italic"))
label.grid(row=2, column=0)

window.mainloop()
