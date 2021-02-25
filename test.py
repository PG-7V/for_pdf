from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox, Spinbox
from tkinter.filedialog import askdirectory
from PIL import Image, ImageDraw, ImageFont, ImageEnhance
import csv
import os
import requests
import shutil

# def on_closing():
#     if messagebox.askokcancel("Quit", "PDF is create."):
#         window.destroy()
#         exit()
#
# def cli():
#     print(22222)
#     on_closing()
#
# window = Tk()
# window.title("Create PDF")
# window.geometry('400x600')
#
# btn = Button(window, text="Запустить", command=cli)
# btn.grid(column=1, row=3, padx=10, pady=10)
#
#
# window.mainloop()
text = "рпп т  о о о о о оо о о о о о о . о р р, т рр  \ т п пм п п п "

im = Image.open('test_img.jpg')

draw_text = ImageDraw.Draw(im)
print(len(text))

draw_text.text((int(700 - len(text)*8.5), 25), f'{text}',
               font=ImageFont.truetype('Roboto-Light.ttf', size=28), fill='black')

draw_text.text((650, 70), f'{text}',
               font=ImageFont.truetype('Roboto-Light.ttf', size=28), fill='black')

im.show()