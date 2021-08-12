import os
import numpy as np

def conv3D(filter, image, stride):
    channel_number, filter_height, filter_width = filter.shape
    channel_number, image_height, image_width = image.shape
    ofmap_height = image_height - filter_height + stride
    ofmap_width = image_width - filter_width + stride

    psum = np.zeros((channel_number, ofmap_height, ofmap_width))
    for ch in range(channel_number):
        for i in range(ofmap_height):
            for j in range(ofmap_width):
                ofpsum = np.multiply(filter[ch, :, :], image[ch, 0+i:filter_height+i, 0+j:filter_width+j])
                psum[ch ,i, j] =  sum(sum(ofpsum))
                ofmap = sum(psum)

    return ofmap, psum

# Set parameters
pattern_seed    = 2
channels        = 2
filter_height   = 11
filter_width    = 11
ifmap_height    = 80
ifmap_width     = 80
ofmap_height    = ifmap_height - filter_height + 1
ofmap_width     = ifmap_width - filter_width + 1


os.chdir('Patterns')
filter = np.random.randint(0, 2, size=(channels, filter_height, filter_width)) # channel, height, width
image = np.random.randint(0, 2, size=(channels, ifmap_height, ifmap_width))

ofmap, psum = conv3D(filter, image, stride=1)
print(psum.shape)

filename_filter = "filter_random" + str(pattern_seed) + ".dat"
filename_filter_C = "filter_rand" + str(pattern_seed) + "_C++.dat"
filename_image  = "image_random" + str(pattern_seed) + ".dat"
filename_image_C = "image_rand" + str(pattern_seed) + "_C++.dat"
filename_ofmap = "ofmap_random" + str(pattern_seed) + ".dat"
filename_ofmap_C = "ofmap_rand" + str(pattern_seed) + "_C++.dat"
filename_psum = "psum_random" + str(pattern_seed) + ".dat"
filename_psum_C = "psum_rand" + str(pattern_seed) + "_C++.dat"

# Write random array data
with open(filename_filter, 'w') as f:
    for char in filter:
        f.write(str(char))
f.close()
with open(filename_image, 'w') as im:
    for line in image:
        for char in line:
            im.write(str(char))
im.close()
with open(filename_ofmap, 'w') as of:
    for char in ofmap:
        of.write(str(char))
of.close()

# Convert array data to convenient data for C++ pattern
with open(filename_filter, 'r') as f:
    for line in f.readlines():
        line = line.replace('][', ' ')
        line = line.replace('[[', '[')
        line = line.replace(']]', ']')
        line = line.replace(' [', ' ')
        line = line.replace(']', '')
        line = line.replace('[', '\n')
        line = line.replace(' ', '\n')

        with open(filename_filter_C, 'a') as w:
            if line[0] == '\n':
                line = line[1:]
            w.write(line)

# Check whether the number of lines is correct
num_line = 0
with open(filename_filter_C, 'r') as im:
    for line in im.readlines():
        num_line += 1
    if (num_line != filter_height*filter_width*channels):
        print('Warning! This random pattern may not match the format. Please run the script again.')
f.close()
w.close()

with open(filename_image, 'r') as im:
    for line in im.readlines():
        line = line.replace('][', ' ')
        line = line.replace('[[', '[')
        line = line.replace(']]', ']')
        line = line.replace(' [', '')
        line = line.replace(']', '')
        line = line.replace('[', '\n')
        line = line.replace(' ', '\n')

        with open(filename_image_C, 'a') as w:
            if line[0] == '\n':
                line = line[1:]
            w.write(line)

# Check whether the number of lines is correct
num_line = 0
with open(filename_image_C, 'r') as im:
    for line in im.readlines():
        num_line += 1
    if (num_line != ifmap_height*ifmap_width*channels):
        print('Warning! This random pattern may not match the format. Please run the script again.')
im.close()
w.close()

with open(filename_ofmap, 'r') as of:
    for line in of.readlines():
        line = line.replace('.', '')
        line = line.replace('][', ' ')
        line = line.replace('[[', '[')
        line = line.replace(']]', ']')
        line = line.replace(' [', '')
        line = line.replace(']', '')
        line = line.replace('[', '\n')
        line = line.replace(' ', '\n')

        with open(filename_ofmap_C, 'a') as w:
            if line[0] == '\n':
                line = line[1:]
            w.write(line)

# Check whether the number of lines is correct
num_line = 0
with open(filename_ofmap_C, 'r') as of:
    for line in of.readlines():
        num_line += 1
    if (num_line != ofmap_height*ofmap_width):
        print('Warning! This random pattern may not match the format. Please run the script again.')
of.close()
w.close()








# Arrange data path
try:
    shutil.move("./"+ filename_filter_C, "./Convert2C++/.")
except:
    os.replace("./"+ filename_filter_C, "./Convert2C++/" + filename_filter_C)
try:
    shutil.move("./"+ filename_image_C, "./Convert2C++/.")
except:
    os.replace("./"+ filename_image_C, "./Convert2C++/" + filename_image_C)
try:
    shutil.move("./"+ filename_ofmap_C, "./Convert2C++/.")
except:
    os.replace("./"+ filename_ofmap_C, "./Convert2C++/" + filename_ofmap_C)