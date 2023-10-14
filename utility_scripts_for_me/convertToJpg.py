from PIL import Image
import os

def convert_images_to_jpg():
    path = os.getcwd() # gets current directory
    script_name = os.path.basename(__file__) # gets script file name
    for filename in os.listdir(path):
        if os.path.isfile(os.path.join(path, filename)) and filename != script_name:
            if os.path.splitext(filename)[1] in ['.png', '.bmp', '.gif']: # add more image formats if needed
                img = Image.open(os.path.join(path, filename))
                rgb_im = img.convert('RGB')
                rgb_im.save(os.path.join(path, os.path.splitext(filename)[0] + '.jpg'), 'JPEG')
                os.remove(os.path.join(path, filename)) # removes the original file

convert_images_to_jpg()

input("Enter a key to exit...")