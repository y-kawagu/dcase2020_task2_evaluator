# dcase2020_task2_evaluator
このスクリプトはdcase2020_task2で出力したeval dataのanomaly scoreの
各マシンごとのAUC,pAUCを出力することを目的としています。  

## Description
AUC、pAUC算出スクリプトは以下のスクリプトで構成されています。
- `evaluator.py`
    - このスクリプトは anomaly score が格納されたディレクトリと真値のcsvを使用して、AUC、pAUCを出力します。 **teams/<team_name>**
    - AUC、pAUCのcsvファイルは指定したディレクトリに保存されます。 **result_<team_name>.csv**

## usage
### 1. リポジトリのクローン
Githubからこのリポジトリをクローンします。

### 2. 必要なデータの用意
- eval_data_listの用意
    - make_datasetで生成したeval_data_list.csvを指定したディレクトリに格納します。
- anomaly_scoreの用意
    - DCASE2020_task2のシステムのEvaluationモードで実行した時に生成される、
resultディレクトリをチーム名に改名し指定するディレクトリに格納します。


### 3. ディレクトリ構成
- ./dcase2020_task2_evaluator
    - __/teams__ <<evaluatorが参照するディレクトリ
        - /{team_name_1}
            - anomaly_score_(machine_type)_id_NN.csv
            - anomaly_score_(machine_type)_id_NN.csv
            - ...
        - /{team_name_2}
            - anomaly_score_(machine_type)_id_NN.csv
            - anomaly_score_(machine_type)_id_NN.csv
            - ...
        - ...
        - *result_{team_name_1}.csv*
        - *result_{team_name_2}.csv*
    - /README.md
    - __/evaluator.py__ <<evaluator本体
    - __/eval_data_list.csv__　<<evaluatorが参照するファイル
  
上記の構成で動作します。

斜字のデータは`evaluator.py`を実行した後に生成されます。

### 4. パラメーターの変更
パラメーターは`evaluator.py`の以下の定数から変えることができます。
- MAX_FPR
    - FPR(偽陽性率)の閾値 : default 0.1
- EVAL_DATA_LIST_PATH
    - eval_data_list.csvのPath : default "./eval_data_list.csv"
- RESULT_DIR
    - 出力先ディレクトリのPath : default "./teams/"
- TEAMS_ROOT_DIR
    - anomaly score csvを保存しているフォルダ群のPath : "./teams/"

### 5. 実行方法
AUC、pAUC算出スクリプト　`evaluator.py`　を実行します
```
$ python evaluator.py
```
`evaluator.py` は各システムの各マシンごとAUCとpAUCを算出し、結果をディレクトリ **RESULT_DIR** に保存します。

### 6. 結果の確認
出力した結果は各マシンごとに区切られており、idに対応した
AUC、pAUC の結果を確認できます。

`result_<team_name>.csv`
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
In addition, we checked performing on **Windows 10 Pro 1903**.

### Software packages
- Python == 3.6.5

### Python packages
- numpy                         == 1.16.0
- scikit-learn                  == 0.20.2

