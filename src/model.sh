#!/bin/bash

#   rm -rf model
#   mkdir model
#   rm -rf result
#   mkdir result
#   rm -rf result_analyze
#   mkdir -p result_analyze/TP result_analyze/TN result_analyze/FP result_analyze/FN
time python bgru_threshold.py
