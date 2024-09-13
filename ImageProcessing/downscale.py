from PIL import Image
import os

def downscale_img(img):
    pixels = list(img.getdata())
    width, height = img.size
    pixels = [pixels[i * width:(i + 1) * width] for i in range(height)]

    downscaled = Image.new(mode='RGB', size=(((img.size[0]-1)//2),((img.size[1]-1)//2)))
    d_pixels = downscaled.load()
    for i in range(downscaled.size[0]):
        for j in range(downscaled.size[1]):
            d_pixels[i,j] = tuple(map(lambda x: x//4, map(sum, zip(pixels[2*j][2*i], pixels[2*j+1][2*i], pixels[2*j][2*i+1], pixels[2*j+1][2*i+1]))))
    return downscaled

def downscale_folder(path):
    '''Attempts to downscale all JPEGs in folder.'''
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith('.jpg'):
                img = Image.open(path + '\\'+ file)
                try:
                    down = downscale_img(img)
                    down.save(path + '\\'+ file[:-4] + '-down.jpg')
                except:
                    print('ERROR: File ' + file + ' could not be downscaled.')
                    pass