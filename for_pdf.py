from PIL import Image


print("Изменения")

im_list = ["1661_0.jpg", "ORh_274063_.jpg", "5425_0.jpg", "ORh_274064_.jpg"]
#
# im1 = Image.open("1661_0.jpg")
# im2 = Image.open("ORh_274063_.jpg")
# im3 = Image.open("5425_0.jpg")
# im4 = Image.open("ORh_274064_.jpg")
# im_list = [im2, im3, im4]
#
pdf1_filename = "catalog3.pdf"
# im1.save(pdf1_filename, "PDF", resolution=100.0, save_all=True, append_images=im_list)

im_list_obj = []
for i in im_list:
    im_list_obj.append(Image.open(i))
imk = im_list_obj.pop(0)
imk.save(pdf1_filename, "PDF", resolution=100.0, save_all=True, append_images=im_list_obj)
print('good')