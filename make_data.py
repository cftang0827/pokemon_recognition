import numpy as np 
import cv2 
import random 
import os 
from tqdm import tqdm 

data_list = []
image_dirs = os.listdir('pokemon_aug')

for dd in image_dirs:
    if dd == '.DS_Store':
        continue
    image_dir_path = os.path.join('pokemon_aug', dd, 'output')
    for ip in tqdm(os.listdir(image_dir_path)):
        img_path = os.path.join(image_dir_path, ip)
        print(ip)
        if ip == '.DS_Store':
            continue
        img = cv2.imread(img_path)[:,:,::-1]
        data_list.append(img)

data_npy = np.array(data_list)
np.save('data.npy', data_npy)
