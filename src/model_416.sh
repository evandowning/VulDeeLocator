#!/bin/bash

id="416"

#   rm -rf model_${id}
#   mkdir model_${id}
#   rm -rf result_${id}
#   mkdir result_${id}
#   rm -rf result_analyze_${id}
#   mkdir -p result_analyze_${id}/TP result_analyze_${id}/TN result_analyze_${id}/FP result_analyze_${id}/FN
time python bgru_threshold.py ${id}
