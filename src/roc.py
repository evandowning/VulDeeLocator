import sys
import os
import argparse
import numpy as np

from sklearn.metrics import roc_curve
from sklearn.metrics import auc

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# Get FPR at TPR
def get_fpr(target_tpr,tpr,fpr):
    return fpr[np.where(tpr>=target_tpr)[0][0]]
# Get TPR at FPR
def get_tpr(target_fpr,tpr,fpr):
    return tpr[np.where(fpr>=target_fpr)[0][0]]
# Get threshold at FPR
def get_thr_fpr(target_fpr,thresholds,fpr):
    return thresholds[np.where(fpr>=target_fpr)[0][0]]
# Get threshold at TPR
def get_thr_tpr(target_tpr,thresholds,tpr):
    return thresholds[np.where(tpr>=target_tpr)[0][0]]

# Graph curve
def graph(y_true,y_score,graphFN):
    fpr, tpr, thresholds = roc_curve(y_true, y_score)
    roc_auc = auc(fpr, tpr)

#   fpr_thresh = 0.01 # 1%

#   # Get TPR at FPR
#   tprATfpr = get_tpr(target_fpr=fpr_thresh,tpr=tpr,fpr=fpr)
#   # Get FPR at TPR
#   fprATtpr = get_fpr(target_tpr=roc_auc,tpr=tpr,fpr=fpr)

    # Initialize subplot
    plt.figure()

#   plt.plot(fpr, tpr, label='AUC: %0.2f, TPR@FPR=%0.3f: %0.2f\n               FPR@TPR=%0.3f: %0.2f' % (roc_auc, fpr_thresh, tprATfpr, roc_auc, fprATtpr))
    plt.plot(fpr, tpr, label='AUC: %0.2f' % (roc_auc,))
    plt.plot([0, 1], [0, 1], 'k--')  # random predictions curve
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.0])
    plt.xlabel('FPR')
    plt.ylabel('TPR')
    plt.legend(loc='lower right')

    plt.savefig(graphFN)
    plt.clf()
    plt.close()

# Get y_true and y_score values
def tally(fn):
    y_true = list()
    y_score = list()

    with open(fn,'r') as fr:
        for e,line in enumerate(fr):
            if e == 0:
                continue
            line = line.strip('\n')

            pkl,rest = line.split('.pkl')
            _,score,true,indexes = rest.split(',',3)

            y_true.append(float(true))
            y_score.append(float(score))

    return y_true,y_score

def _main():
    # Parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('--train', help='train predictions', required=True)
    parser.add_argument('--test', help='test predictions', required=True)
    parser.add_argument('--wild1', help='wild 1 predictions', required=True)
    parser.add_argument('--wild2', help='wild 2 predictions', required=True)
    parser.add_argument('--name', help='name file', required=True)

    args = parser.parse_args()

    # Store arguments
    trainFN = args.train
    testFN = args.test
    wild1FN = args.wild1
    wild2FN = args.wild2
    name = args.name

    y_true_combined = list()
    y_score_combined = list()
    y_true_wild = list()
    y_score_wild = list()

    for fn in [trainFN,testFN,wild1FN,wild2FN]:
        y_true,y_score = tally(fn)

        if fn == trainFN:
            kind = 'train'
            # Graph ROC curve
            graph(y_true,y_score,'{0}_{1}.png'.format(name,kind))
        elif fn == testFN:
            kind = 'test'
            y_true_combined.extend(y_true)
            y_score_combined.extend(y_score)
            # Graph ROC curve
            graph(y_true,y_score,'{0}_{1}.png'.format(name,kind))
        elif fn == wild1FN:
            kind = 'wild1'
            y_true_combined.extend(y_true)
            y_score_combined.extend(y_score)
            y_true_wild.extend(y_true)
            y_score_wild.extend(y_score)
        elif fn == wild2FN:
            kind = 'wild2'
            y_true_combined.extend(y_true)
            y_score_combined.extend(y_score)
            y_true_wild.extend(y_true)
            y_score_wild.extend(y_score)

    # Graph ROC curve
    graph(y_true_wild,y_score_wild,'{0}_wild.png'.format(name))

    # Graph ROC curve
    graph(y_true_combined,y_score_combined,'{0}_combined_test_wild.png'.format(name))

if __name__ == '__main__':
    _main()
