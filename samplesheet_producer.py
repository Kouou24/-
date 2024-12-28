
import csv
import os

os.chdir("D:/DNA_methylation/CKD/data")
idx = 0

with open('Sample_sheet.csv','w',newline='') as f:
    writer = csv.writer(f,delimiter=',',quotechar='|',quoting=csv.QUOTE_MINIMAL)
    writer.writerow(['[header]'])
    writer.writerow(['Investigator'])
    writer.writerow(['Project Name','DNA Methylation 850k'])
    writer.writerow(['Experiment'])
    writer.writerow(['Date'])
    writer.writerow([''])
    writer.writerow(['[Data]'])
    writer.writerow(['Sample_Name','Sample_Plate','Sample_Group','Pool_ID','Sentrix_ID','Sentrix_Position'])

    for item in os.listdir():
        newData = item.split('_')
        if len(newData)>3:
            if (int(newData[0][-1])+int(newData[0][-2])*10+int(newData[0][-3])*100 >= 640):
                idx = idx + 1
                writer.writerow([idx,'','C','',newData[1],newData[2]])
    for item in os.listdir():
        newData = item.split('_')
        if len(newData)>3:
            if (int(newData[0][-1])+int(newData[0][-2])*10+int(newData[0][-3])*100 < 640):
                idx = idx + 1
                writer.writerow([idx,'','E','',newData[1],newData[2]])

