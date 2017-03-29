import random
import urllib.request

def download_web_image(url)
    title = random.randrange(1, 1000)
    full_name = str(title) + ".jpg"
    urllib.request.urlretrieve(url, full_name)

download_web_image()