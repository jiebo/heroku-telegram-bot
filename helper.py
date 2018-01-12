
import urllib

CONST_TEMP_IMAGE_FILE_NAME = "temp.jpg"


def download_and_return_image(url):
    downloadimagefile(url)
    photo = open(CONST_TEMP_IMAGE_FILE_NAME, 'rb')
    return photo


def downloadimagefile(url):
    """Download image from URL and save into temp file"""
    f = open(CONST_TEMP_IMAGE_FILE_NAME, 'wb')
    f.write(urllib.request.urlopen(url).read())
    f.close()