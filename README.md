# dcase2020_task2_evaluator
このスクリプトはdcase2020_baselineで出力したeval_dataのanomaly_scoreの
AUC,pAUCリザルトを出力することを目的としています。  

## usage
Evaluation モードで実行した時dcase2020_baselineに生成される
resultディレクトリと同階層にmake_datasetで生成したeval_data_list.csvと
本スクリプトを配置することで使用できます。
- eval_data_list.csvに記載されている機種名の順番でresultが生成されます。
- resultディレクトリ内にresult.csvが生成されます。
### ディレクトリ構成

00_train.pyと01_test.pyを実行したdcase2020_baselineに配置した場合

- ./dcase2020_baseline
    - /dev_data
    - /eval_data
    - /model
    - __/result__ <<evaluatorが参照するディレクトリ
        - anomaly_score_(machine_type)_id_NN.csv
        - anomaly_score_(machine_type)_id_NN.csv
        - ...
    - /00_train.py
    - /01_test.py
    - /common.py
    - /keras_model.py
    - /baseline.yaml
    - /readme.md
    - __/evaluator.py__ <<evaluator本体
    - __/eval_data_list.csv__　<<evaluatorが参照するファイル
  
上記の構成で動作します。
太字のデータが同階層にあれば動作するので、別ディレクトリに太字のデータを移動させても問題ありません。