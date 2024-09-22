import random
from PIL import Image
import numpy as np
import os

def generate_section(img, img_down):
    '''Create and save a data and label tensor for one 8x8 section of image.'''
    width, height = img_down.size
    widthU, heightU = img.size
    start_x = random.randrange(0,height-9)
    start_y = random.randrange(0,width-9)
    dataD = list(img_down.getdata())
    dataD = [dataD[i*width:(i+1)*width] for i in range(height)]
    dataU = list(img.getdata())
    dataU = [dataU[i*widthU:(i+1)*widthU] for i in range(heightU)]
    sectionX = []
    sectionY = []
    for x in range(start_x,start_x+8):
        for y in range(start_y,start_y+8):
            sectionX += [dataD[x][y][:3] + (255,)]
            sectionY += [dataU[start_x+x+4][start_y+y+4][:3]+(255,)]
    XSec = np.array(sectionX).reshape(8,8,4).astype('uint8')
    YSec = np.array(sectionY).reshape(8,8,4).astype('uint8')
    return XSec, YSec


def generate_all_data(sample_count, samples_per_image, path):
    '''performs generate_section sample_count times.'''

    image_count = 230
    if samples_per_image * image_count < sample_count:
        print('Not enough data for training samples.')
    else:
        print('Leftover data (lower bound):   ' + str((samples_per_image * image_count) - sample_count))


    Xtr = np.zeros((sample_count,8,8,4), dtype='uint8')
    Ytr = np.zeros((sample_count,8,8,4), dtype='uint8')
    i = 0
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith('.jpg') and not file.endswith('-down.jpg'):
                img = Image.open(path + '\\'+ file)
                imgD= Image.open(path + '\\'+ file[:-4]+'-down.jpg')
                try:
                    for _ in range(samples_per_image):
                        if i < sample_count:
                            tr = generate_section(img,imgD)
                            Xtr[i] = tr[0]
                            Ytr[i] = tr[1]
                        i += 1
                    print(str(((i/sample_count)*100)//1) + '%: Image ' + str(i//samples_per_image) + '/' + str(sample_count//samples_per_image) + ' printed: ' + file)
                            
                except Exception as e:
                    print('Error trying to handle image ' + file + ':  ' + str(e))
            if i >= sample_count:
                break
