import pandas as pd

def remove_outliers(row):
    q1 = row.quantile(0.25)  # 第 25 百分位數 (Q1)
    q3 = row.quantile(0.75)  # 第 75 百分位數 (Q3)
    iqr = q3 - q1            # 四分位距 (IQR)
    lower_bound = q1 - 1.5 * iqr  # 下界
    upper_bound = q3 + 1.5 * iqr  # 上界
    return row.where((row >= lower_bound) & (row <= upper_bound), other=pd.NA)

# 讀取數據
data = pd.read_csv("D:/DNA_methylation/CKD_0.02/csv/half_all_beta_data.csv")

# 劃分控制組和實驗組
meta_column = data.iloc[:, 0]
standard = data.iloc[0].count()//2+1
control_data = data.iloc[:, 1:standard]
experimental_data = data.iloc[:,standard:]

#print(standard)
#print(control_data)
#print(experimental_data)
"""
# 去除控制組的離群值
remove_outliers_control = control_data.apply(remove_outliers, axis=1) 
csv_out = pd.concat([meta_column.reset_index(drop=True), remove_outliers_control.reset_index(drop=True)], axis=1)
csv_out.to_csv("D:/DNA_methylation/CKD_0.02/csv/no_outlier_control.csv", index=False)

# 去除實驗組的離群值
remove_outliers_experimental = experimental_data.apply(remove_outliers, axis=1)
csv_out = pd.concat([meta_column.reset_index(drop=True), remove_outliers_experimental.reset_index(drop=True)], axis=1)
csv_out.to_csv("D:/DNA_methylation/CKD_0.02/csv/no_outlier_exp.csv", index=False)

#print(remove_outliers_control)
#print(remove_outliers_experimental)
"""
# 計算控制組的行平均值（忽略 NaN）
remove_outliers_control = pd.read_csv("D:/DNA_methylation/CKD_0.02/csv/no_outlier_control.csv")
remove_outliers_experimental = pd.read_csv("D:/DNA_methylation/CKD_0.02/csv/no_outlier_exp.csv")
remove_outliers_control = remove_outliers_control.drop(columns=['Unnamed: 0'])
remove_outliers_experimental = remove_outliers_experimental.drop(columns=['Unnamed: 0'])



control_means = remove_outliers_control.mean(axis=1)

#print(control_means)

# 實驗組數據減去控制組平均值
last_experimental = remove_outliers_experimental.sub(control_means, axis=0)

# 將結果保存到 CSV 並打印
final_exp = last_experimental.apply(remove_outliers, axis=1)
csv_out = pd.concat([meta_column.reset_index(drop=True), final_exp], axis=1)
csv_out.to_csv("D:/DNA_methylation/CKD_0.02/csv/final_exp.csv", index=False)
#print(control_means)
#print(last_experimental)
