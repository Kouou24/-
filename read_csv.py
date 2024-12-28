import pandas as pd

df_csv = pd.read_csv("D:/DNA_methylation/CKD_0.05/csv/DMP_result_TN.csv")
"""
k = ['cg20746451','cg01490296','cg10297223','cg02990553','cg06205244','cg21285133','cg21285782','cg14279121','cg11508872','cg26296769']     
for i in k:
    {
        print(df_csv[df_csv['Unnamed: 0'] == i])
    }

"""
print(df_csv[df_csv['Unnamed: 0'] == 'cg10297223'])
#print(df_csv)