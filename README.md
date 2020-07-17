# dcase2020_task2_evaluator
The **dcase2020_task2_evaluator** is a script for calculating the AUC and pAUC scores from the anomaly score list for the evaluation dataset in DCASE 2020 Challenge Task 2 "Unsupervised Detection of Anomalous Sounds for Machine Condition Monitoring".

http://dcase.community/challenge2020/task-unsupervised-detection-of-anomalous-sounds

## Description

The **dcase2020_task2_evaluator** consists of only one script:
- `evaluator.py`
    - This script outputs the AUC and pAUC scores using: 
      - Ground truth of the normal and anomaly labels
      - Anomaly scores for each wave file listed in the csv file for each macine ID

## Usage
### 1. Clone repository
Clone this repository from Github.

### 2. Prepare data
- Ground truth
    - Download the ground truth `eval_data_list.csv` from zenodo and put it at the top directory
- Anomaly scores
    - Generate csv files `anomaly_score_<Machine_Type>\_id_<Machine_ID>.csv` by using a system. (The format information is described [here](http://dcase.community/challenge2020/task-unsupervised-detection-of-anomalous-sounds#submission).) 
    - Rename the directory containing the csv files to a team name
    - Move the directory into **./teams/**

### 3. Check directory structure
- ./dcase2020_task2_evaluator
    - /evaluator.py
    - /eval_data_list.csv
    - /teams
        - /<team_name_1>
            - anomaly_score_<Machine_Type>\_id_<Machine_ID>.csv
            - anomaly_score_<Machine_Type>\_id_<Machine_ID>.csv
            - ...
        - /<team_name_2>
            - anomaly_score_<Machine_Type>\_id_<Machine_ID>.csv
            - anomaly_score_<Machine_Type>\_id_<Machine_ID>.csv
            - ...
        - ...
        - *result_<team_name_1>.csv*
        - *result_<team_name_2>.csv*
        - ...
    - /README.md

The output files (`result_<team_name_1>.csv`, `result_<team_name_2>.csv`, ...) will be generated by this script.
If you use this script to evaluate the output of a single system, one team is enough, and you can assign any team name to <team_name_1>.

### 4. Change parameters
The parameters are defined in the script `evaluator.py` as follows.
- MAX_FPR
    - The FPR threshold for pAUC: default 0.1
- EVAL_DATA_LIST_PATH
    - The path of the ground truth : default "./eval_data_list.csv"
- TEAMS_ROOT_DIR
    - The directory in which each team's subdirectory containing the anomaly scores : "./teams/"
- RESULT_DIR
    - The output directory : default "./teams/"

### 5. Run script
Run the script `evaluator.py` 
```
$ python evaluator.py
```
The script `evaluator.py` calculates the AUC and pAUC scores for each Machine Type and output the calculated scores into the csv files (`result_<team_name_1>.csv`, `result_<team_name_2>.csv`, ...) in **RESULT_DIR** (default: **./teams/**).

### 6. Check results
You can check the AUC and pAUC scores in the `result_<team_name_N>.csv` in **RESULT_DIR**.
The AUC and pAUC scores for each Machine ID are listed as follows:

`result_<team_name_N>.csv`
```
fan
id,AUC,pAUC
01,0.7939877300613497,0.6181788827897966
03,0.8663687150837989,0.6768597471331961
05,0.869850950290476,0.7075731309293712
Average,0.8434024651452082,0.6675372536174548

pump
id,AUC,pAUC
01,0.8455172413793103,0.7014519056261344
03,0.7973451327433627,0.5891942244993014
05,0.8474193548387097,0.6394312393887945
Average,0.8300939096537941,0.6433591231714101

slider
id,AUC,pAUC
01,0.8836516853932583,0.6850975753991722
03,0.8030337078651685,0.5416913069189828
05,0.6597752808988764,0.49645180366646957
Average,0.7821535580524345,0.5744135619948748

valve
id,AUC,pAUC
01,0.57725,0.5109649122807017
03,0.5424166666666665,0.5166666666666667
05,0.551825,0.49144736842105263
Average,0.5571638888888889,0.506359649122807

ToyCar
id,AUC,pAUC
05,0.7480452830188679,0.6356703078450845
06,0.8309132075471697,0.6985104270109235
07,0.8150188679245283,0.645759682224429
Average,0.7979924528301886,0.6599801390268123

ToyConveyor
id,AUC,pAUC
04,0.9368309859154929,0.8021497405485545
05,0.8444647887323944,0.6209043736100816
06,0.8399295774647887,0.670126019273536
Average,0.8737417840375586,0.6977267111440573
```

## Dependency
This script has been verified to work on **Windows 10 Pro 1903**.

### Software packages
- Python == 3.6.5

### Python packages
- numpy                         == 1.16.0
- scikit-learn                  == 0.20.2

