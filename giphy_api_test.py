""" This simple Giphy API test goes out and searches for a gif on the giphy site
    returns the json and strips the image url from it turns it into an array
    that OpenCV uses to display the image.

    Developer: Robert Marchetti
"""

import json
from urllib import parse, request
from skimage import io
import cv2


def search_and_display_image():
    # search url
    url = "http://api.giphy.com/v1/gifs/search"

    params = parse.urlencode({
        "q": "Machine learning",
        "api_key": "heaQPrVNXPVzUgZx4ykPD0oOnwF0sOMD",
        "limit": "5"
    })

    with request.urlopen("".join((url, "?", params))) as response:
        data = json.loads(response.read())
        url = json.dumps(data['data'][0]['images']['downsized_large']['url'], sort_keys=True, indent=4)

        # get the gif image url from the long url
        image_url = url.split('?')[0].strip('"')
        # read the image url to array
        img_arr = io.imread(image_url)
        # Show Image
        cv2.imshow('URL Image', img_arr)
        # wait
        cv2.waitKey(0)


search_and_display_image()
