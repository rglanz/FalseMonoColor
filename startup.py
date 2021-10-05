#!usr/bin/env python3

# Required packages: pyqt5, pyqtgraph, PIL, numpy

# Imports
from PyQt5.Qt import QMainWindow, QApplication, QFileDialog
from pyqtgraph import GraphicsLayoutWidget
from PIL import Image
import pyqtgraph as pg
import numpy as np
import sys

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.fileDialog()
        self.launchGUI()

    def fileDialog(self):
        open_image_dialog = QFileDialog()
        open_image_dialog.setNameFilters(["Images (*.jpg *.png *.bmp *.tif)"])
        open_image_dialog.selectNameFilter("Images (*.jpg *.png *.bmp *.tif)")
        open_image_dialog.exec_()
        self.image_path = open_image_dialog.selectedFiles()

    def launchGUI(self):
        image_object = Image.open(self.image_path[0]).convert('L')
        image_array = np.rot90(np.array(image_object))

        GraphicsLayoutWidget()
        pg.image(image_array)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
