from sklearn import svm
import sys
import os
import argparse
import numpy as np
import pandas as pd
import timeit
from sklearn import metrics
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix

def parse_args(argv):
    parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument(
        '-d', '--dataset', metavar='str',
        help='Dataset (csv file).', type=str, required=True)
    parser.add_argument(
        '-c', '--classifier', metavar='str',
        help="Classifier.",
        choices=['svm', 'rf','both'],
        type=str, default='both')
     parser.add_argument('--train-size', type = float, default = 0.8, 
        help = 'Proportion of samples to use for train. Default: 0.8')
     parser.add_argument('--cv', metavar = 'INT', type = int, default = 10,
        help="Number of folds to use in cross validation. Default: 10")
    args = parser.parse_args(argv)
    return args

def get_classifiers(classifier_name):
    if(classifier_name == 'svm'):
        return {'svm': svm.SVC()}
    elif(classifier_name == 'rf'):
        return {'rf': RandomForestClassifier(random_state = 0)}
    return {'svm': svm.SVC(), 'rf': RandomForestClassifier(random_state = 0)}

if __name__=="__main__":
    args = parse_args(sys.argv[1:])

    try:
        dataset = pd.read_csv(args.dataset)
    except BaseException as e:
        print('Exception: {}'.format(e))
        exit(1)

    X = dataset.iloc[:,:-1] # features
    y = dataset.iloc[:,-1] # class

    classifiers = get_classifiers(args.classifier)

    for classifier_name, clf in classifiers.items():
        print('Fit Model', classifier_name)
        start_time = timeit.default_timer()
        clf.fit(X, y)
        end_time = timeit.default_timer()
        print("Elapsed Time:", end_time - start_time)

        print('Predict')
        start_time = timeit.default_timer()
        pred = clf.predict(X)
        end_time = timeit.default_timer()
        print("Elapsed Time:", end_time - start_time)

        accuracy = metrics.accuracy_score(y, pred)
        precision = metrics.precision_score(y, pred, zero_division = 0)
        recall = metrics.recall_score(y, pred, zero_division = 0)
        f1_score = metrics.f1_score(y, pred, zero_division = 0)
        roc_auc = metrics.roc_auc_score(y, pred)

        precision *= 100.0
        accuracy *= 100.0
        recall *= 100.0
        f1_score *= 100.0
        roc_auc *= 100.0

        data = [{'Accuracy':accuracy,'Precision':precision,'Recall':recall,'F1_Score':f1_score,'RoC_AuC':roc_auc}]
        df = pd.DataFrame(data)

        x = (args.dataset).split("/")
        df.to_csv(classifier_name+ "_output_" + x[-1], index = False)
        print(df)
