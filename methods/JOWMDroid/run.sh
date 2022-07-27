CHECK_PIP=$(which pip)
CHECK_ZIP=$(which unzip)
[ "$CHECK_PIP" != "" ] && [ "$CHECK_ZIP" != "" ] || { echo "instale o pip: sudo apt -y install python3-pip unzip"; exit; }
CHECK_PKGS=$(pip show numpy scipy pandas scikit-learn | grep -i -w "not found")
[ "$CHECK_PKGS" = "" ] || { echo "instale os pacotes Python: sudo pip install numpy scikit-learn scipy pandas"; exit; }

[[ $1 && $2 ]] || { echo "Uso: bash $0 OUTPUT_PREFIX DATASET [DATASET...]" && exit 1;}
OUTPUT_PREFIX=$1; shift
for DATASET in $*
do
    D_NAME=$(echo $DATASET | awk -F/ '{print $NF}')
    TS=$(date +%Y%m%d%H%M%S)
    OUT_FILENAME="dataset_jowmdroid_${D_NAME}_$TS"
    echo "python3 -m methods.JOWMDroid.JOWMDroid -d $DATASET -o $OUT_FILENAME --output-prefix $OUTPUT_PREFIX --output-prefix $OUTPUT_PREFIX --output-prefix $OUTPUT_PREFIX --output-prefix $OUTPUT_PREFIX --feature-selection-only --exclude-hyperparameter"
    { time python3 -m methods.JOWMDroid.JOWMDroid -d $DATASET -o $OUT_FILENAME --output-prefix $OUTPUT_PREFIX --feature-selection-only --exclude-hyperparameter; } 2> time_$OUT_FILENAME.txt
done
