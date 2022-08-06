from sklearn import svm
import sys
import argparse
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_validate
from methods.utils import get_dataset, get_base_parser, get_X_y, get_filename
import logging

def parse_args(argv):
    parser = argparse.ArgumentParser(parents=[get_base_parser()])
    parser.add_argument(
        '-m', '--model', metavar='str',
        help="Models to run evaluation: 'svm', 'rf' (for Random Forest) or 'all'. Default: 'all'",
        choices=['svm', 'rf','all'],
        type=str, default='all')
    parser.add_argument('--n_folds', metavar = 'INT', type = int, default = 10,
        help="Number of folds to use in cross validation. Default: 10")
    args = parser.parse_args(argv)
    return args

def get_classifiers(classifier_name):
    if(classifier_name == 'svm'):
        return {'svm': svm.SVC()}
    elif(classifier_name == 'rf'):
        return {'rf': RandomForestClassifier(random_state = 0)}
    return {'svm': svm.SVC(), 'rf': RandomForestClassifier(random_state = 0)}

def cross_validation(model, X, y, n_folds = 10, metrics=['accuracy', 'precision', 'recall', 'f1', 'roc_auc']):
    results = cross_validate(estimator=model, X=X, y=y, cv=n_folds, scoring=metrics)
    metrics_results = {}
    for metric in metrics:
        metrics_results[metric] = results[f'test_{metric}'].mean() * 100
    return metrics_results

if __name__=="__main__":
    logging.basicConfig(format = '%(name)s - %(levelname)s - %(message)s')
    global logger_eval
    logger_eval = logging.getLogger('EVALUATION')
    logger_eval.setLevel(logging.INFO)

    args = parse_args(sys.argv[1:])
    X, y = get_X_y(args, get_dataset(args))

    classifiers = get_classifiers(args.model)
    results = []

    for classifier_name, clf in classifiers.items():
        logger_eval.info('Running Evaluation With %s' % classifier_name.upper())
        results.append({**cross_validation(clf, X, y, args.n_folds), "model": classifier_name})
    pd.DataFrame(results).to_csv(get_filename(args.output_file, prefix=args.output_prefix), index = False)
