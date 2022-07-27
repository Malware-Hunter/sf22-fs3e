#!/bin/bash
CHECK_PIP=$(which pip)
[ "$CHECK_PIP" != "" ] || { echo "instale o pip: sudo apt -y install python3-pip"; exit; }
PKGS=(pandas scikit-learn mlxtend matplotlib)
CHECK_PKGS=`pip show ${PKGS[@]} | grep -i -w "not found"`
[ "$CHECK_PKGS" = "" ] || { echo "instale os pacotes Python: sudo pip install ${PKGS[@]}"; exit; }

[[ $1 && $2 ]] || { echo "Uso: bash $0 OUTPUT_PREFIX DATASET [DATASET...]" && exit 1;}
OUTPUT_PREFIX=$1; shift
for DATASET in $*
do
    D_NAME=$(echo $DATASET | awk -F/ '{print $NF}')
    TS=$(date +%Y%m%d%H%M%S)
    OUT_FILENAME="dataset_sigpid_${D_NAME}_$TS"
    echo "python3 -m methods.SigPID.sigpid -d $DATASET -o $OUT_FILENAME --output-prefix $OUTPUT_PREFIX"
    { time python3 -m methods.SigPID.sigpid -d $DATASET -o $OUT_FILENAME --output-prefix $OUTPUT_PREFIX; } 2> time_$OUT_FILENAME.txt
done
