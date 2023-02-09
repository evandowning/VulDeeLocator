rm -rf /home/evan/labeled-dataset-master/CWE415/source_files/CWE415_Double_Free__new_delete_wchar_t_84_bad_omitgood.cpp_dir/
rm -rf /home/evan/labeled-dataset-master/CWE415/source_files/CWE415_Double_Free__new_delete_wchar_t_84_bad_omitbad.cpp_dir/
rm -rf /home/evan/labeled-dataset-master/CWE415/source_files/CWE415_Double_Free__new_delete_wchar_t_54e_omitgood.cpp_dir/
rm -rf /home/evan/labeled-dataset-master/CWE415/source_files/CWE415_Double_Free__new_delete_wchar_t_54e_omitbad.cpp_dir/
rm -rf /home/evan/labeled-dataset-master/samples-from-wild/jasper-version-2.0.11/src/libjasper/base/jas_malloc.c_dir/
rm -rf /home/evan/labeled-dataset-master/samples-from-wild/samples-from-wild/openjpeg-v2.3.1/src/lib/openjp2/opj_malloc.c_dir/

python getVulLineForCounting.py /home/evan/labeled-dataset-master/CWE415/source_files/CWE415_Double_Free__new_delete_wchar_t_84_bad_omitgood.cpp 1.xml
python getVulLineForCounting.py /home/evan/labeled-dataset-master/CWE415/source_files/CWE415_Double_Free__new_delete_wchar_t_84_bad_omitbad.cpp 4.xml
python getVulLineForCounting.py /home/evan/labeled-dataset-master/CWE415/source_files/CWE415_Double_Free__new_delete_wchar_t_54e_omitgood.cpp 5.xml
python getVulLineForCounting.py /home/evan/labeled-dataset-master/CWE415/source_files/CWE415_Double_Free__new_delete_wchar_t_54e_omitbad.cpp 6.xml
python getVulLineForCounting.py /home/evan/labeled-dataset-master/samples-from-wild/jasper-version-2.0.11/src/libjasper/base/jas_malloc.c 2.xml
python getVulLineForCounting.py /home/evan/labeled-dataset-master/samples-from-wild/samples-from-wild/openjpeg-v2.3.1/src/lib/openjp2/opj_malloc.c 3.xml

cat 1.txt > SARD-hole_line.txt
cat 2.txt >> SARD-hole_line.txt
cat 3.txt >> SARD-hole_line.txt
cat 4.txt >> SARD-hole_line.txt
cat 5.txt >> SARD-hole_line.txt
cat 6.txt >> SARD-hole_line.txt

python multiFileCompile.py /home/evan/labeled-dataset-master/CWE415/source_files/CWE415_Double_Free__new_delete_wchar_t_84_bad_omitgood.cpp 1.xml
python multiFileCompile.py /home/evan/labeled-dataset-master/CWE415/source_files/CWE415_Double_Free__new_delete_wchar_t_84_bad_omitbad.cpp 4.xml
python multiFileCompile.py /home/evan/labeled-dataset-master/CWE415/source_files/CWE415_Double_Free__new_delete_wchar_t_54e_omitgood.cpp 5.xml
python multiFileCompile.py /home/evan/labeled-dataset-master/CWE415/source_files/CWE415_Double_Free__new_delete_wchar_t_54e_omitbad.cpp 6.xml
python multiFileCompile.py /home/evan/labeled-dataset-master/samples-from-wild/jasper-version-2.0.11/src/libjasper/base/jas_malloc.c 2.xml
python multiFileCompile.py /home/evan/labeled-dataset-master/samples-from-wild/samples-from-wild/openjpeg-v2.3.1/src/lib/openjp2/opj_malloc.c 3.xml

exit


./get-llvmwithline SARD-hole_line.txt


mv /home/evan/labeled-dataset-master/CWE415/source_files/CWE415_Double_Free__new_delete_wchar_t_84_bad_omitgood.bc /home/evan/labeled-dataset-master/CWE415/source_files/CWE415_Double_Free__new_delete_wchar_t_84_bad_omitgood.cpp_dir
cp /home/evan/labeled-dataset-master/CWE415/source_files/CWE415_Double_Free__new_delete_wchar_t_84_bad_omitgood.cpp /home/evan/labeled-dataset-master/CWE415/source_files/CWE415_Double_Free__new_delete_wchar_t_84_bad_omitgood.cpp_dir

mv /home/evan/labeled-dataset-master/CWE415/source_files/CWE415_Double_Free__new_delete_wchar_t_84_bad_omitbad.bc /home/evan/labeled-dataset-master/CWE415/source_files/CWE415_Double_Free__new_delete_wchar_t_84_bad_omitbad.cpp_dir
cp /home/evan/labeled-dataset-master/CWE415/source_files/CWE415_Double_Free__new_delete_wchar_t_84_bad_omitbad.cpp /home/evan/labeled-dataset-master/CWE415/source_files/CWE415_Double_Free__new_delete_wchar_t_84_bad_omitbad.cpp_dir

