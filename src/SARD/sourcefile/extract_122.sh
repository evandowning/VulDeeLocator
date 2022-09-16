#!/bin/bash

set -e

cweRoot="/home/evan/labeled-dataset-master/"


# For each CWE
#for id in 415 416 190 121 122; do
for id in 122; do
    idRoot="${cweRoot}/CWE${id}/source_files/"

    sardline="SARD-hole_line_${id}.txt"
    if [ -f $sardline ]; then
        rm $sardline
    fi

    # For each source file
    count=1
    # Takes about 3 minutes for CWE416
    for fn in `find ${idRoot} -maxdepth 1 -type f \( -name "*.c" -o -name "*.cpp" \)`; do
       echo "Parsing $fn"

        outDir="${fn}_dir/"
        # Clear directory of data (bc,ll,pkl files)
        rm -rf "${outDir}"
        # Create output directory
        mkdir -p "${outDir}"

        cweJson="${fn/source_files/source_labels\/individual}.json"
        cweXml="${cweJson/.json/.xml}"
        cweTxt="${cweJson/.json/.txt}"

        # Create XML file for line labels
        python genxml.py $cweJson $cweXml $fn $count

        # Extract data
        python getVulLineForCounting.py "${fn}" $cweXml
        cat $cweTxt >> $sardline
        python multiFileCompile.py $fn $cweXml

        count=$((count+1))
    done

    # Deduplicate SARD file
    cat ${sardline} | sort | uniq > tmp.txt
    mv tmp.txt ${sardline}

    # Parse data
    # Takes 13 minutes for CWE 416
    ./get-llvmwithline $sardline &> get-llvmwithline_${id}_stdout_stderr.txt

    if [ -f autoreorder_${id}_stdout.txt ]; then
        rm autoreorder_${id}_stdout.txt
    fi

    # For each source file
    # Takes 31 minutes for CWE 416
    while read -r line; do
        fn=`echo $line | cut -d' ' -f1`
        echo "Extracting $fn"

        outDir="${fn}_dir/"
        bc="${fn%.*}.bc"
        cweJson="${fn/source_files/source_labels\/individual}.json"
        cweTxt="${cweJson/.json/.txt}"

        # Clear out files in root of this directory (e.g., in case we re-run this routine while debugging)
        find "${outDir}" -maxdepth 1 -type f -delete

        cp $bc $outDir
        cp $fn $outDir

        python autoReorder.py $outDir $cweTxt >> autoreorder_${id}_stdout.txt

        python getFlawLoc.py $outDir
    done < $sardline
done
