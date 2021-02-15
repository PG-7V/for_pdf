from PIL import Image, ImageDraw, ImageFont
import csv
import os
import requests
import shutil


def get_file(url):
    r = requests.get(url, stream=True)
    return r


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
                        im.save(path + '/' + str(count) + '.png')
                        list_png.append(path + '/' + str(count) + '.png')
                        continue
                    else:
                        save_image(path + '/' + str(count) + '.jpg', get_file(row['Photo']))
                        im = Image.open(path + '/' + str(count) + '.jpg')

                        if sale or new:
                            if sale:
                                logo = 'sale.png'
                            elif new:
                                logo = 'new.png'
                            watermark = Image.open(logo)
                            im.paste(watermark, (25, 25), watermark)

                        font = ImageFont.truetype('Roboto-Light.ttf', size=24)
                        draw_text = ImageDraw.Draw(im)
                        draw_text.text(
                            (700, 25),
                            'В наличии',
                            font=font,
                            fill='#2a9926')
                        if 'Артикул' in row['Title']:
                            art = ('Артикул' + row['SKU'])
                        else:
                            art = (row['SKU'])

                        draw_text.text(
                            (700, 60),
                            (art),
                            font=font,
                            fill='#1C0606')
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
                        im.save(path + '/' + str(count) + '.png')
                        list_png.append(path + '/' + str(count) + '.png')
        pdf1_filename = path_o + '/' + "catalog3.pdf"
        im_list_obj = []
        for i in list_png:
            im_list_obj.append(Image.open(i))
        imk = im_list_obj.pop(0)
        imk.save(pdf1_filename, "PDF", resolution=100.0, save_all=True, append_images=im_list_obj)

        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'folder')
        shutil.rmtree(path)


if __name__ == '__main__':
    main()