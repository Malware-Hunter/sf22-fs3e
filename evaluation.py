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
from sklearn.model_selection import cross_val_score, cross_validate
from sklearn.model_selection import train_test_split

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
    parser.add_argument('--cv', '--k_fold',metavar = 'INT', type = int, default = 10,
        help="Number of folds to use in cross validation. Default: 10")
    args = parser.parse_args(argv)
    return args

def get_classifiers(classifier_name):
    if(classifier_name == 'svm'):
        return {'svm': svm.SVC()}
    elif(classifier_name == 'rf'):
        return {'rf': RandomForestClassifier(random_state = 0)}
    return {'svm': svm.SVC(), 'rf': RandomForestClassifier(random_state = 0)}

def cross_validation(model, _X, _y, _cv = args.k_fold):
      '''Function to perform K Folds Cross-Validation
       Parameters
       ----------
      model: Python Class, default=None
              This is the machine learning algorithm to be used for training.
      _X: array
           This is the matrix of features.
      _y: array
           This is the target variable.
      _cv: int, default=5
          Determines the number of folds for cross-validation.
       Returns
       -------
       The function returns a dictionary containing the metrics 'accuracy', 'precision',
       'recall', 'f1' for both training set and validation set.
      '''
      _scoring = ['accuracy', 'precision', 'recall', 'f1']
      results = cross_validate(estimator=model,
                               X=_X,
                               y=_y,
                               cv=_cv,
                               scoring=_scoring,
                               return_train_score=True)
      
      return {"Training Accuracy scores": results['train_accuracy'],
              "Mean Training Accuracy": results['train_accuracy'].mean()*100,
              "Training Precision scores": results['train_precision'],
              "Mean Training Precision": results['train_precision'].mean()*100,
              "Training Recall scores": results['train_recall'],
              "Mean Training Recall": results['train_recall'].mean()*100,
              "Training F1 scores": results['train_f1'],
              "Mean Training F1 Score": results['train_f1'].mean()*100,
              "Validation Accuracy scores": results['test_accuracy'],
              "Mean Validation Accuracy": results['test_accuracy'].mean()*100,
              "Validation Precision scores": results['test_precision'],
              "Mean Validation Precision": results['test_precision'].mean()*100,
              "Validation Recall scores": results['test_recall'],
              "Mean Validation Recall": results['test_recall'].mean()*100,
              "Validation F1 scores": results['test_f1'],
              "Mean Validation F1 Score": results['test_f1'].mean()*100
              }

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
    
    cross_validation(model = classifiers, _X, _y, _cv = args.k_fold)

    for classifier_name, clf in classifiers.items():
        print('Fit Model', classifier_name)
        start_time = timeit.default_timer()
        clf.fit(X,y)
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
