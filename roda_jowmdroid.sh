CHECK_PIP=$(which pip)
CHECK_ZIP=$(which unzip)
[ "$CHECK_PIP" != "" ] && [ "$CHECK_ZIP" != "" ] || { echo "instale o pip: sudo apt -y install python3-pip unzip"; exit; }
CHECK_PKGS=$(pip show numpy scipy pandas scikit-learn | grep -i -w "not found")
[ "$CHECK_PKGS" = "" ] || { echo "instale os pacotes Python: sudo pip install numpy scikit-learn scipy pandas"; exit; }

bash setup_datasets.sh
[[ $? != 0 ]] && exit 1
[[ $1 && $2 ]] || { echo "Uso: bash $0 OUTPUT_FILE DATASET [DATASET...]" && exit 1;}
OUTPUT_FILE=$1
shift
for DATASET in $*
do
    D_NAME=$(echo $DATASET | awk -F, '{print NF}')
    echo "python3 -m methods.JOWMDroid.JOWMDroid -d $DATASET -o $OUTPUT_FILE --feature-selection-only --exclude-hyperparameter"
    python3 -m methods.JOWMDroid.JOWMDroid -d $DATASET -o $OUTPUT_FILE --feature-selection-only --exclude-hyperparameter
done
