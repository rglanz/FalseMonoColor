# FalseMonoColor

Simple container for pyqtgraph, which allows for the recolorization of images (histological sections, in this usage) using a GUI that I thought I needed to design myself, but had already been done for me :,) (see http://pyqtgraph.org)

![GUI](/assets/gui_use.gif?raw=true)

## Installation

1. Open a conda prompt.

Change the directory to this folder.

Create the virtual environment by typing ```conda env create -f environment.yaml```

#### Launch program

Activate the environment in the conda prompt by typing ```conda activate FalseMonoColor```

Change the directory to this folder.

Type ```python startup.py```

### Usage

Select your image in the file dialog (a demo image can be found at Assets/demo_image.jpg)

See http://pyqtgraph.org for instructions.

### Terminal Shortcut

If you are using a Unix machine (macOS, Linux), create the following bash script:

>\#!/bin/bash
>
>source activate FalseMonoColor
>
>python [your/directory/here]/FalseMonoColor/startup.py

and save it as 'fmc.sh' in your User folder. Change [your/directory/here] to the directory containing FalseMonoColor.

Run the command ```chmod u+x fmc.sh``` in terminal.

From now on, you can launch the GUI by simply typing ```./fmc``` into your terminal.