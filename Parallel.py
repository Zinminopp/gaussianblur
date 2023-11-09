import time
from PIL import Image,ImageFilter
import os
import concurrent.futures

def image_operation(sample):
    img = Image.open(sample)
    Gimg = img.filter(ImageFilter.GaussianBlur(radius=8))
    name, extension = os.path.splitext(sample)
    Gimg.save('POutput/{}.png'.format(name))
    print(name,extension, ' was processed')


if __name__ == '__main__':
    if os.path.exists('POutput') is False:
        os.makedirs('POutput')
    start = time.perf_counter()
    Images = []

    for file in os.listdir('.'):
        if file.endswith('.jpg'):
            Images.append(file)
    with concurrent.futures.ProcessPoolExecutor () as exe:
        exe.map(image_operation, Images)
    stop = time.perf_counter()

    print('Time taken to processs in seconds ', stop - start)