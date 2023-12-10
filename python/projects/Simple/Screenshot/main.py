import pyscreenshot


image= pyscreenshot.grab()
image.show()
image.save('gfg.png')

image1= pyscreenshot.grab(bbox=(40, 40, 600, 900))
image1.show()
image1.save('gfg-cropped.png')


# run below commands before running this program.

# pip install pillow
# pip install pyscreenshot


