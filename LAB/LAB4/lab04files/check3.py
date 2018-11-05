from PIL import Image
im = Image.new('RGB', (1000,360),'black')

width = (1000-31*2-10*5)//6

im_1 = Image.open('1.jpg')
im_1 = im_1.resize((width,256))

im_2 = Image.open('2.jpg')
im_2 = im_2.resize((width,256))

im_3 = Image.open('3.jpg')
im_3 = im_3.resize((width,256))

im_4 = Image.open('4.jpg')
im_4 = im_4.resize((width,256))

im_5 = Image.open('5.jpg')
im_5 = im_5.resize((width,256))

im_6 = Image.open('6.jpg')
im_6 = im_6.resize((width,256))

im1_x_index = 31
im2_x_index = im1_x_index+width+10
im3_x_index = im2_x_index+width+10
im4_x_index = im3_x_index+width+10
im5_x_index = im4_x_index+width+10
im6_x_index = im5_x_index+width+10

im.paste( im_1, (im1_x_index,20))
im.paste( im_2, (im2_x_index,60))
im.paste( im_3, (im3_x_index,20))
im.paste( im_4, (im4_x_index,60))
im.paste( im_5, (im5_x_index,20))
im.paste( im_6, (im6_x_index,60))

im.show()

