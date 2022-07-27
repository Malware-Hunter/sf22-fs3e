CHECK_PIP=$(which pip)
[ "$CHECK_PIP" != "" ] || { echo "instale o pip: sudo apt -y install python3-pip"; exit; }
PKGS=(pandas scikit-learn)
CHECK_PKGS=`pip show ${PKGS[@]} | grep -i -w "not found"`
[ "$CHECK_PKGS" = "" ] || { echo "instale os pacotes Python: sudo pip install ${PKGS[@]}"; exit; }

[[ $1 && $2 && $3 ]] || { echo "Uso: bash $0 OUTPUT_PREFIX MODEL DATASET [DATASET...]" && exit 1;}
OUTPUT_PREFIX=$1; shift
MODEL=$1; shift
for DATASET in $*
do
    D_NAME=$(echo $DATASET | awk -F/ '{print $NF}')
    TS=$(date +%Y%m%d%H%M%S)
    OUT_FILENAME="ml_results_${MODEL}_${D_NAME}"
    echo  "python3 -m evaluation -d $DATASET -m $MODEL -o $OUT_FILENAME.csv --output-prefix $OUTPUT_PREFIX"
    { time python3 -m evaluation -d $DATASET -m $MODEL -o $OUT_FILENAME.csv --output-prefix $OUTPUT_PREFIX ; } 2> time_$OUT_FILENAME.txt
done