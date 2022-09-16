#!/bin/bash

#for id in 415 416 190 121 122; do
for id in 415; do
    # Clean directories
    rm -rf model_${id}
    mkdir model_${id}
    rm -rf result_${id}
    mkdir result_${id}
    rm -rf result_analyze_${id}
    mkdir -p result_analyze_${id}/TP result_analyze_${id}/TN result_analyze_${id}/FP result_analyze_${id}/FN

    # Train and test model
    time python bgru_threshold.py ${id}
done
