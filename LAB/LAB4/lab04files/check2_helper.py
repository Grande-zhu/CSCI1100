from PIL import Image

def make_square(im):
    size = im.size
    shorter = min(size[0],size[1])
    im=im.crop((0,0,shorter,shorter))
    return im


