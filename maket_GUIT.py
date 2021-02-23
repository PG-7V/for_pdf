from PIL import Image, ImageDraw, ImageFont
import csv
import os
import requests
import shutil


def create_bool(a, b, string):
    if a in string:
        string = True
    elif b in string:
        string = False
    return string


def get_file(url):
    r = requests.get(url, stream=True)
    return r


def save_image(name, file_object):
    with open(name, 'wb') as fo:
        for chunk in file_object.iter_content(8192):
            fo.write(chunk)


def main(data):
    collection = ""
    proc = data['proc']
    name_output_catalog = 'catalog111'
    if_quantity = create_bool("Только в наличии", 'Все', data['quantity'])
    if_material = create_bool('С тканью', 'Скрыть', data['if_material'])
    if data['season'] == 'Все платья':
        if_collection = False
    else:
        if_collection = True
    if if_collection:
        collection = data['season']
    if_characteristics = create_bool('Отобразить', 'Скрыть', data['if_characteristics'])
    if_descr = if_descr_resize = True
    descr_resize = data['descr_resize']
    if_price_resize = data['if_price_resize']
    price_resize = data['price_resize']
    if_price = create_bool('Отобразить', 'Без цены', data['view_price'])
    if 'Нет' in data['valute']:
        valute = ''
    else:
        valute = data['valute']

    if_create_logo = create_bool('Отобразить', 'Не отображать', data['if_create_logo'])

    list_png = []
    path_o = data['filename']
    font_path = path_o + '/' + 'Roboto-Light.ttf'
    file_csv = path_o + '/' + 'for_pdf.csv'
    try:
        shutil.rmtree(os.path.abspath('folder'))
    except:
        pass
    if not os.path.exists('folder'):
        os.makedirs('folder')
    path = os.path.abspath('folder')
    path_folder = path

    with open(file_csv, encoding='utf-8') as f:
        fieldnames = ['Tilda UID', 'Brand', 'SKU', 'Mark', 'Category', 'Title', 'Description', 'Text', 'Photo',
                      'Price', 'Quantity', 'Price Old', 'Editions', 'Modifications', 'External ID', 'Parent UID',
                      'Characteristics:Состав', 'Weight', 'Length', 'Width', 'Height']
        reader = csv.DictReader(f, delimiter=";", fieldnames=fieldnames)
        sale = 0
        new = 0
        category = 0
        count = 0
        character = ''
        descr = ''
        for row in reader:
            count += 1
            if 'Размеры' in row['Description']:
                sale = 0
                new = 0
                category = 0
                character = ''
                descr = row['Description']
                if row["Category"].strip() in collection:
                    category = 1
                if 'Sale' in row['Mark']:
                    sale = 1
                elif 'New' in row['Mark']:
                    new = 1
                if row['Characteristics:Состав']:
                    character = row['Characteristics:Состав']
                    if ', ' in character:
                        character = character.replace(', ', '\n')
                continue

            if not row['Description']:

                if row['SKU']:
                    if 'т' in row['SKU']:
                        save_image(path + '/' + str(count) + '.jpg', get_file(row['Photo']))
                        im = Image.open(path + '/' + str(count) + '.jpg')
                        im.save(path + '/' + str(count) + '1.jpg')
                        if if_material:
                            if if_collection:
                                if category:
                                    if if_quantity:
                                        if quantity:
                                            list_png.append(path + '/' + str(count) + '1.jpg')
                                    else:
                                        list_png.append(path + '/' + str(count) + '1.jpg')
                            else:
                                if if_quantity:
                                    if quantity:
                                        list_png.append(path + '/' + str(count) + '1.jpg')

                                else:
                                    list_png.append(path + '/' + str(count) + '1.jpg')
                        continue
                    else:
                        quantity = 0
                        if row['Price']:
                            price = float(round((float(row['Price'])), 2))
                        if row["Quantity"]:
                            quantity = int(row["Quantity"])
                        save_image(path + '/' + str(count) + '.jpg', get_file(row['Photo']))
                        im = Image.open(path + '/' + str(count) + '.jpg')
                        draw_text = ImageDraw.Draw(im)
                        font = ImageFont.truetype(font_path, size=30)

                        if (sale or new) and if_create_logo:
                            if sale:
                                draw_text.ellipse((25, 25, 130, 130), fill="red", outline="red")
                                draw_text.text((42, 62), 'SALE', font=font, fill='white')

                            elif new:
                                draw_text.ellipse((25, 25, 130, 130), fill="green", outline="green")
                                draw_text.text((45, 62), 'NEW', font=font, fill='white')

                        font = ImageFont.truetype(font_path, size=24)
                        if quantity:
                            draw_text.text(
                                (700, 25),
                                'В наличии',
                                font=font,
                                fill='#2a9926')
                            # quantity = 0
                        if 'Артикул' in row['Title']:
                            art = ('Артикул: ' + row['SKU'])
                        else:
                            art = (row['SKU'])
                        draw_text.text(
                            (700, 60),
                            (art),
                            font=font,
                            fill='#1C0606')
                        if if_descr:
                            if if_descr_resize:
                                descr1 = descr.split(" ")
                                descr2 = descr1[1].split("-")
                                descr = f"{descr1[0]} {int(descr2[0]) + int(descr_resize)}-{int(descr2[1]) + int(descr_resize)}"
                            draw_text.text(
                                (700, 90),
                                (descr),
                                font=font,
                                fill='#1C0606')
                            if if_price:
                                if valute:
                                    price = str((round((price + if_price_resize) * price_resize), 2)) + " " + valute
                                    if '(' in price:
                                        price = price.replace('(', '')
                                        price = price.replace(')', '')
                                elif not valute:
                                    price = str((round((price + if_price_resize) * price_resize), 2))
                                    if '(' in price:
                                        price = price.replace('(', '')
                                        price = price.replace(')', '')
                                draw_text.text(
                                    (700, 120),
                                    (price),
                                    font=font,
                                    fill='#1C0606')
                        elif if_price:
                            if valute:
                                price = str((round((price + if_price_resize) * price_resize), 2)) + " " + valute
                                if '(' in price:
                                    price = price.replace('(', '')
                                    price = price.replace(')', '')
                            elif not valute:
                                price = str((round((price + if_price_resize) * price_resize), 2))
                                if '(' in price:
                                    price = price.replace('(', '')
                                    price = price.replace(')', '')
                            draw_text.text(
                                (700, 90),
                                (price),
                                font=font,
                                fill='#1C0606')
                        if if_characteristics:
                            draw_text.text(
                                (700, 900),
                                'Состав:',
                                font=font,
                                fill='#2a9926')
                            draw_text.text(
                                (700, 925),
                                (character),
                                font=font,
                                fill='#1C0606')
                        im.save(path + '/' + str(count) + '1.jpg')
                        if if_collection:
                            if category:
                                if if_quantity:
                                    if quantity:
                                        list_png.append(path + '/' + str(count) + '1.jpg')
                                else:
                                    list_png.append(path + '/' + str(count) + '1.jpg')
                        else:
                            if if_quantity:
                                if quantity:
                                    list_png.append(path + '/' + str(count) + '1.jpg')
                            else:
                                list_png.append(path + '/' + str(count) + '1.jpg')
        pdf1_filename = path_o + '/' + f"{name_output_catalog}.pdf"
        im_list_obj = []
        for i in list_png:
            im_list_obj.append(Image.open(i))
        imk = im_list_obj.pop(0)
        imk.save(pdf1_filename, "PDF", quality=proc, save_all=True, append_images=im_list_obj)
        path_folder = os.path.join(path_folder)
        shutil.rmtree(path_folder)


