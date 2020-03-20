from skimage import data
from PIL import Image
import numpy as np
import scipy
from skimage import io
import imageio
import napari
im = imageio.mimread('C:\\Users\\Kyle\\Box\\BIDC Main\\BIDC_Personal Folders\\Kyle\\Research\\TestData\\MIBI\\FOV1_MassCorrected_Filtered_summed_image.tiff', multifile=True)
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
    viewer.add_image(im[1], name='Channel 1')
    viewer.layers[0].name = 'Channel 1'
    viewer.layers[0].colormap = 'red'
    viewer.layers[0].opacity = 0.7
    viewer.layers[0].blending = 'additive'
    viewer.add_image(im[6], name='Channel 6')
    viewer.layers[1].name = 'Channel 6'
    viewer.layers[1].colormap = 'green'
    viewer.layers[1].opacity = 0.7
    viewer.layers[1].blending = 'additive'

