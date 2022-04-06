# VulDeeLocator: A Deep Learning-Based Fine-Grained Vulnerability Detector

We propose Vulnerability Deep learning-based Locator (VulDeeLocator), a deep learning-based fine-grained vulnerability detector, for C/C++ programs with source code. VulDeeLocator advances the state-of-the-art by simultaneously achieving a high detection capability and a high locating precision. The core innovations underlying VulDeeLocator are (i) the leverage of intermediate code to accommodate semantic information that cannot be conveyed by source code-based representation, and (ii) the concept of granularity refinement for precisely pinning down locations of vulnerabilities.

We extract pieces of source code according to some syntax information (i.e., source code- and Syntax-based Vulnerability Candidate or sSyVC for short), involving four kinds of sSyVCs: library/API function call (FC), array definition (AD), pointer definition (PD), and arithmetic expression (AE). Then we extend these pieces of code to accommodate the semantic information from the intermediate code (i.e., intermediate code- and Semantics-based Vulnerability Candidate or iSeVC for short).

We prepare a dataset of Lower Level Virtual Machine (LLVM) intermediate code with accompanying program source code from two data sources: the National Vulnerability Database (NVD) and the Software Assurance Reference Dataset (SARD). We collect 15,150 programs, including 2,821 real-world programs and 12,329 synthetic and academic programs. The dataset contains 155,539 vulnerability candidates in intermediate code (i.e., iSeVC), among which 40,382 are vulnerable and 115,157 are not vulnerable. For vulnerable iSeVCs, the line numbers of the vulnerabilities are available.

## Setup
  * [Install Anaconda](https://www.anaconda.com/products/individual)
  * ```
    $ conda update conda

    # For organizing dataset
    $ conda create --name vdl_data python=2.7

    # For data preprocessing and modeling
    $ conda create --name vdl python=3.6
    $ conda activate vdl
    (vdl) $ pip install -r requirements.txt
    ```

## Usage
  * Organizing datasets
    ```
    $ conda activate vdl_data

    (vdl_data) $ ./unzip.sh

    # NVD dataset
    # NOTE: Couldn't find mentioned "process_dataflow_NVD.py" file below, so we ignore this for now.

    # SARD dataset
    (vdl_data) $ cd ./src/SARD/sourcefile
    (vdl_data) $ cp ../../../../../data/iSeVCs/iSeVCs_for_train_programs/*.txt .
    ```
  * Data preprocess
    ```
    $ conda activate vdl

    (vdl) $ cd src/data_preprocess/

    # NVD
    # TODO

    # SARD
    (vdl) $ python process_dataflow.py

    (vdl) $ python create_word2vecmodel.py
    (vdl) $ python get_dl_input.py
    ```
  * Train model
    ```
    $ conda activate vdl

    (vdl) $ cd src/
    (vdl) $ python bgru_threshold.py
    (vdl) $ python bgru_raw.py
    ```
