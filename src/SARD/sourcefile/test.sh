rm -rf /home/evan/labeled-dataset-master/CWE415/source_files/CWE415_Double_Free__new_delete_wchar_t_84_bad_omitgood.cpp_dir/

python getVulLineForCounting.py /home/evan/labeled-dataset-master/CWE415/source_files/CWE415_Double_Free__new_delete_wchar_t_84_bad_omitgood.cpp 1.xml
#   python getVulLineForCounting.py /home/evan/labeled-dataset-master/CWE415/source_files/CWE415_Double_Free__new_delete_wchar_t_84_bad_omitbad.cpp 4.xml
#   python getVulLineForCounting.py /home/evan/labeled-dataset-master/samples-from-wild/jasper-version-2.0.11/src/libjasper/base/jas_malloc.c 2.xml
#   python getVulLineForCounting.py /home/evan/labeled-dataset-master/samples-from-wild/samples-from-wild/openjpeg-v2.3.1/hector_build/../src/lib/openjp2/opj_malloc.c 3.xml

cat 1.txt > SARD-hole_line.txt
#   cat 2.txt >> SARD-hole_line.txt
#   cat 3.txt >> SARD-hole_line.txt
#   cat 4.txt >> SARD-hole_line.txt

python multiFileCompile.py /home/evan/labeled-dataset-master/CWE415/source_files/CWE415_Double_Free__new_delete_wchar_t_84_bad_omitgood.cpp 1.xml
#   python multiFileCompile.py /home/evan/labeled-dataset-master/CWE415/source_files/CWE415_Double_Free__new_delete_wchar_t_84_bad_omitbad.cpp 4.xml
#   python multiFileCompile.py /home/evan/labeled-dataset-master/samples-from-wild/jasper-version-2.0.11/src/libjasper/base/jas_malloc.c 2.xml
#   python multiFileCompile.py /home/evan/labeled-dataset-master/samples-from-wild/samples-from-wild/openjpeg-v2.3.1/hector_build/../src/lib/openjp2/opj_malloc.c 3.xml

./get-llvmwithline SARD-hole_line.txt

mv /home/evan/labeled-dataset-master/CWE415/source_files/CWE415_Double_Free__new_delete_wchar_t_84_bad_omitgood.bc /home/evan/labeled-dataset-master/CWE415/source_files/CWE415_Double_Free__new_delete_wchar_t_84_bad_omitgood.cpp_dir
cp /home/evan/labeled-dataset-master/CWE415/source_files/CWE415_Double_Free__new_delete_wchar_t_84_bad_omitgood.cpp /home/evan/labeled-dataset-master/CWE415/source_files/CWE415_Double_Free__new_delete_wchar_t_84_bad_omitgood.cpp_dir

python autoReorder.py /home/evan/labeled-dataset-master/CWE415/source_files/CWE415_Double_Free__new_delete_wchar_t_84_bad_omitgood.cpp_dir/ 1.txt

python getFlawLoc.py /home/evan/labeled-dataset-master/CWE415/source_files/CWE415_Double_Free__new_delete_wchar_t_84_bad_omitgood.cpp_dir/

#NOTE: don't need to do this
#python addFlawtag.py SARD-hole_line.txt

#TODO - not sure if we need this...
#python getSourceLine.py /home/evan/labeled-dataset-master/CWE415/source_files/CWE415_Double_Free__new_delete_wchar_t_84_bad_omitgood.cpp_dir/
