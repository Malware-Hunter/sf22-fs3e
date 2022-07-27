CHECK_PIP=$(which pip)
[ "$CHECK_PIP" != "" ] || { echo "instale o pip: sudo apt -y install python3-pip"; exit; }
PKGS=(pandas scikit-learn)
CHECK_PKGS=`pip show ${PKGS[@]} | grep -i -w "not found"`
[ "$CHECK_PKGS" = "" ] || { echo "instale os pacotes Python: sudo pip install ${PKGS[@]}"; exit; }

set_increment(){
    TOTAL_FEATURES=$1
    [[ $TOTAL_FEATURES -lt 10 ]] && INCREMENT=1 && return
    [[ $TOTAL_FEATURES -lt 100 ]] && INCREMENT=10 && return
    [[ $TOTAL_FEATURES -lt 1000 ]] && INCREMENT=100 && return
    INCREMENT=200
}

[[ $1 && $2 ]] || { echo "Uso: bash $0 OUTPUT_PREFIX DATASET [DATASET...]" && exit 1;}
OUTPUT_PREFIX=$1; shift
for DATASET in $*
do
    TOTAL_N_FEATURES=`head -1 "$DATASET" | awk -F, '{print NF-1}'`
    D_NAME=$(echo $DATASET | awk -F/ '{print $NF}')
    set_increment $TOTAL_N_FEATURES
    TS=$(date +%Y%m%d%H%M%S)
    OUT_FILENAME="dataset_rfg_${D_NAME}_$TS"
    echo  "python3 -m methods.RFG.rfg -d $DATASET -i $INCREMENT -o $OUT_FILENAME --output-prefix $OUTPUT_PREFIX"
    { time python3 -m methods.RFG.rfg -d $DATASET -i $INCREMENT -o $OUT_FILENAME --output-prefix $OUTPUT_PREFIX; } 2> time_$OUT_FILENAME.txt
done
