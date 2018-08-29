import Augmentor
import os 

for ff in os.listdir('pokemon_aug'):
    p = Augmentor.Pipeline(os.path.join('pokemon_aug', ff))
    p.rotate(probability=0.7, max_left_rotation=25, max_right_rotation=25)
    p.zoom(probability=0.5, min_factor=0.6, max_factor=1.5)
    p.random_distortion(probability=1, grid_width=4, grid_height=4, magnitude=8)
    p.flip_left_right(probability=1)
    p.resize(probability=1.0, width=224, height=224)
    p.sample(50)
    p.process()
