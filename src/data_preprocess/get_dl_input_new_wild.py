## coding: utf-8
'''
This python file is used to split database into 80% train set and 20% test set, tranfer the original code into vector, creating input file of deap learning model.
'''
from __future__ import print_function
from gensim.models.word2vec import Word2Vec
import numpy as np
import pickle
import sys
import os
import gc

VECTOR_DIM = 30  
MAXLEN = 900   

def generate_corpus(model, sample):
    """generate corpus
    This function is used to create input of deep learning model
    # Arguments
        #w2vModelPath: String, the path of word2vec or doc2vec model
        model : word2vec model
        samples: List, the samples
    # Return
        dl_corpus: the vectors of corpus
    """

    dl_corpus = []
    for word in sample:
        if word in model:
            dl_corpus.append(model[word])
        else:
            dl_corpus.append([0]*VECTOR_DIM)

    return [dl_corpus]

def get_dldata(filepath, folders, dlTrainCorpusPath, dlTestCorpusPath, seed=2018, batch_size=16):
    """create deeplearning model dataset
    This function is used to create train dataset and test dataset

    # Arguments
        filepath: String, path of all vectors
        dlTrainCorpusPath: String, path of train set
        dlTestCorpusPath: String, path of test set
        seed: seed of random
        batch_size: the size of mini-batch
    """

    split=0.8
    folders_train = folders[:int(len(folders)*split)]
    folders_test = folders[int(len(folders)*split):]

    print(len(folders_train),len(folders_test))

    print("produce train dataset...")
    for mode in ["api", "arr", "bds", "point"]:
        N = 1
        num = [0]
        for i in num:
            train_set = [[], [], [], [], [], []]
            for folder in folders_train:
                for filename in os.listdir(folder):
                    if mode not in filename:
                        continue
                    path = os.path.join(folder,filename)
                    print(path)
                    f = open(path, 'rb')
                    data = pickle.load(f)
                    f.close()

                    if len(data[0][0]) > MAXLEN:
                        data[2] = [x for x in data[2] if x <= MAXLEN]
                    data[0] = cutdata(data[0][0])
                    if data[0] == None:
                        continue
                    for n in range(len(data)):
                        train_set[n].append(data[n])
                    train_set[-1].append(path)

            outFN = dlTrainCorpusPath + mode + "_" + str(i) + ".pkl"
            print(outFN)
            f_train = open(outFN, 'wb')
            pickle.dump(train_set, f_train)
            f_train.close()

            del train_set 
            gc.collect() 


    print("produce test dataset...")
    for mode in ["api", "arr", "bds", "point"]:
        N = 1
        num = [0]
        for i in num:
            test_set = [[], [], [], [], [], []]
            for folder in folders_test:
                for filename in os.listdir(folder):
                    if mode not in filename:
                        continue
                    path = os.path.join(folder,filename)
                    print(path)
                    f = open(path, 'rb')
                    data = pickle.load(f)
                    f.close()
                    if len(data[0][0]) > MAXLEN:
                        data[2] = [x for x in data[2] if x <= MAXLEN]
                    data[0] = cutdata(data[0][0])
                    if data[0] == None:
                        continue
                    for n in range(len(data)):
                        test_set[n].append(data[n])
                    test_set[-1].append(path)

            outFN = dlTestCorpusPath + mode + "_" + str(i) + ".pkl"
            print(outFN)
            f_test = open(outFN, 'wb')
            pickle.dump(test_set, f_test)
            f_test.close()

            del test_set 
            gc.collect() 

    return

def cutdata(data, maxlen=MAXLEN, vector_dim=VECTOR_DIM):
    """cut data to maxlen
    This function is used to cut the slice or fill slice to maxlen

    # Arguments
        data: The slice
        maxlen: The max length to limit the slice
        vector_dim: the dim of vector
    """
    if maxlen:
        fill_0 = [0]*vector_dim
        if len(data) > 900:
            pass
        if len(data) <=  maxlen:
            data = data + [fill_0] * (maxlen - len(data))
        else:
            data = data[:maxlen]
    return data

if __name__ == "__main__":
    idlabel = sys.argv[1]

    CORPUSPATH = "./data_{0}/SARD/corpus/".format(idlabel)
    VECTORPATH = "./data_{0}/vector/".format(idlabel)
    W2VPATH = "w2v_model_{0}/wordmodel_min_iter5.model".format(idlabel)

    print("turn the corpus into vectors...")
    model = Word2Vec.load(W2VPATH)

    folders = list()

    for root,dirs,files in os.walk(CORPUSPATH):
        for fn in files:
            corpus_path = os.path.join(root,fn)

            vector_folder = root.replace('SARD/corpus','vector')
            if not os.path.exists(vector_folder):
                os.makedirs(vector_folder)

            vector_path = corpus_path.replace('SARD/corpus','vector')

            folders.append(vector_folder)

            f_corpus = open(corpus_path, 'rb')
            data = pickle.load(f_corpus)
            f_corpus.close()

            data.append(data[0])
            data[0] = generate_corpus(model, data[0])

            f_vector = open(vector_path, 'wb')
            pickle.dump(data, f_vector)
            f_vector.close()

    print("\nw2v over...")

    print("spliting the train set and test set...")
    dlTrainCorpusPath = "data_{0}/dl_input/train/".format(idlabel)
    dlTestCorpusPath = "data_{0}/dl_input/test/".format(idlabel)
    get_dldata(VECTORPATH, folders, dlTrainCorpusPath, dlTestCorpusPath)

    print("\nsuccess!")
