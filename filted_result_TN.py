import pandas as pd

data = pd.read_csv("D:/DNA_methylation/CKD_0.02/csv/DMP_result_TN.csv")
selected_columns = ['Unnamed: 0', 'N_to_T.adj.P.Val', 'N_to_T.gene', 'N_to_T.feat.cgi', 'N_to_T.UCSC_Islands_Name']
filtered_data = data[selected_columns]
filtered_data.to_csv("D:/DNA_methylation/CKD_0.02/csv/new_DMP_result_TN.csv",index=False)
print("result_TN 已經過濾")
#print(filtered_data)