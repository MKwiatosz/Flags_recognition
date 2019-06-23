#-----------------------------------
# 
#           DATA AUGMENTATION
#
#-----------------------------------

from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img
import os

datagen = ImageDataGenerator(
        rotation_range=10,
        #width_shift_range=0.9,
        #height_shift_range=0.1,
        shear_range=0.1,
        zoom_range=[0.6,0.9],
        #horizontal_flip=False,
        brightness_range=[0.2,5.0],
        rescale=1./255,
        fill_mode='nearest')

img = load_img('flags/ch/ch.png')  # this is a PIL image
x = img_to_array(img)  # this is a Numpy array with shape (3, 150, 150)
x = x.reshape((1,) + x.shape)  # this is a Numpy array with shape (1, 3, 150, 150)

# the .flow() command below generates batches of randomly transformed images
# and saves the results to the `training` directory
i = 0
for batch in datagen.flow(x, batch_size=1,
                          save_to_dir='dataset/test', save_prefix='ch', save_format='jpg'):
    i += 1
    if i > 60:
        break  # otherwise the generator would loop indefinitely

j = 0
