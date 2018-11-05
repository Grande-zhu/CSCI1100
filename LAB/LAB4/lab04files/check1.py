from PIL import Image
im = Image.new('RGB', (512,512),'white')

im_1 = Image.open('ca.jpg')
im_1 = im_1.resize((256,256))

im_2 = Image.open('im.jpg')
im_2 = im_2.resize((256,256))

im_3 = Image.open('hk.jpg')
im_3 = im_3.resize((256,256))

im_4 = Image.open('bw.jpg')
im_4 = im_4.resize((256,256))

im.paste( im_1, (0,0))
im.paste( im_2, (256,0))
im.paste( im_3, (0,256))
im.paste( im_4, (256,256))


im.show()

