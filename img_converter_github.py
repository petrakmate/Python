import os
from PIL import Image

# if there is a 'new' folder - use that, if not, create it
save_here = r'C:\Users\User\Pictures\Poke\new_images'
if not os.path.isdir(save_here):
    os.mkdir(save_here)
orig_path = r'C:\Users\User\Pictures\Poke\image_libr'
path_p = os.fsencode(orig_path)

# loop through the folder and filter the jpg files
for img in os.listdir(path_p):
    file = os.fsdecode(img)
    if file.endswith('.jpg'):
        new_img_name = str('new_' + file + '.png').replace('.jpg','')
        new_img_dir = os.path.join(save_here, new_img_name)
        old_img_dir = os.path.join(orig_path, file)
        new_img = Image.open(old_img_dir)
        new_img.save(new_img_dir,'png')
