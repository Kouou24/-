

import pandas as pd

final_result = pd.read_csv("D:/DNA_methylation/CKD_0.02/csv/new_DMP_result_TN.csv")
df_csv = pd.read_csv("D:/DNA_methylation/CKD_0.02/csv/final_exp.csv")
meta_column = df_csv.iloc[:, 0]
df_csv = df_csv.drop(columns=['Unnamed: 0'])

#print(meta_column)
pd_fin = df_csv.mean(axis=1)
#pd_fin.insert(0, meta_column.name, meta_column)  # 將第 0 列重新插入
pd_fin = pd.concat([meta_column.reset_index(drop=True), pd_fin.reset_index(drop=True)], axis=1)
pd_fin.columns = ["Locus_Name", "Row_Average"]
#print(pd_fin)

filtered_data = final_result[final_result.iloc[:, 0].isin(pd_fin["Locus_Name"])]
print(filtered_data)
filtered_data["N_to_T.deltaBeta"] = pd_fin.set_index("Locus_Name").loc[
    filtered_data["Unnamed: 0"]
]["Row_Average"].values

sorted_data = filtered_data.sort_values(by="N_to_T.deltaBeta", key=abs, ascending=False)
#print(sorted_data)
sorted_data.reset_index(drop=True, inplace=True)
print(sorted_data)
sorted_data.to_csv("D:/DNA_methylation/CKD_0.02/csv/result_match_delta_beta.csv", index=False)


