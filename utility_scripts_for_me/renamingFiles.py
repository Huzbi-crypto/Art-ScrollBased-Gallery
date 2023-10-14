import os

def rename_files():
    i = 1
    path = os.getcwd() # gets current directory
    script_name = os.path.basename(__file__) # gets script file name
    files = sorted(os.listdir(path), key=lambda x: os.path.getctime(os.path.join(path, x)))
    for filename in files:
        if os.path.isfile(os.path.join(path, filename)) and filename != script_name:
            new_filename = str(i) + os.path.splitext(filename)[1]
            os.rename(os.path.join(path, filename), os.path.join(path, new_filename))
            i += 1

rename_files()
input("Enter a key to exit...")