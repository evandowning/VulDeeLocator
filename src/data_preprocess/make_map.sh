#!/bin/bash

cweRoot="/home/evan/labeled-dataset-master/"

for id in 415 416 190 121 122; do
    idRoot="${cweRoot}/CWE${id}/source_files/"

    # For each source file
    for fn in `find ${idRoot} -maxdepth 1 -type f -name '*.c' -o -name '*.cpp'`; do
        outDir=`echo "${fn}_dir/" | rev | cut -d '/' -f 2 | rev`
        cweJson="${fn/source_files/source_labels\/individual}.json"
        cweTxt="${cweJson/.json/.txt}"

        echo $outDir $cweTxt
    done
done
