#!/bin/bash
CHECK_PIP=$(which pip)
[ "$CHECK_PIP" != "" ] || { echo "instale o pip: sudo apt -y install python3-pip"; exit; }
PKGS=(pandas numpy scikit-learn)
CHECK_PKGS=`pip show ${PKGS[@]} | grep -i -w "not found"`
[ "$CHECK_PKGS" = "" ] || { echo "instale os pacotes Python: sudo pip install ${PKGS[@]}"; exit; }

set_increment(){
    TOTAL_FEATURES=$1
    [[ $TOTAL_FEATURES -lt 50 ]] && INCREMENT=1 && return
    [[ $TOTAL_FEATURES -lt 1000 ]] && INCREMENT=5 && return
    INCREMENT=10
}

sigapi(){
    DATASET=$1
    D_NAME=$2
}

bash setup_datasets.sh
[[ $? != 0 ]] && exit 1
[[ $1 && $2 ]] || { echo "Uso: bash $0 OUTPUT_FILE DATASET [DATASET...]" && exit 1;}
OUTPUT_FILE=$1
shift
for DATASET in $*
do
    D_NAME=$(echo $DATASET | awk -F, '{print NF}')
    set_increment `head -1 $DATASET | awk -F, '{print NF-1}'`
    TS=$(date +%Y%m%d%H%M%S)
    echo "python3 -m methods.SigAPI.main -d $DATASET -o resultado-selecao-$D_NAME -i $INCREMENT"
    { time python3 -m methods.SigAPI.main -d $DATASET -o resultado-selecao-$D_NAME -i $INCREMENT; } 2> time_sigapi_${D_NAME}_$TS.txt
done
