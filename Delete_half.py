import pandas as pd

data = pd.read_csv("D:/DNA_methylation/CKD_0.02/csv/filted_all_beta_data.csv")

filtered_data = pd.concat([data.iloc[:, [0]], data.iloc[:, 1::2]], axis=1)

filtered_data.to_csv("D:/DNA_methylation/CKD_0.02/csv/half_all_beta_data.csv",index=False)

print("已成功刪除偶數欄位！")