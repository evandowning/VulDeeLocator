#!/bin/bash

#   rm -rf ./data/SARD/
#   mkdir -p ./data/SARD/data_source/ ./data/SARD/label_source/ ./data/SARD/corpus/

#   time python copy_source.py /home/evan/labeled-dataset-master/CWE415/source_files/ ./data/SARD/data_source/

#   time python process_dataflow_new.py

#   rm -rf ./w2v_model
#   mkdir ./w2v_model
#   time python create_word2vecmodel.py

rm -rf ./data/vector/
mkdir ./data/vector/
rm -rf ./data/dl_input/
mkdir -p ./data/dl_input/train/ ./data/dl_input/test/
time python get_dl_input_new.py
