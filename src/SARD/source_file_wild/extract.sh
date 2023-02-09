#!/bin/bash

cweRoot="/home/evan/labeled-dataset-master/"

count=1

#TODO
# For each CWE
#for id in 415 416 190 121 122; do
for id in 415; do
    sardline="SARD-hole_line_${id}.txt"
    rm $sardline

    idRoot="${cweRoot}/CWE${id}/source_files/"

    # For each source file
    for fn in `find ${idRoot} -type f`; do
        echo $fn

        outDir="${fn}_dir/"
        # Clear directory of data (bc,ll,pkl files)
        rm -rf "${outDir}"
        # Create output directory
        mkdir -p "${outDir}"
        echo $outDir

        cweJson="${fn/source_files/source_labels\/individual}.json"
        cweXml="${cweJson/.json/.xml}"
        cweTxt="${cweJson/.json/.txt}"
        echo $cweJson
        echo $cweXml

        # Create XML file for line labels
        python genxml.py $cweJson $cweXml $fn $count

        # Extract data
        python getVulLineForCounting.py "${fn}" $cweXml
        cat $cweTxt >> $sardline
        python multiFileCompile.py $fn $cweXml

        count=$((count+1))
    done

    # Parse data
    ./get-llvmwithline $sardline

    idRoot="${cweRoot}/CWE${id}/source_files/"

    # For each source file
    for fn in `find ${idRoot} -type f`; do
        outDir="${fn}_dir/"

        bc="${fn%.*}.bc"

        mv $bc $outDir
        cp $fn $outDir

        cweJson="${fn/source_files/source_labels\/individual}.json"
        cweTxt="${cweJson/.json/.txt}"

        python autoReorder.py $outDir $cweTxt

        python getFlawLoc.py $outDir
    done
done
