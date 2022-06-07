#!/bin/bash

id="190"

#   rm -rf ./data_${id}/SARD/
#   mkdir -p ./data_${id}/SARD/data_source/ ./data_${id}/SARD/label_source/ ./data_${id}/SARD/corpus/

#   time python copy_source.py /home/evan/labeled-dataset-master/CWE${id}/source_files/ ./data_${id}/SARD/data_source/

time python process_dataflow_new.py ${id}

rm -rf ./w2v_model_${id}
mkdir ./w2v_model_${id}
time python create_word2vecmodel.py ${id}

rm -rf ./data_${id}/vector/
mkdir ./data_${id}/vector/
rm -rf ./data_${id}/dl_input/
mkdir -p ./data_${id}/dl_input/train/ ./data_${id}/dl_input/test/
time python get_dl_input_new.py ${id}
