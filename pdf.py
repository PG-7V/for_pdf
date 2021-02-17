# import os
# import PIL.Image
#
# def img2pdf(fname):
#     filename = fname
#     name = filename.split('.')[0]
#     im = PIL.Image.open('1661.jpg')
#     if not os.path.exists('im2pdf_output'):
#         os.makedirs('im2pdf_output')
#     newfilename = ''.join([name, '.pdf'])
#     PIL.Image.Image.save(im, newfilename, "PDF", resolution = 100.0)
#     print("processed successfully: {}".format(newfilename))
#
# #files = [f for f in os.listdir('./') if f.endswith('.jpg')]
# #for fname in files:
# img2pdf('1661.jpg')
#


from PIL import Image, ImageDraw, ImageFont

img = Image.open('1661.jpg')
font = ImageFont.truetype('Roboto-Light.ttf', size=24)
draw_text = ImageDraw.Draw(img)
draw_text.text(
    (700, 90),
    'В наличии',
    # Добавляем шрифт к изображению
    font=font,
    fill='#2a9926')
draw_text.text(
    (700, 120),
    'В наличии 2',
    # Добавляем шрифт к изображению
    font=font,
    fill='#2a9926')

img.show()
