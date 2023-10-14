from PIL import Image
import os

def reduce_image_resolution():
    path = os.getcwd() # gets current directory
    script_name = os.path.basename(__file__) # gets script file name
    for filename in os.listdir(path):
        if os.path.isfile(os.path.join(path, filename)) and filename != script_name:
            if os.path.splitext(filename)[1] in ['.jpg', '.png', '.bmp', '.gif']: # add more image formats if needed
                img = Image.open(os.path.join(path, filename))
                width, height = img.size
                img = img.resize((width//2, height//2), Image.LANCZOS)
                # new_filename = "resized_" + filename
                img.save(os.path.join(path, filename))

reduce_image_resolution()

input("Press a key to exit...")
