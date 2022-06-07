import sys
import os
import pickle

#   CWE416_Use_After_Free__malloc_free_char_01_omitbad.c_dir/api
#       CWE416_Use_After_Free__malloc_free_char_01_omitbad-debug.final.ll
#       CWE416_Use_After_Free__malloc_free_char_01_omitbad.final.ll
#       CWE416_Use_After_Free__malloc_free_char_01_omitbad.sliced.final.ll
#       CWE416_Use_After_Free__malloc_free_char_01_omitbad_1_33:data,37:data.sliced.final.ll
#       CWE416_Use_After_Free__malloc_free_char_01_omitbad_1_33:data,37:data_#goodG2B#.final.ll
#       CWE416_Use_After_Free__malloc_free_char_01_omitbad_2_49:data,52:data.sliced.final.ll
#       CWE416_Use_After_Free__malloc_free_char_01_omitbad_2_49:data,52:data_#goodB2G#.final.ll
#       CWE416_Use_After_Free__malloc_free_char_01_omitbad_3_52:data,52:data.sliced.final.ll
#       CWE416_Use_After_Free__malloc_free_char_01_omitbad_3_52:data,52:data_#goodB2G#.final.ll
#       CWE416_Use_After_Free__malloc_free_char_01_omitbad_4_76:time.sliced.final.ll
#       CWE416_Use_After_Free__malloc_free_char_01_omitbad_4_76:time_#main#.final.ll

#   CWE416_Use_After_Free__malloc_free_char_01_omitgood.c_dir/api
#       CWE416_Use_After_Free__malloc_free_char_01_omitgood-debug.final.ll
#       CWE416_Use_After_Free__malloc_free_char_01_omitgood.final.ll
#       CWE416_Use_After_Free__malloc_free_char_01_omitgood.sliced.final.ll
#       CWE416_Use_After_Free__malloc_free_char_01_omitgood_1_31:data,36:data.sliced.final.ll
#       CWE416_Use_After_Free__malloc_free_char_01_omitgood_1_31:data,36:data_#CWE416_Use_After_Free__malloc_free_char_01_bad#.final.ll
#       CWE416_Use_After_Free__malloc_free_char_01_omitgood_2_34:data,36:data.sliced.final.ll
#       CWE416_Use_After_Free__malloc_free_char_01_omitgood_2_34:data,36:data_#CWE416_Use_After_Free__malloc_free_char_01_bad#.final.ll
#       CWE416_Use_After_Free__malloc_free_char_01_omitgood_3_52:time.sliced.final.ll
#       CWE416_Use_After_Free__malloc_free_char_01_omitgood_3_52:time_#main#.final.ll

root = 'data_416/vector'
for folder in ['CWE416_Use_After_Free__malloc_free_char_01_omitbad.c_dir','CWE416_Use_After_Free__malloc_free_char_01_omitgood.c_dir']:
    pathFolder = os.path.join(root,folder)

    for fn in os.listdir(pathFolder):
        path = os.path.join(pathFolder,fn)

        print(path)

        with open(path,'rb') as fr:
            slice_corpus ,slice_linenum, slice_vlinenum, slice_func, testcase = pickle.load(fr)

        sys.stdout.write('\t{0} {1}\n'.format(slice_vlinenum,slice_func))
