import pandas as pd

test_result = pd.read_csv("D:/DNA_methylation/CKD_0.02/csv/DMP_result_TN.csv")
all_beta_data = pd.read_csv("D:/DNA_methylation/CKD_0.02/csv/all_beta_normalized.csv")

filted_data = all_beta_data[all_beta_data['Unnamed: 0'].isin(test_result['Unnamed: 0'])]

filted_data.to_csv("D:/DNA_methylation/CKD_0.02/csv/filted_all_beta_data.csv",index=False)

print("已完成過濾")