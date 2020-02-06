##################################################
# python library
import os
import sys
import csv
import glob
import re
import numpy
from sklearn import metrics

###################################################
# constant value
# AUC parameter
MAX_FPR = 0.1
# Check the list with machine type
CHK_MACHINE_TYPE_LINE = 2

# column num of list
# #eval_data_csv
FILENAME_COL = 0
MACHINE_TYPE_COL = 0
Y_TRUE_COL = 2
# #anomaly_score_csv
EXTRACTION_ID_COL = 0
SCORE_COL = 1

# file path
eval_data_list_path = "./eval_data_list.csv"
result_dir = "./result"
result_name = "result.csv"
result_file = "{result_dir}/{result_name}".format(result_dir=result_dir, result_name=result_name)


###################################################
# def
def save_csv(save_file_path,
             save_data):
    with open(save_file_path, "w", newline="") as f:
        writer = csv.writer(f, lineterminator='\n')
        writer.writerows(save_data)


###################################################
# main
if __name__ == "__main__":
    # load csv
    if os.path.exists(eval_data_list_path):
        with open(eval_data_list_path) as fp:
            eval_data_list = list(csv.reader(fp))
    else:
        sys.exit(1)

    machine_types = []
    # create machine type list
    for idx in eval_data_list:
        if len(idx) < CHK_MACHINE_TYPE_LINE:
            machine_types.append(idx[MACHINE_TYPE_COL])

    # set result list
    csv_lines = []
    # create auc p_auc result
    for machine_type in machine_types:
        # get anomaly score for machine type
        anomaly_score_path_list = sorted(glob.glob("{dir}/anomaly_score_{machine_type}_id*".format(dir=result_dir,
                                                                                                   machine_type=machine_type)))
        csv_lines.append([machine_type])
        csv_lines.append(["id", "AUC", "pAUC"])
        performance = []
        print("=============================================")
        print("MACHINE TYPE IS [{}]".format(machine_type))
        print("---------------------------------------------")
        for anomaly_score_path in anomaly_score_path_list:
            with open(anomaly_score_path) as fp:
                anomaly_score_list = list(csv.reader(fp))
            machine_id = re.findall('id_[0-9][0-9]', anomaly_score_path)[EXTRACTION_ID_COL]
            print(machine_id)

            # set id score list
            y_true = []
            # Find y_true with machine_type and machine_id
            for eval_data in eval_data_list:
                if len(eval_data) < CHK_MACHINE_TYPE_LINE:
                    flag = True if eval_data[MACHINE_TYPE_COL] == machine_type else False
                else:
                    if flag and machine_id in str(eval_data[FILENAME_COL]):
                        y_true.append(float(eval_data[Y_TRUE_COL]))
            y_pred = [float(anomaly_score[SCORE_COL]) for anomaly_score in anomaly_score_list]
            auc = metrics.roc_auc_score(y_true, y_pred)
            p_auc = metrics.roc_auc_score(y_true, y_pred, max_fpr=MAX_FPR)
            csv_lines.append([machine_id.split("_", 1)[1], auc, p_auc])
            performance.append([auc, p_auc])
            print("AUC :", auc)
            print("pAUC :", p_auc)
        # create average data
        averaged_performance = numpy.mean(numpy.array(performance, dtype=float), axis=0)
        csv_lines.append(["Average"] + list(averaged_performance))
        csv_lines.append([])
    print("=============================================")
    print("AUC and pAUC results -> {}".format(result_file))
    save_csv(save_file_path=result_file, save_data=csv_lines)
