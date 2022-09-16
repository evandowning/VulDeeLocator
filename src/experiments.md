# Download dataset and decompress
`labeled-dataset-master/`

# Parse Source files
```
# Install dependencies
$ sudo apt install clang llvm libclang-dev libclang-cpp-dev
$ sudo apt install libncurses5
$ sudo cp -R /usr/lib/llvm-11/include/clang-c /usr/include/

# Change directory
$ cd src/SARD/sourcefile

# Compile dg
$ git clone https://github.com/mchalupa/dg
$ cd dg
$ mkdir build
$ cd build
$ cmake ..
$ make -j4
$ make check

# Change environment
$ conda activate vdl_data

# Compile tools
(vdl_data) $ gcc make.cpp
(vdl_data) $ ./a.out

# Test a few source files (manually verify results)
(vdl_data) $ ./test.sh

# Edit extract*.sh scripts with location of dataset
$ vim exract_wild.sh
$ vim exract.sh

# Extract datasets
(vdl_data) $ ./extract_wild.sh &> extract_wild_stdout_stderr.txt
(vdl_data) $ ./extract.sh &> extract_stdout_stderr.txt
```

# Data Preprocess
```
# Change directory
$ cd data_preprocess/

# Change environment
$ conda activate vdl

# Edit make_map.sh with location of dataset
$ vim make_map.sh

# Create mapping for file paths
(vdl) $ ./make_map.sh > map.txt

# Preprocess datasets
(vdl) $ ./preprocess.sh &> preprocess_stdout_stderr.txt

Map between tokenIndexes and lineNumbers is in "tokenMap.txt"
```

# Model
```
# Change environment
$ conda activate vdl

# Train/Test models
(vdl) $ ./model.sh &> model_stdout_stderr.txt

See "predictions*.txt" files for results (keep in mind that the brackets are indexes, not line numbers -- see "tokenMap.txt").

# Graph ROC curves
(vdl) $ ./roc.sh
```
