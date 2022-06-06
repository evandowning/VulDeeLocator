## coding: utf-8
'''
This python file is used to precess the vulnerability slices, including read the pkl file and split codes into corpus.
Run main function and you can get a corpus pkl file which map the same name slice file.
'''
from __future__ import print_function
from get_tokens import *
import os  
import stat
import pickle  

def get_sentences(slicepath, labelpath, corpuspath):
    """split sentences into corpus
    
    This function is used to split the slice file and split codes into words

    # Arguments
        slicepath: String type, the src of slice files
        labelpath: String type, the src of label files 
        corpuspath: String type, the src to save corpus 

    # Return
        [slices[], linenum[], vlinenum[]] 
    """

    # Read in mapping
    f2f = dict()
    with open('map.txt','r') as fr:
        for line in fr:
            line = line.strip('\n')
            f1,f2 = line.split(' ')
            f2f[f1] = f2

    f2v = dict()

    # Read in vulnerable lines
    for k,v in f2f.items():
        with open(v,'r') as fr:
            for line in fr:
                line = line.strip('\n')
                _,l = line.split(' ')

                if k not in f2v:
                    f2v[k] = list()
                f2v[k].append(int(l))

    # For each program
    for folder in os.listdir(slicepath):  
        srcFolder = os.path.join(slicepath,folder)
        # For each focus
        for fourfocus in os.listdir(srcFolder):
            fourFolder = os.path.join(srcFolder,fourfocus)

            if not os.path.isdir(fourFolder):
                continue

            for filename in os.listdir(fourFolder):
                if not filename.endswith(".final.ll"):
                    continue

                filepath = os.path.join(fourFolder,filename)
                if os.path.getsize(filepath) > 1:
                    f = open(filepath, 'r')
                    sentences = f.read().split("\n")
                    f.close()

                    vlinenumlists = f2v[folder]

                    slice_corpus = []
                    slice_linenum = []
                    slice_vlinenum = []
                    slice_func = []
                    token_index = 0
                    linenum_index = 0
                    funcs = []
                    variables = []

                    if sentences[0] == '\r' or sentences[0] == '':
                        del sentences[0]
                    if sentences == []:
                        continue
                    if sentences[-1] == '' or sentences[-1] == '\r':
                        del sentences[-1]

                    for sentence in sentences:
                        list_tokens = create_tokens(sentence.strip()) 

                        for t_index in range(1,len(list_tokens)):
                            if list_tokens[t_index].startswith("@"):
                                if (list_tokens[0] == "call" and "define" in sentences[sentences.index(sentence)+1]) or (list_tokens[0] == "define" and "call" in sentences[sentences.index(sentence)-1]):
                                    if "good" in list_tokens[t_index] or "bad" in list_tokens[t_index]:
                                        slice_func.append(str(list_tokens[t_index]))
                                    if list_tokens[t_index] in funcs:
                                        list_tokens[t_index] = "func_"+str(funcs.index(list_tokens[t_index]))
                                    else:
                                        funcs.append(list_tokens[t_index])
                                        list_tokens[t_index] = "func_"+str(len(funcs)-1)
                                elif list_tokens[0] == "define" or list_tokens[0] == "store":
                                    if "good" in list_tokens[t_index] or "bad" in list_tokens[t_index]:
                                        slice_func.append(str(list_tokens[t_index]))
                                    if list_tokens[t_index] in funcs:
                                        list_tokens[t_index] = "func_"+str(funcs.index(list_tokens[t_index]))
                                    else:
                                        funcs.append(list_tokens[t_index])
                                        list_tokens[t_index] = "func_"+str(len(funcs)-1)
                                elif not "llvm" in list_tokens[t_index] and ("load" in list_tokens[:t_index] or "call" in list_tokens[:t_index]):
                                    if list_tokens[t_index] in variables:
                                        list_tokens[t_index] = "variable_"+str(variables.index(list_tokens[t_index]))
                                    else:
                                        variables.append(list_tokens[t_index])
                                        list_tokens[t_index] = "variable_"+str(len(variables)-1)

                        slice_corpus = slice_corpus + list_tokens

                        linenum_index += 1
                        slice_linenum.append(token_index)
                        if linenum_index in vlinenumlists:
                            slice_vlinenum.append(token_index)

                        token_index = token_index + len(list_tokens)

                    slice_func = list(set(slice_func))
                    if slice_func == []:
                        slice_func = ['main']

                    folder_path = os.path.join(corpuspath, folder)
                    savefilepath = os.path.join(folder_path, fourfocus+'_'+filename[:-3]+'.pkl')
                    if not os.path.exists(folder_path):
                        os.mkdir(folder_path)
                        #os.chmod(folder_path, stat.S_IRWXO)
                    f = open(savefilepath, 'wb') 
                    pickle.dump([slice_corpus ,slice_linenum, slice_vlinenum, slice_func], f)
                    f.close()
                else:
                    print('\ntoo small: ',filename)

if __name__ == '__main__':
    SLICEPATH = './data/SARD/data_source/'  #path of slices generated by synthetic and academic datasets
    LABELPATH = './data/SARD/label_source/'   #path of labels
    CORPUSPATH = './data/SARD/corpus/'      #path of corpus

    get_sentences(SLICEPATH, LABELPATH, CORPUSPATH)

    print('\nsuccess!')
