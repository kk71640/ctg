#!/bin/sh
  
jupyter nbconvert --to script train.ipynb --output main
rm -f out.log
nohup python main.py > out.log &
tail -f out.log
