import numpy as np
import pandas as pd

# train_data = pd.read_table(r'E:\Users\yzmz1314\Dropbox\Python\GitHub\Python3\djangoProject\sales\data.txt',iterator=True,header=None)
#
# while True:
#     try:
#         chunk = train_data.get_chunk(5600000)
#         chunk.columns = ['time','side','qty','symbol','px','exchange','class','description','tags','local_time','source','orderID','exchangeOID','fillID','strategy','ilink','px_multiplier','multiplier','trader-owner','OC']
#         chunk.to_csv('big_data111.csv', mode='a',header=False,index = None)
#     except Exception as e:
#         break
# #
# data_txt = np.loadtxt(r'E:\Users\yzmz1314\Dropbox\Python\GitHub\Python3\djangoProject\sales\fill.cme.UTV2X3.20210113', encoding='utf-8', dtype=str)
# data_txtDF = pd.DataFrame(data_txt)
# data_txtDF.to_csv('datas_train.csv', index=False)

# data = pd.read_csv(r'E:\Users\yzmz1314\Dropbox\Python\GitHub\Python3\djangoProject\sales\fill.cme.UTV2X3.20210113')
# data.to_csv('datatest.csv', index=False)
# print(data)


import csv


with open(r'E:\Users\yzmz1314\Dropbox\Python\GitHub\Python3\djangoProject\sales\data\data.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, dialect='excel')
    with open(r'E:\Users\yzmz1314\Dropbox\Python\GitHub\Python3\djangoProject\sales\data\fill.cme.UTV2X3.20210113', 'r') as filein:
        for line in filein:
            line_list = line.strip('\n').split('\n')
            for colum in line_list:
                columtxt = colum.strip('\n').split('\t')
                spamwriter.writerow(columtxt)
#     filein.close()
# csvfile.close()
