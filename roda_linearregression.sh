#!/bin/bash
CHECK_PIP=$(which pip)
[ "$CHECK_PIP" != "" ] || { echo "instale o pip: sudo apt -y install python3-pip"; exit; }
PKGS=(pandas numpy scikit-learn)
CHECK_PKGS=`pip show ${PKGS[@]} | grep -i -w "not found"`
[ "$CHECK_PKGS" = "" ] || { echo "instale os pacotes Python: sudo pip install ${PKGS[@]}"; exit; }

bash setup_datasets.sh
[[ $? != 0 ]] && exit 1
[[ $1 ]] || { echo "Uso: bash $0 DATASET [DATASET...]" && exit 1;}
for DATASET in $*
do
    echo "python3 -m methods.SigAPI.sigapi_funcoesdeselecao -d $DATASET"
    D_NAME=$(echo $DATASET | awk -F, '{print NF}')
    TS=$(date +%Y%m%d%H%M%S)
    { time python3 -m methods.LinearRegression.LinearRegression -d $DATASET --output-file linear_regression_$D_NAME; } 2> time_LR_${D_NAME}_$TS.txt
done
