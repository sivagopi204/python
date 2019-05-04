# importing google_images_download module 
from google_images_download import google_images_download
from PIL import Image
import os

response = google_images_download.googleimagesdownload() 
search_queries =['mobiles'] 

def downloadimages(query):
    arguments = {"keywords": query, "format": "png", "limit":10, "print_urls":True, "size": "large", "aspect_ratio": "panoramic"}
    try:
        response.download(arguments)    
    except:
		pass
for query in search_queries: 
    downloadimages(query) 
    print()

path = 'downloads/mobiles/'
for r, d, f in os.walk(path):
    for file in f:
        if '.png' in file:
            path = os.path.join(r, file)
            im = Image.open(path)
            name = file.rstrip(".png") + ".jpg"
            im.convert('RGB').save(name,"JPEG")

