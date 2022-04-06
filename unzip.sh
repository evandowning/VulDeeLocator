#!/bin/bash

extract() {
    root="$1"
    folder="$2"
    file="${folder}.7z"

    cd "$root"

    mkdir "$folder"
    mv "$file" "$folder"
    cd "$folder"
    7z x "$file"
    mv "$file" ../
}

cd data/programs/
root=`pwd`

folder="real-world programs"
extract "$root" "$folder"

folder="synthetic and academic programs"
extract "$root" "$folder"
