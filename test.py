from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox, Spinbox
from tkinter.filedialog import askdirectory
from PIL import Image, ImageDraw, ImageFont, ImageEnhance
import csv
import os
import requests
import shutil


# url = 'https://static.tildacdn.com/tild6466-6462-4530-a137-343933333736/1661_0.jpg'
#
# r = requests.get(url, stream=True)
# with open('test_img.jpg', 'wb') as fo:
#     for chunk in r.iter_content(8192):
#         fo.write(chunk)

# img = Image.open('test_img.jpg')
# # img.save('save_test_img.jpg', quality=99)
# # draw_text = ImageDraw.Draw(img)
# # font = ImageFont.truetype('Roboto-Light.ttf', size=18)
# #
# # # draw_text.ellipse()
# # draw_text.ellipse((40, 70, 90, 120), fill="red", outline="red")
# # draw_text.text((50, 84), 'sale', font=font, fill='white')
# # draw_text.text((25, 25), 'Под заказ', font=ImageFont.truetype('Roboto-Light.ttf', size=24), fill='red')
# img.save('save_test_img2.jpg', quality=100)
# # contrast = ImageEnhance.Contrast(img)
# # contrast.enhance(1.2).show()
#
# img.show()

price = 25.0
if_price_resize = 2.22
price_resize = 3.333

price = str(round(((price + if_price_resize) * price_resize), 2))
# price = price + if_price_resize
# price = price * price_resize
# price = round(price, 2)
# price = str(price)

print(price)