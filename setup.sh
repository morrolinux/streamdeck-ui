#!/bin/bash

conda init
conda activate
conda create -n streamdeck python=3.9
conda activate streamdeck
cd ~/streamdeck-ui 
pip3 install poetry PySide2 pillow StreamDeck cairosvg filetype obsws-python
conda install pynput packaging
poetry install
