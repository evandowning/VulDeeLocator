This master branch is the original VulDeeLocator implementation.

For the modifications for running the VulChecker baseline, see the `develop` branch [here](https://github.com/evandowning/VulDeeLocator/tree/develop)

# VulDeeLocator: A Deep Learning-Based Fine-Grained Vulnerability Detector

We propose Vulnerability Deep learning-based Locator (VulDeeLocator), a deep learning-based fine-grained vulnerability detector, for C/C++ programs with source code. VulDeeLocator advances the state-of-the-art by simultaneously achieving a high detection capability and a high locating precision. The core innovations underlying VulDeeLocator are (i) the leverage of intermediate code to accommodate semantic information that cannot be conveyed by source code-based representation, and (ii) the concept of granularity refinement for precisely pinning down locations of vulnerabilities.

We extract pieces of source code according to some syntax information (i.e., source code- and Syntax-based Vulnerability Candidate or sSyVC for short), involving four kinds of sSyVCs: library/API function call (FC), array definition (AD), pointer definition (PD), and arithmetic expression (AE). Then we extend these pieces of code to accommodate the semantic information from the intermediate code (i.e., intermediate code- and Semantics-based Vulnerability Candidate or iSeVC for short).

We prepare a dataset of Lower Level Virtual Machine (LLVM) intermediate code with accompanying program source code from two data sources: the National Vulnerability Database (NVD) and the Software Assurance Reference Dataset (SARD). We collect 15,150 programs, including 2,821 real-world programs and 12,329 synthetic and academic programs. The dataset contains 155,539 vulnerability candidates in intermediate code (i.e., iSeVC), among which 40,382 are vulnerable and 115,157 are not vulnerable. For vulnerable iSeVCs, the line numbers of the vulnerabilities are available.
