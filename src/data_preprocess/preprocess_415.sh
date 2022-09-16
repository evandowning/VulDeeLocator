#!/bin/bash

#for id in 415 416 190 121 122 "wild"; do
for id in 415; do
    rm -rf ./data_${id}/SARD/
    mkdir -p ./data_${id}/SARD/data_source/ ./data_${id}/SARD/label_source/ ./data_${id}/SARD/corpus/

    # Took 1 second for wild
    if [[ "$id" == "wild" ]]; then
        time python copy_source.py /home/evan/labeled-dataset-master/wild_compile/ ./data_${id}/SARD/data_source/
    # Took 10 seconds for CWE 416
    else
        time python copy_source.py /home/evan/labeled-dataset-master/CWE${id}/source_files/ ./data_${id}/SARD/data_source/
    fi

    # Took 1 minute for wild
    if [[ "$id" == "wild" ]]; then
        time python process_dataflow_new_wild.py ${id} > process_dataflow_new_wild_stdout.txt
    # Took 10 minutes for CWE 416
    else
        time python process_dataflow_new.py ${id} > process_dataflow_new_${id}_stdout.txt
    fi

    rm -rf ./w2v_model_${id}
    mkdir ./w2v_model_${id}
    # Took 35 seconds for wild
    if [[ "$id" == "wild" ]]; then
        time python create_word2vecmodel_wild.py ${id}
    # Took 20 minutes for CWE 416
    else
        time python create_word2vecmodel.py ${id}
    fi

    rm -rf ./data_${id}/vector/
    mkdir ./data_${id}/vector/
    rm -rf ./data_${id}/dl_input/
    mkdir -p ./data_${id}/dl_input/train/ ./data_${id}/dl_input/test/
    # Took 13 minutes for wild
    if [[ "$id" == "wild" ]]; then
        time python get_dl_input_new_wild.py ${id}
    # Took 25 minutes for CWE 416
    else
        time python get_dl_input_new.py ${id}
    fi
done
