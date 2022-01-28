from PIL import Image
import os
from os.path import isfile
 
def watermark_with_transparency(input_image_path,
                                output_image_path,
                                watermark_image_path
                                ):
    base_image = Image.open(input_image_path).convert("RGBA") # convert to RGBA is important

    watermark = Image.open(watermark_image_path).convert("RGBA")
    width, height = base_image.size
    mark_width, mark_height = watermark.size
    position = (width-mark_width, height-mark_height) # put the watermark at the lower-right corner

 
    transparent = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    transparent.paste(base_image, (0, 0))
    transparent.paste(watermark, position, mask=watermark)
    transparent.save(output_image_path)

def chooseScale(dir):
    scale25 = '..\Escala\escala2.5x.png'
    scale10 = '..\Escala\escala10x.png'
    if '2.5x' in dir:
        print(dir)
        return scale25       
    elif '10x' in dir:
        return scale10
    else:
        raise Exception(dir)



dirs = os.listdir()
dirs.sort()
print(dirs)
err = []
for dir in dirs:
    dir = dir.lower()
    if isfile(dir) and '.py' not in dir:
        watermark_with_transparency(dir, dir[:-4] + '_escala.png', chooseScale(dir))



