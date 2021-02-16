from PIL import Image, ImageDraw, ImageFont
import csv
import os
import requests
import shutil


def create_boll(string):
    if "да" in string:
        string = True
    elif "нет" in string:
        string = False
    return string

proc = int(input("Введите размер от искомого:"))
name_output_catalog = str(input("Введите имя каталога:"))

if_descr = str(input("Размеры печатать? Да/Нет:")).lower()
create_boll(if_descr)
descr_resize = 0
if_descr_resize = str(input("Размеры изменять? Да/Нет:")).lower()
create_boll(if_descr_resize)
if if_descr_resize:
    descr_resize = int(input("Введите число изменения размеров:"))

if_create_logo = str(input("Печатать логотип? Да/Нет:")).lower()
create_boll(if_create_logo)


def get_file(url):
    r = requests.get(url, stream=True)
    return r

# def resize(open_file_obj, proc):
#     height, width = open_file_obj.size
#     size = height / 100 * proc, width / 100 * proc
#     open_file_obj.thumbnail(size)


def save_image(name, file_object):
    with open(name, 'wb') as fo:
        for chunk in file_object.iter_content(8192):
            fo.write(chunk)

            
def main():
    list_png = []
    path_o = os.getcwd()
    file_csv = path_o + '/' + 'for_pdf.csv'
    if not os.path.exists('folder'):
        os.makedirs('folder')
    path = os.path.abspath('folder')

    with open(file_csv, encoding='utf-8') as f:
        fieldnames = ['Tilda UID', 'Brand', 'SKU', 'Mark', 'Category', 'Title', 'Description', 'Text', 'Photo',
                      'Price', 'Quantity', 'Price Old', 'Editions', 'Modifications',  'External ID', 'Parent UID',
                      'Characteristics:Состав', 'Weight', 'Length', 'Width', 'Height']
        reader = csv.DictReader(f, delimiter=";", fieldnames=fieldnames)
        sale = 0
        new = 0
        count = 0
        character = ''
        descr = ''
        for row in reader:
            count += 1
            if 'Размеры' in row['Description']:
                sale = 0
                new = 0
                character = ''
                descr = row['Description']
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
                    if 'ткань' in row['SKU']:
                        save_image(path + '/' + str(count) + '.jpg', get_file(row['Photo']))
                        im = Image.open(path + '/' + str(count) + '.jpg')
                        im.save(path + '/' + str(count) + '1.jpg')
                        list_png.append(path + '/' + str(count) + '1.jpg')
                        continue
                    else:
                        save_image(path + '/' + str(count) + '.jpg', get_file(row['Photo']))
                        im = Image.open(path + '/' + str(count) + '.jpg')
                        draw_text = ImageDraw.Draw(im)
                        font = ImageFont.truetype('Roboto-Light.ttf', size=30)

                        if (sale or new) and if_create_logo:
                            if sale:
                                draw_text.ellipse((25, 25, 130, 130), fill="red", outline="red")
                                draw_text.text((42, 62), 'SALE', font=font, fill='white')

                            elif new:
                                draw_text.ellipse((25, 25, 130, 130), fill="green", outline="green")
                                draw_text.text((45, 62), 'NEW', font=font, fill='white')



                        font = ImageFont.truetype('Roboto-Light.ttf', size=24)
                        draw_text.text(
                            (700, 25),
                            'В наличии',
                            font=font,
                            fill='#2a9926')
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
                                descr = f"{descr1[0]} {int(descr2[0]) + descr_resize}-{int(descr2[1]) + descr_resize}"
                                draw_text.text(
                                    (700, 90),
                                    (descr),
                                    font=font,
                                    fill='#1C0606')
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
                        list_png.append(path + '/' + str(count) + '1.jpg')
        pdf1_filename = path_o + '/' + f"{name_output_catalog}.pdf"
        im_list_obj = []
        for i in list_png:
            im_list_obj.append(Image.open(i))
        imk = im_list_obj.pop(0)
        imk.save(pdf1_filename, "PDF", quality=proc, save_all=True, append_images=im_list_obj)

        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'folder')
        shutil.rmtree(path)


if __name__ == '__main__':
    main()