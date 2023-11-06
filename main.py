import tkinter as tk
from io import BytesIO

import requests as requests
from PIL import ImageTk, Image

root = tk.Tk()
root.geometry("300x400")
root.title("Funny Cats!")

tk.Label(text="Funny cats :3").pack()


def createNewImage():
    imageWindow = tk.Toplevel()
    imageWindow.title("New cat image hshshsshs")
    img_url = "https://cataas.com/cat"
    response = requests.get(img_url, headers={"User-Agent": "Mozilla/5.0"})
    image_data = response.content
    photo = Image.open(BytesIO(image_data))
    tk_photo = ImageTk.PhotoImage(photo)
    newImage = tk.Label(imageWindow, image=tk_photo)
    newImage.image = tk_photo
    newImage.pack()
    imageWindow.mainloop()


btn = tk.Button(text="Generuj nowy obrazek :)", command=lambda: createNewImage())
btn.pack()

tk.mainloop()
