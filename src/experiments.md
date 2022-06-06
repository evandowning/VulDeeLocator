# Parse Source files
```
$ sudo apt install clang llvm libclang-dev libclang-cpp-dev
$ sudo cp -R /usr/lib/llvm-11/include/clang-c /usr/include/

# I think they actually provided the binary
#   $ wget https://github.com/mchalupa/dg/releases/download/v0.9-pre/dg_0e0fc8f9.deb
#   $ sudo dpkg -i dg_0e0fc8f9.deb
#   $ sudo apt install libncurses5

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
```

# Model
```
$ ./model.sh
```
