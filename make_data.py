import numpy as np 
import cv2 
import random 
import os 
from tqdm import tqdm 
import pickle

train_data_list = []
test_data_list = []
image_dirs = os.listdir('pokemon_aug')
overall_number = 30
split_number = 24

for dd in tqdm(image_dirs):
    if dd == '.DS_Store':
        continue
    image_dir_path = os.path.join('pokemon_aug', dd, 'output')
    image_path_list = os.listdir(image_dir_path)
    random.shuffle(image_path_list)

    #train
    for ip in image_path_list[:split_number]:
        img_path = os.path.join(image_dir_path, ip)
        # print(ip)
        if ip == '.DS_Store':
            continue
        img = cv2.imread(img_path)[:,:,::-1] / 255
        train_data_list.append((str(int(dd)-1), img))    # dd --> label. img --> image_np_data
    # test
    for ip in image_path_list[split_number:]:
        img_path = os.path.join(image_dir_path, ip)
        # print(ip)
        if ip == '.DS_Store':
            continue
        img = cv2.imread(img_path)[:,:,::-1] / 255
        test_data_list.append((str(int(dd)-1), img))    # dd --> label. img --> image_np_data


with open('train_data.pickle', 'wb') as f:
    pickle.dump(train_data_list, f)

with open('test_data.pickle', 'wb') as f:
    pickle.dump(test_data_list, f)


