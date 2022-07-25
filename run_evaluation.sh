CHECK_PIP=$(which pip)
[ "$CHECK_PIP" != "" ] || { echo "instale o pip: sudo apt -y install python3-pip"; exit; }
PKGS=(pandas scikit-learn)
CHECK_PKGS=`pip show ${PKGS[@]} | grep -i -w "not found"`
[ "$CHECK_PKGS" = "" ] || { echo "instale os pacotes Python: sudo pip install ${PKGS[@]}"; exit; }

[[ $1 && $2 ]] || { echo "Uso: bash $0 MODEL DATASET [DATASET...]" && exit 1;}
MODEL=$1
shift
for DATASET in $*
do
    D_NAME=$(echo $DATASET | awk -F/ '{print $NF}')
    TS=$(date +%Y%m%d%H%M%S)
    OUT_FILENAME="ml_${MODEL}_${D_NAME}_$TS"
    echo  "python3 -m evaluation -d $DATASET -m $MODEL -o $OUT_FILENAME.csv"
    { time python3 -m evaluation -d $DATASET -m $MODEL -o $OUT_FILENAME.csv; } 2> time_$OUT_FILENAME.csv
done