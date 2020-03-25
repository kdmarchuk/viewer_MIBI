from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog
from random import randrange
import sys
import imageio
import napari
import exifread
import pathlib


class App(QWidget):

    def __init__(self):
        super().__init__()
        
        # Limits to the linear monochrome LUTs within napari
        self.available_LUTs = ['blue', 'cyan', 'gray', 'green', 'magenta', 'red', 'yellow']

        self.run_all()

    # Prompt to select MIBItiff. No error handling.
    def get_working_directory(self):
        mibi_tiff_str = (QFileDialog.getOpenFileName(self, "Select MIBItiff File:"))
        self.mibi_tiff_path = pathlib.Path(str(mibi_tiff_str[0]))
        return self.mibi_tiff_path

    # Opens the tiff file
    def open_tiff(self, file_name):
        image = imageio.mimread(file_name, multifile=True)
        return image

    # Gets the channels from the tags
    def get_tags(self, file_name, num_images):
        f = open(file_name, 'rb')
        tags = exifread.process_file(f)
        channel_list = [str(tags['Image PageName']), str(tags['Thumbnail PageName'])]
        for n in range(2, num_images):
            channel_list.append(str(tags['IFD ' + str(n) + ' PageName']))

        return channel_list

    # Determine how many channels there should be
    def get_image_length(self, image):
        num_images = len(image)
        return num_images

    # launches napari with the fle and channel names
    def launch_napari(self, image, channel_names, LUTs):
        with napari.gui_qt():
            viewer = napari.Viewer()
            for c in range(len(channel_names)):
                viewer.add_image(image[c], name=channel_names[c], visible=False)
                viewer.layers[c].name = channel_names[c]
                viewer.layers[c].colormap = LUTs[randrange(len(LUTs))]
                viewer.layers[c].opacity = 1.0
                viewer.layers[c].blending = 'additive'
                viewer.layers[c].interpolation = 'gaussian'

    # Runs the program
    def run_all(self):
        self.working_path = self.get_working_directory()
        self.im = self.open_tiff(self.mibi_tiff_path)
        self.num_channels = self.get_image_length(self.im)
        self.channels = self.get_tags(self.mibi_tiff_path, self.num_channels)
        self.launch_napari(self.im, self.channels, self.available_LUTs)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())