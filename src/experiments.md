# Parse Source files
```
$ sudo apt install clang llvm libclang-dev libclang-cpp-dev
$ sudo apt install libncurses5
$ sudo cp -R /usr/lib/llvm-11/include/clang-c /usr/include/

# Compile dg
$ git clone https://github.com/mchalupa/dg
$ cd dg
$ mkdir build
$ cd build
$ cmake ..
$ make -j4

(vdl_data) $ cd src/SARD/sourcefile
$ gcc make.cpp
$ ./a.out


# For testing some source files
./test.sh

#TODO
# Generate xml files for source files
python genxml.py

```

# Data Preprocess
```
(vdl) $ cd data_preprocess/

$ ./preprocess.sh

Map between tokenIndexes and lineNumbers is in "tokenMap.txt"
```

# Model
```
$ ./model.sh

See "predictions.txt" file
```
