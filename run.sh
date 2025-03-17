#!/bin/bash

source ~/.bashrc
cd ~/streamdeck-ui 
conda activate streamdeck
xhost si:localuser:$USER
poetry run streamdeck &
