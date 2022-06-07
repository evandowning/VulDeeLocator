#!/bin/bash

# Get wild sample lines
#   python get_wild.py > get_wild_stdout.txt

sardline="SARD-hole_line_wild.txt"

#   while read -r line; do
#       fn=`echo $line | cut -d' ' -f1`

#       outDir="${fn}_dir/"
#       # Clear directory of data (bc,ll,pkl files)
#       rm -rf "${outDir}"
#       # Create output directory
#       mkdir -p "${outDir}"
#   done < $sardline

#   # Parse data
#   ./get-llvmwithline $sardline

# For each source file
while read -r line; do
    fn=`echo $line | cut -d' ' -f1`

    outDir="${fn}_dir/"

    bc="${fn%.*}.bc"
    txt="${bc/.bc/.txt}"

    echo $fn
    echo $outDir
#   echo $bc
    echo $txt

    cp $bc $outDir
    cp $fn $outDir

    python autoReorder.py $outDir $txt

    python getFlawLoc.py $outDir

done < $sardline