mv /home/evan/labeled-dataset-master/CWE415/source_files/CWE415_Double_Free__new_delete_wchar_t_54e_omitgood.bc /home/evan/labeled-dataset-master/CWE415/source_files/CWE415_Double_Free__new_delete_wchar_t_54e_omitgood.cpp_dir
cp /home/evan/labeled-dataset-master/CWE415/source_files/CWE415_Double_Free__new_delete_wchar_t_54e_omitgood.cpp /home/evan/labeled-dataset-master/CWE415/source_files/CWE415_Double_Free__new_delete_wchar_t_54e_omitgood.cpp_dir

mv /home/evan/labeled-dataset-master/CWE415/source_files/CWE415_Double_Free__new_delete_wchar_t_54e_omitbad.bc /home/evan/labeled-dataset-master/CWE415/source_files/CWE415_Double_Free__new_delete_wchar_t_54e_omitbad.cpp_dir
cp /home/evan/labeled-dataset-master/CWE415/source_files/CWE415_Double_Free__new_delete_wchar_t_54e_omitbad.cpp /home/evan/labeled-dataset-master/CWE415/source_files/CWE415_Double_Free__new_delete_wchar_t_54e_omitbad.cpp_dir

mv /home/evan/labeled-dataset-master/samples-from-wild/jasper-version-2.0.11/src/libjasper/base/jas_malloc.bc /home/evan/labeled-dataset-master/samples-from-wild/jasper-version-2.0.11/src/libjasper/base/jas_malloc.c_dir
cp /home/evan/labeled-dataset-master/samples-from-wild/jasper-version-2.0.11/src/libjasper/base/jas_malloc.c /home/evan/labeled-dataset-master/samples-from-wild/jasper-version-2.0.11/src/libjasper/base/jas_malloc.c_dir

mv /home/evan/labeled-dataset-master/samples-from-wild/samples-from-wild/openjpeg-v2.3.1/src/lib/openjp2/opj_malloc.bc /home/evan/labeled-dataset-master/samples-from-wild/samples-from-wild/openjpeg-v2.3.1/src/lib/openjp2/opj_malloc.c_dir
cp /home/evan/labeled-dataset-master/samples-from-wild/samples-from-wild/openjpeg-v2.3.1/src/lib/openjp2/opj_malloc.c /home/evan/labeled-dataset-master/samples-from-wild/samples-from-wild/openjpeg-v2.3.1/src/lib/openjp2/opj_malloc.c_dir


python autoReorder.py /home/evan/labeled-dataset-master/CWE415/source_files/CWE415_Double_Free__new_delete_wchar_t_84_bad_omitgood.cpp_dir/ 1.txt
python autoReorder.py /home/evan/labeled-dataset-master/CWE415/source_files/CWE415_Double_Free__new_delete_wchar_t_84_bad_omitbad.cpp_dir/ 4.txt
python autoReorder.py /home/evan/labeled-dataset-master/CWE415/source_files/CWE415_Double_Free__new_delete_wchar_t_54e_omitgood.cpp_dir/ 5.txt
python autoReorder.py /home/evan/labeled-dataset-master/CWE415/source_files/CWE415_Double_Free__new_delete_wchar_t_54e_omitbad.cpp_dir/ 6.txt
python autoReorder.py /home/evan/labeled-dataset-master/samples-from-wild/jasper-version-2.0.11/src/libjasper/base/jas_malloc.c_dir/ 2.txt
python autoReorder.py /home/evan/labeled-dataset-master/samples-from-wild/samples-from-wild/openjpeg-v2.3.1/src/lib/openjp2/opj_malloc.c_dir/ 3.txt

python getFlawLoc.py /home/evan/labeled-dataset-master/CWE415/source_files/CWE415_Double_Free__new_delete_wchar_t_84_bad_omitgood.cpp_dir/
python getFlawLoc.py /home/evan/labeled-dataset-master/CWE415/source_files/CWE415_Double_Free__new_delete_wchar_t_84_bad_omitbad.cpp_dir/
python getFlawLoc.py /home/evan/labeled-dataset-master/CWE415/source_files/CWE415_Double_Free__new_delete_wchar_t_54e_omitgood.cpp_dir/
python getFlawLoc.py /home/evan/labeled-dataset-master/CWE415/source_files/CWE415_Double_Free__new_delete_wchar_t_54e_omitbad.cpp_dir/
python getFlawLoc.py /home/evan/labeled-dataset-master/samples-from-wild/jasper-version-2.0.11/src/libjasper/base/jas_malloc.c_dir/
python getFlawLoc.py /home/evan/labeled-dataset-master/samples-from-wild/samples-from-wild/openjpeg-v2.3.1/src/lib/openjp2/opj_malloc.c_dir/

#NOTE: don't need to do this
#python addFlawtag.py SARD-hole_line.txt

#NOTE: don't need to do this
#python getSourceLine.py /home/evan/labeled-dataset-master/CWE415/source_files/CWE415_Double_Free__new_delete_wchar_t_84_bad_omitgood.cpp_dir/
