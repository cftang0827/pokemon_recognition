import Augmentor
import os 

for ff in os.listdir('pokemon_aug'):
    p = Augmentor.Pipeline(os.path.join('pokemon_aug', ff))
    p.rotate(probability=0.5, max_left_rotation=25, max_right_rotation=25)
    # p.zoom(probability=0.5, min_factor=0.9, max_factor=1.1)
    p.shear(probability=0.5, max_shear_left=10, max_shear_right=10)
    # p.random_distortion(probability=0.5, grid_width=4, grid_height=4, magnitude=8)
    p.flip_left_right(probability=0.5)
    p.resize(probability=1.0, width=224, height=224)
    p.sample(30)
    p.process()
