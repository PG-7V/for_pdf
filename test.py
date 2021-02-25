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
text = "Объединяет любое количествострок, строка, метод которой вызывается,"

im = Image.open('test_img.jpg')

draw_text = ImageDraw.Draw(im)
print(len(text))

draw_text.text((30, 30), 'Бренд: Орхидея',
               font=ImageFont.truetype('Roboto-Light.ttf', size=28), fill='black')
draw_text.ellipse((40, 80, 90, 130), fill="red")
draw_text.text((50, 93), 'sale', font=ImageFont.truetype('Roboto-Light.ttf', size=18), fill='white')
#draw_text.text((int(700 - len(text)*8.5), 25), f'{text}',
               #font=ImageFont.truetype('Roboto-Light.ttf', size=28), fill='black')

draw_text.text((680, 30), 'В наличии',
               font=ImageFont.truetype('Roboto-Light.ttf', size=28), fill='black')
draw_text.text((680, 65), 'Артикул: 1661',
               font=ImageFont.truetype('Roboto-Light.ttf', size=28), fill='black')
draw_text.text((680, 100), 'Размеры: 46-52',
               font=ImageFont.truetype('Roboto-Light.ttf', size=28), fill='black')
draw_text.text((680, 135), 'Цена: 24.5 BYN',
               font=ImageFont.truetype('Roboto-Light.ttf', size=28), fill='black')
draw_text.text((680, 905), 'Состав: ',
               font=ImageFont.truetype('Roboto-Light.ttf', size=28), fill='black')

draw_text.text((680, 940), 'Хлопок 100 %',
               font=ImageFont.truetype('Roboto-Light.ttf', size=28), fill='black')

iter = len(text)//26
if iter > 0:
    text = list(text)
    for i in range(1, iter+1):
        text.insert((i*26)+i, '\n')
    text = ''.join(text)



draw_text.text((550, 1050), f'{text}', font=ImageFont.truetype('Roboto-Light.ttf', size=24), fill='black')

im.show()