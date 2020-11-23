from PIL import Image

img = Image.open('/Users/meshal/Desktop/Img Prossing -Udmy/aspro.jpg')

print(img.size)

img.thumbnail((400, 200))

img.save('astroooo_new.png')
