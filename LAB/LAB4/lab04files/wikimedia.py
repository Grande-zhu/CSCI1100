"""This module wraps the Wikimedia API for Wikipedia Images. Two types 
of search are possible: gensearch and title search. 

- Gensearch tends to find more relevant images. Currently it is 
  restricted to exact query search.

- Title search also returns useful images, but needs to be carefully
  filtered by name, because it can return random images from a page as
  well.

The search includes three parts: 

- Search for an image file name from a URL
- For each unique file name, search for an image URL for a given size.
  Currently size is hardcoded, but can be changed either by width or 
  by height. 
- Given an image URL, return an image object. Note that occasionally
  images fail to load. In this case, None is returned. 

USE OF THE MODULE: 

The best use of the module is using the function find_images:

     find_images(query_string, target_num_images)
 
which will return a list of image objects given a query, the 
maximum length of the list will be target_num_images, however 
fewer images may also be returned.

ALTERNATE USE OF THE MODULE:

An alternate use is to divide up the use into two steps:

1. Get a list of image URLs using function using function

   find_image_URLs(query_string)

2. Read each image separately using:

   get_image(url)

This use assumes knowledge of loops and understanding of None return
type.

Author: Sibel Adali
Version: 1.0 (10/1/2017)

"""

import requests
from io import BytesIO
from PIL import Image

def find_images(query_string, target_num_images=4):
    """This function wraps three functions to find max 4 valid images for
    a given query, skipping files that do not load properly. The
    returned list is a list of image objects. This is the simplest
    function in this module and the easiest to use.

    """

    image_urls = find_image_URLs(query_string)
    images = []
    num_images = 0
    for url in image_urls:
        im = get_image(url)
        if im != None:
            images.append(im)
            num_images += 1
            if num_images == target_num_images:
                break
    return images

def find_image_URLs(query):
    """This function wraps two functions and returns a list of image
    URLs for a given query. Max number of URLs is currently 10. If no
    image is found, empty set is returned.
    
    """

    image_files = find_image_titles_gensearch(query, filter_by_name=False)
    image_urls = get_urls_given_filename(image_files,imagewidth=400)
    return image_urls


def get_image(image_url):
    """ Returns image object for a given URL or None if the image
    cannot be opened.

    """
    
    try:
        resp = requests.get(image_url)
        im = Image.open(BytesIO(resp.content))
        return im
    except:
        return None

## The following are the more complex helper functions for the
## above main functions.

def check_title(title,queryset):

    """ Check if a given title contains at least one of the 
    words in the original query. This is used for title search to
    eliminate useless images, but also tends to filter useful images.

    """
    
    title = title.lower()
    for word in queryset:
        if title.find(word) != -1:
            return True
    return False

def find_image_titles_gensearch(query, filter_by_name=False):
    """Returns title of images for a given query as a list. At most 10
    image titles will be returned currently. To get more titles,
    paging needs to be implemented. Left for future development. The
    process will fail quietly in case of connectivity or other API
    problems and return an empty set.

    For this query, filter_by_name is not necessary as most images are
    relevant, so it is set to false by default. If set to true, only
    those images with title containing query keywords will be
    returned.

    """

    url = 'https://en.wikipedia.org/w/api.php?action=query&prop=imageinfo|categories&generator=search&gsrsearch="{0}"&gsrnamespace=6&format=json'
    image_files = []

    try:
        resp = requests.get(url.format(query))
        m = resp.json()

        queryset = set(query.lower().split())
    
        for key in m['query']['pages']:
            title = m['query']['pages'][key]['title']
            if filter_by_name:
                if check_title(title, queryset):
                    image_files.append (title)
            else:
                image_files.append (title)
    except:
        pass
            
    return image_files

def find_image_titles_titlesearch(query, filter_by_name=True):
    """Returns title of images for a given Wikipedia page queried as a
    list. This works identical find_images_gensearch at the moment, at
    most 10 image titles will be returned. The process will fail
    quietly in case of connectivity or other API problems and return
    an empty set.

    For this query, filter_by_name is recommended as many irrelevant
    images can also be returned. However, filtering tends to remove
    useful images too. Currently, the use of this functionis not
    recommended.

    """
    
    url = "https://en.wikipedia.org/w/api.php?action=query&titles={0}&prop=images&format=json"
    image_files = []

    try:
        resp = requests.get(url.format(query))
        m = resp.json()

        queryset = set(query.lower().split())
    
        for key in m['query']['pages']:
            for item in m['query']['pages'][key]['images']:
                title = item['title']
                if filter_by_name:
                    if check_title(title, queryset):
                        image_files.append (title)
                else:
                    image_files.append (title)
    except:
        pass
            
    return image_files

def get_urls_given_filename(image_files,imagewidth=400):
    """ Returns a list of URLs of images given in the list
    image_files. The expected width of images can be specified as
    well. If no image is found for a given URL, it fails quietly.

    """

    url = "https://en.wikipedia.org/w/api.php?action=query&titles={0}&prop=imageinfo&&iiprop=url&iiurlwidth={1}&format=json"
    
    url_list = []
    for file_name in image_files:
        try:
            resp = requests.get(url.format(file_name,imagewidth))
            m = resp.json()
            for val in m['query']['pages']:
                for val2 in m['query']['pages'][val]['imageinfo']:
                    im_url = val2['thumburl']
                    url_list.append(im_url)
        except:
            pass
    return url_list


if __name__ == "__main__":
    
    ##Example use of the module

    query_string = input("Enter query => ")
    images = find_images(query_string, target_num_images=4)
    for im in images:
        im.show()
