#!/bin/bash

source ~/.bashrc
conda
cd ~/streamdeck-ui 
sleep 5
conda activate streamdeck
poetry run streamdeck &
