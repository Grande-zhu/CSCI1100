"""
This module tests PIL library installation
"""

import doctest
from io import BytesIO
from PIL import Image
import requests

def test_doctest(x):
    """
    test_doctest(x) returns
    the value x passed in.

    >>> test_doctest(1)
    1
    >>> test_doctest(0)
    0
    """
    return x

def test_PIL():
    """
    test_PIL() loads the image logo, and then rotates and displays it
    Return value: None
    """
    img_file = "http://www.ecse.rpi.edu/~agung/logo.jpg"
    response = requests.get(img_file)
    resized_image = Image.open(BytesIO(response.content))
    cropped_image = resized_image.crop((0, 0, resized_image.size[1], resized_image.size[1]))
    cropped_image.rotate(90).show()
    print("Testing PIL: RPI logo rotated 90 degrees is shown.")

if __name__ == "__main__":
    doctest.testmod(verbose=True)
    test_PIL()
