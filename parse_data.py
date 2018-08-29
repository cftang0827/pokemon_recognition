import os 
from shutil import copyfile

f = open('data_info.txt', 'r')
raw_data = {}

while True:
    raw = f.readline()
    if raw == '':
        break
    number = int(raw.split('\t')[0].split('#')[-1])
    name = raw.split('\t')[3].split('*')[0]
    raw_data[number] = name
f.close()

os.mkdir('pokemon_aug')

for i in raw_data.keys():
    os.mkdir(os.path.join('pokemon_aug', str(i)))


for fn in os.listdir('pokemon'):
    if fn == '.DS_Store':
        continue
    if len(fn.split('.')[0].split('-')) == 1:
        number = int(fn.split('.')[0].split('f')[0])
        if number <= 151:
            copyfile(os.path.join('pokemon', fn), os.path.join('pokemon_aug', str(number), fn))
        
