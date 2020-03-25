from skimage import data
from PIL import Image
import numpy as np
import scipy
from skimage import io
import imageio
import napari
im = imageio.mimread('C:\\Users\\Kyle\\Box\\BIDC Main\\BIDC_Personal Folders\\Kyle\\Research\\TestData\\MIBI\\FOV1_MassCorrected_Filtered_summed_image.tiff', multifile=True)
print(len(im))
print(im[0].meta)

"""
im = imageio.mimread('C:\\Users\\Kyle\\Box\\BIDC Main\\BIDC_Personal Folders\\Kyle\\Research\\TestData\\MIBI\\FOV1_MassCorrected_Filtered_summed_image.tiff', multifile=True)
print(len(im))
description = (im[10].meta["description"])
print(im[2].meta)
s = str(description)
null = 0
false = 0
description2 = eval(s)
print(description2["channel.target"])
#print(im.shape)

im = Image.open('C:\\Users\\Kyle\\Box\\BIDC Main\\BIDC_Personal Folders\\Kyle\\Research\\TestData\\MIBI\\FOV1_MassCorrected_Filtered_summed_image.tiff')
imarray = np.array(im)
imarray.shape
"""

with napari.gui_qt():
    viewer = napari.Viewer()
    viewer.add_image(im[0], name='Channel 1')
    viewer.layers[0].name = 'Channel 1'
    viewer.layers[0].colormap = 'red'
    viewer.layers[0].opacity = 0.7
    viewer.layers[0].blending = 'additive'
    viewer.add_image(im[1], name='Channel 2')
    viewer.layers[1].name = 'Channel 2'
    viewer.layers[1].colormap = 'green'
    viewer.layers[1].opacity = 0.7
    viewer.layers[1].blending = 'additive'
    viewer.add_image(im[2], name='Channel 3')
    viewer.layers[2].name = 'Channel 3'
    viewer.layers[2].colormap = 'blue'
    viewer.layers[2].opacity = 0.7
    viewer.layers[2].blending = 'additive'
    viewer.add_image(im[3], name='Channel 4')
    viewer.layers[3].name = 'Channel 4'
    viewer.layers[3].colormap = 'green'
    viewer.layers[3].opacity = 0.7
    viewer.layers[3].blending = 'additive'
    viewer.add_image(im[4], name='Channel 5')
    viewer.layers[4].name = 'Channel 5'
    viewer.layers[4].colormap = 'green'
    viewer.layers[4].opacity = 0.7
    viewer.layers[4].blending = 'additive'
    viewer.add_image(im[5], name='Channel 6')
    viewer.layers[5].name = 'Channel 6'
    viewer.layers[5].colormap = 'green'
    viewer.layers[5].opacity = 0.7
    viewer.layers[5].blending = 'additive'
    viewer.add_image(im[6], name='Channel 7')
    viewer.layers[6].name = 'Channel 7'
    viewer.layers[6].colormap = 'green'
    viewer.layers[6].opacity = 0.7
    viewer.layers[6].blending = 'additive'
    viewer.add_image(im[7], name='Channel 8')
    viewer.layers[7].name = 'Channel 8'
    viewer.layers[7].colormap = 'green'
    viewer.layers[7].opacity = 0.7
    viewer.layers[7].blending = 'additive'
    viewer.add_image(im[8], name='Channel 9')
    viewer.layers[8].name = 'Channel 9'
    viewer.layers[8].colormap = 'green'
    viewer.layers[8].opacity = 0.7
    viewer.layers[8].blending = 'additive'

