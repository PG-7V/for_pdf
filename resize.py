from PIL import Image, ImageDraw, ImageFont

# x = int(input("Введите размер от искомого:"))

img1 = Image.open('1661.jpg')

# draw = ImageDraw.Draw(img1)
# font = ImageFont.truetype('Roboto-Light.ttf', size=30)
# draw.ellipse((25, 25, 130, 130), fill="red", outline="red")
# draw.text((42, 62), 'SALE', font=font, fill='white')


draw = ImageDraw.Draw(img1)
font = ImageFont.truetype('Roboto-Light.ttf', size=30)
draw.ellipse((25, 25, 130, 130), fill="green", outline="green")
draw.text((45, 62), 'NEW', font=font, fill='white')



# height, width = img1.size
# size = height / 100 * x, width / 100 * x
# img1.thumbnail(size)



#img1.thumbnail((img1.size))
img1.show()
# img1.save('1661_15.jpg', quality=100)