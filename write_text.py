from PIL import Image, ImageDraw, ImageFont
import csv
import os

# Загрузить фото
# Нанести лого
# Внести запись
# сложить фото в pdf

# в текущей дирректории создать каталог for_pdf.csv

im = Image.open('1661.jpg')
# Изображение для водяного знака
img = ''



watermark = Image.open('sale.png')
im.paste(watermark, (25, 25), watermark)

# Создаем объект со шрифтом
font = ImageFont.truetype('Roboto-Light.ttf', size=24)
draw_text = ImageDraw.Draw(im)
draw_text.text(
    (700, 25),
    'В наличии',
    # Добавляем шрифт к изображению
    font=font,
    fill='#2a9926')
draw_text.text(
    (700, 60),
    'Артикул: 1661',
    # Добавляем шрифт к изображению
    font=font,
    fill='#1C0606')
draw_text.text(
    (700, 90),
    'Размеры: 48-56',
    # Добавляем шрифт к изображению
    font=font,
    fill='#1C0606')
draw_text.text(
    (700, 900),
    'Состав:',
    # Добавляем шрифт к изображению
    font=font,
    fill='#2a9926')
draw_text.text(
    (700, 925),
    'Хлопок: 60%\nПолиэстер: 40%',
    # Добавляем шрифт к изображению
    font=font,
    fill='#1C0606')





im.save('123.jpg')