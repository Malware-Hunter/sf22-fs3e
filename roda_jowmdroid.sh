CHECK_PIP=$(which pip)
CHECK_ZIP=$(which unzip)
[ "$CHECK_PIP" != "" ] && [ "$CHECK_ZIP" != "" ] || { echo "instale o pip: sudo apt -y install python3-pip unzip"; exit; }
CHECK_PKGS=$(pip show numpy scipy pandas scikit-learn | grep -i -w "not found")
[ "$CHECK_PKGS" = "" ] || { echo "instale os pacotes Python: sudo pip install numpy scikit-learn scipy pandas"; exit; }

roda_dataset() {
    DATASET=$1
    D_NAME=$(echo $DATASET | cut -d"/" -f2)
    echo "python3 -m methods.JOWMDroid.JOWMDroid -d $DATASET -o jowmdroid_$D_NAME --feature-selection-only --exclude-hyperparameter"
    python3 -m methods.JOWMDroid.JOWMDroid -d $DATASET -o jowmdroid_$D_NAME --feature-selection-only --exclude-hyperparameter
}

bash setup_datasets.sh
[[ $? != 0 ]] && exit 1
[[ $1 ]] || { echo "Uso: bash $0 DATASET [DATASET...]" && exit 1;}
for DATASET in $*
do
    roda_dataset $DATASET
done
