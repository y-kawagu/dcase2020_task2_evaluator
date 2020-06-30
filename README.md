# dcase2020_task2_evaluator
このスクリプトはdcase2020_task2で出力したeval_dataのanomaly_scoreの
AUC,pAUCリザルトを出力することを目的としています。  

## usage
DCASE2020_task2のシステムのEvaluationモードで実行した時に生成される
resultディレクトリをチーム名に改名し指定するディレクトリに格納することで
複数のシステムのanomaly_scoreとmake_datasetで生成したeval_data_list.csvを利用して
本スクリプトを実行することで各システムのAUC,ｐAUCのリザルトを出力できます。
- eval_data_list.csvに記載されている機種名の順番でresultが生成されます。
- 指定したディレクトリにresult_<チーム名>.csvが生成されます。
### ディレクトリ構成

- ./dcase2020_task2_evaluator
    - __/teams__
        - /{team_name}
            - anomaly_score_(machine_type)_id_NN.csv
            - anomaly_score_(machine_type)_id_NN.csv
            - ...
        - /{team_name}
            - anomaly_score_(machine_type)_id_NN.csv
            - anomaly_score_(machine_type)_id_NN.csv
            - ...
        - ...
        - *result_{team_name}.csv*
        - *result_{team_name}.csv*
    - /README.md
    - __/evaluator.py__ <<evaluator本体
    - __/eval_data_list.csv__　<<evaluatorが参照するファイル
  
上記の構成で動作します。
太字のデータが同階層にあれば動作するので、別ディレクトリに太字のデータを移動させても問題ありません。
斜字のデータは evaluator.py を実行した後に生成されます。