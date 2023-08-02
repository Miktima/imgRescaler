import json
import os.path
import os
import re
import sys
from PIL import Image


with open('config.json') as json_file:
    confile = json.load(json_file)
    # Parameters for hires photo
    hiresPhoto = {}
    hiresPhoto.update({"maxWidthPort": confile['hiresPhoto']['maxWidthPort']})
    hiresPhoto.update({"maxHeightLand": confile['hiresPhoto']['maxHeightLand']})
    hiresPhoto.update({"quality": confile['hiresPhoto']['quality']})
    hiresPhoto.update({"dpi": confile['hiresPhoto']['dpi']})
    # Parameters for thumbnail photo
    tmbPhoto = {}
    tmbPhoto.update({"maxWidthPort": confile['tmbPhoto']['maxWidthPort']})
    tmbPhoto.update({"maxHeightLand": confile['tmbPhoto']['maxHeightLand']})
    tmbPhoto.update({"quality": confile['tmbPhoto']['quality']})
    tmbPhoto.update({"dpi": confile['tmbPhoto']['dpi']})
    # Configuration parameters
    resFolder = confile['config']['resFolder']
    tmbSuffix = confile['config']['tmbSuffix']

# Load original image from local path 
imgPath = input ("Path to photo: ")
try:    
    origImg = Image.open(imgPath)
except FileNotFoundError:
    print("Error: the path <%s> is not valid" % imgPath)
    sys.exit()
# Get file name to save resized images with the same name
f = re.compile(r'[\w]+.jpg$')
file = f.findall(imgPath)
# Create folder for resized images if it doesn't exist
if os.path.exists(resFolder) == False:
    os.mkdir(resFolder)
# procedure for portrait photo
if origImg.width >= origImg.height:
    # get reduce factor for hires photo
    rel = origImg.width/hiresPhoto["maxWidthPort"]
    # new size for hires photo
    (width, height) = (int(origImg.width // rel), int(origImg.height // rel))
    # resize photo to new size with LANCZOS filter (https://pillow.readthedocs.io/en/stable/handbook/concepts.html#concept-filters)
    hires = origImg.resize((width, height), resample=Image.Resampling.LANCZOS)
    # save hires photo with new dpi and quality
    hires.save(resFolder + "/" + file[0], dpi=(hiresPhoto["dpi"], hiresPhoto["dpi"]), quality=hiresPhoto["quality"])
    # get reduce factor for thumbnail photo
    relTmb = origImg.width/tmbPhoto["maxWidthPort"]
    # new size for thumbnail photo
    (widthTmb, heightTmb) = (int(origImg.width // relTmb), int(origImg.height // relTmb))
    # resize photo to new size with BICUBIC filter (https://pillow.readthedocs.io/en/stable/handbook/concepts.html#concept-filters)
    tmb = origImg.resize((widthTmb, heightTmb), resample=Image.Resampling.BICUBIC)
    # add suffix for thumbnail
    tmbName = re.sub('\.', '_' + tmbSuffix + '.', file[0])
    # save thumbnail photo with new dpi and quality
    tmb.save(resFolder + "/" + tmbName, dpi=(tmbPhoto["dpi"], tmbPhoto["dpi"]), quality=tmbPhoto["quality"])
# procedure for landscape photo (the same steps as for portrait image)
else:
    rel = origImg.height/hiresPhoto["maxHeightLand"]
    (width, height) = (int(origImg.width // rel), int(origImg.height // rel))
    hires = origImg.resize((width, height), resample=Image.Resampling.LANCZOS)
    hires.save(resFolder + "/" + file[0], dpi=(hiresPhoto["dpi"], hiresPhoto["dpi"]), quality=hiresPhoto["quality"])
    relTmb = origImg.height/tmbPhoto["maxHeightLand"]
    (widthTmb, heightTmb) = (int(origImg.width // relTmb), int(origImg.height // relTmb))
    tmb = origImg.resize((widthTmb, heightTmb), resample=Image.Resampling.BICUBIC)
    tmbName = re.sub('\.', '_' + tmbSuffix + '.', file[0])
    tmb.save(resFolder + "/" + tmbName, dpi=(tmbPhoto["dpi"], tmbPhoto["dpi"]), quality=tmbPhoto["quality"])
