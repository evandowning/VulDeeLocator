#!/bin/bash

set -e

BASE="/home/evan/labeled-dataset-master/"
sardline="SARD-hole_line_wild.txt"

# Get wild sample lines
time python get_wild.py --base ${BASE} > get_wild_stdout.txt

# Reset prior run of extracting data
while read -r line; do
    fn=`echo $line | cut -d' ' -f1`

    outDir="${fn}_dir/"
    # Clear directory of data (bc,ll,pkl files)
    rm -rf "${outDir}"
    # Create output directory
    mkdir -p "${outDir}"
done < $sardline

# Parse data
./get-llvmwithline $sardline &> get-llvmwithline_wild_stdout_stderr.txt

# NOTE: takes 5 minutes to get to this point

if [ -f autoreorder_wild_stdout.txt ]; then
    rm autoreorder_wild_stdout.txt
fi

# For each source file
while read -r line; do
    fn=`echo $line | cut -d' ' -f1`

    outDir="${fn}_dir/"

    bc="${fn%.*}.bc"
    txt="${bc/.bc/.txt}"

    # If we've already processed this file
    result=`find $outDir -type f -name '*.final.ll'`
    if [ "$result" != "" ]; then
        continue
    fi

    echo "Parsing $fn"
#   echo $outDir
#   echo $txt

    cp $bc $outDir
    cp $fn $outDir

    python autoReorder.py $outDir $txt >> autoreorder_wild_stdout.txt

    python getFlawLoc.py $outDir

done < $sardline
