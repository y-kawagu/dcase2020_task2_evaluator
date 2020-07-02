########################################################################
# import default python-library
########################################################################
import os
import sys
import csv
import glob
import re
from operator import itemgetter
########################################################################


########################################################################
# import additional python-library
########################################################################
import numpy
from sklearn import metrics
########################################################################


########################################################################
# constant value
########################################################################
# #pAUCの計算用
MAX_FPR = 0.1

# #eval_data_listから機種名の行を調べるため用
CHK_MACHINE_TYPE_LINE = 2

# リストのカラムナンバー
# #eval_data_csvのカラムナンバー
FILENAME_COL = 0
MACHINE_TYPE_COL = 0
Y_TRUE_COL = 2

# #anomaly_score_csvのカラムナンバー
EXTRACTION_ID_COL = 0
SCORE_COL = 1

# 読み込みと出力の設定
# #nomalかanomalyかの情報が入ったCSVの読取用
EVAL_DATA_LIST_PATH = "./eval_data_list.csv"

# #result_<team_name>.csvの出力ディレクトリ
RESULT_DIR = "./teams/"

# #anomaly score csvを格納しているフォルダ群のルートディレクトリ
TEAMS_ROOT_DIR = "./teams/"
########################################################################


########################################################################
# data save in CSV file
########################################################################
def save_csv(save_file_path,
             save_data):
    with open(save_file_path, "w", newline="") as f:
        writer = csv.writer(f, lineterminator='\n')
        writer.writerows(save_data)
########################################################################


########################################################################
# result data output
########################################################################
def output_result(team_dir, machine_types):

    # team_dirのフォルダ名を取得
    dir_name = os.path.basename(team_dir)

    # #AUC,pAUCを出力するファイル名
    result_name = "result_" + dir_name + ".csv"

    # #出力先path
    result_file = "{result_dir}/{result_name}".format(result_dir=RESULT_DIR, result_name=result_name)

    # CSV出力用リストを宣言
    csv_lines = []

    # 機種ごとにAUC、pAUCの算出を行う
    for machine_type in machine_types:

        # 機種名を使ってanomaly_scoreファイル名を取得
        anomaly_score_path_list = sorted(
            glob.glob("{dir}/anomaly_score_{machine_type}_id*".format(dir=team_dir, machine_type=machine_type)))

        # CSV出力用リストへ機種名とタグを追加
        csv_lines.append([machine_type])
        csv_lines.append(["id", "AUC", "pAUC"])

        # AUCとpAUCの平均計算用リストを宣言
        performance = []
        print("=============================================")
        print("MACHINE TYPE IS [{}]".format(machine_type))
        print("---------------------------------------------")

        # idごとのAUC,pAUCの算出
        for anomaly_score_path in anomaly_score_path_list:

            # 各anomaly_scoreファイルの中身をリストへ格納
            with open(anomaly_score_path) as fp:
                anomaly_score_list = list(csv.reader(fp))

                # ファイル名を昇順でソート
                anomaly_score_list_sort = sorted(anomaly_score_list, key=itemgetter(0))

            # idの抽出
            machine_id = re.findall('id_[0-9][0-9]', anomaly_score_path)[EXTRACTION_ID_COL]
            print(machine_id)

            # normalかanomalyの情報格納用
            y_true = []

            # 機種idと機種名を使用してeval_data_listからnormalかanomalyの情報を実数に変換して抽出
            for eval_data in eval_data_list:
                if len(eval_data) < CHK_MACHINE_TYPE_LINE:
                    flag = True if eval_data[MACHINE_TYPE_COL] == machine_type else False
                else:
                    if flag and machine_id in str(eval_data[FILENAME_COL]):
                        y_true.append(float(eval_data[Y_TRUE_COL]))

            # anomaly_scoreを実数に変換して抽出
            y_pred = [float(anomaly_score[SCORE_COL]) for anomaly_score in anomaly_score_list_sort]

            # ここで数が一致していない場合エラー
            if len(y_true) != len(y_pred):
                print("Err:anomaly_score may be missing")
                sys.exit(1)

            # AUCとpAUCの算出を行いid単位で出力用リストへ格納、機種ごとの平均をとるためにリストへ格納
            auc = metrics.roc_auc_score(y_true, y_pred)
            p_auc = metrics.roc_auc_score(y_true, y_pred, max_fpr=MAX_FPR)
            csv_lines.append([machine_id.split("_", 1)[1], auc, p_auc])
            performance.append([auc, p_auc])
            print("AUC :", auc)
            print("pAUC :", p_auc)

        # 平均算出し出力用リストへ格納
        averaged_performance = numpy.mean(numpy.array(performance, dtype=float), axis=0)
        print("\nAUC Average :", averaged_performance[0])
        print("pAUC Average :", averaged_performance[1])
        csv_lines.append(["Average"] + list(averaged_performance))
        csv_lines.append([])

    print("=============================================")
    print("AUC and pAUC results -> {}".format(result_file))
    save_csv(save_file_path=result_file, save_data=csv_lines)
########################################################################


########################################################################
# main evaluator.py
########################################################################
if __name__ == "__main__":

    # teamsディレクトリ内にある複数のチームに対して処理を行う
    teams_dirs = glob.glob("{root_dir}/*".format(root_dir=TEAMS_ROOT_DIR))

    # eval_data_listの読込
    if os.path.exists(EVAL_DATA_LIST_PATH):
        with open(EVAL_DATA_LIST_PATH) as fp:
            eval_data_list = list(csv.reader(fp))
    else:
        print("Err:eval_data_list.csv not found")
        sys.exit(1)

    # 機種名リストを宣言
    machine_types = []

    # 機種名リストにeval_data_listから機種名を格納
    for idx in eval_data_list:
        if len(idx) < CHK_MACHINE_TYPE_LINE:
            machine_types.append(idx[MACHINE_TYPE_COL])

    # team単位で処理を行う
    for team_dir in teams_dirs:
        if os.path.isdir(team_dir):
            output_result(team_dir, machine_types)
        else:
            print("{} is not directory.".format(team_dir))

