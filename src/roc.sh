#!/bin/bash

#for id in 415 416 190 121 122; do
for id in 415 416; do
    time python roc.py --train predictions_${id}_train.txt \
                       --test predictions_${id}_test.txt \
                       --wild1 predictions_${id}_wild_1.txt \
                       --wild2 predictions_${id}_wild_2.txt \
                       --name ${id}
done
