import time
from PIL import Image, ImageFilter
import os

if os.path.exists('SOutput') is False:
    os.makedirs('SOutput')
starttime = time.perf_counter()
for file in os.listdir('.'):
    if file.endswith('.jpg'):
        img = Image.open(file)
        Gimg= img.filter(ImageFilter.GaussianBlur(radius = 8))
        name, extension = os.path.splitext(file)
        Gimg.save('SOutput/{}.png'.format(name))
        print(name, extension, ' was processed')
stoptime = time.perf_counter()
print(f'Processed in {stoptime-starttime} seconds ')