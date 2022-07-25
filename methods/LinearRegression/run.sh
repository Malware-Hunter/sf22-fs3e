#!/bin/bash
CHECK_PIP=$(which pip)
[ "$CHECK_PIP" != "" ] || { echo "instale o pip: sudo apt -y install python3-pip"; exit; }
PKGS=(pandas numpy scikit-learn)
CHECK_PKGS=`pip show ${PKGS[@]} | grep -i -w "not found"`
[ "$CHECK_PKGS" = "" ] || { echo "instale os pacotes Python: sudo pip install ${PKGS[@]}"; exit; }

[[ $1 ]] || { echo "Uso: bash $0 DATASET [DATASET...]" && exit 1;}
for DATASET in $*
do
    D_NAME=$(echo $DATASET | awk -F/ '{print $NF}')
    TS=$(date +%Y%m%d%H%M%S)
    OUT_FILENAME="dataset_linearregression_${D_NAME}_$TS"
    echo "python3 -m methods.LinearRegression.LinearRegression -d $DATASET -o $OUT_FILENAME"
    { time python3 -m methods.LinearRegression.LinearRegression -d $DATASET -o $OUT_FILENAME; } 2> time_$OUT_FILENAME.txt
done
