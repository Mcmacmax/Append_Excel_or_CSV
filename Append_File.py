import pandas as pd
import numpy as np
import glob
import csv
'''
#EXCEL
Path = 'D:/LAB/Append Excel/'
In_Path = Path+"Input/*.xlsx"
out_path =  Path+"Output/Output.xlsx"
count = 0
for xlsx in glob.glob(In_Path, recursive=True): 
    print(count)
    if count == 0: #Header
        data_In= pd.read_excel(xlsx)
        dfobj1 = pd.DataFrame(data_In)
        ColName = list(dfobj1.columns.values)
        dfout = dfobj1
        dfobj = pd.DataFrame([],columns=ColName)
    else :
        #data_In= pd.read_csv(xlsx,header=None,skiprows=1)
        data_In= pd.read_excel(xlsx)
        dfobj = pd.DataFrame(data_In,columns=ColName)   
    #print(dfobj)
    #print(dfout)
    dfout = dfout.append(dfobj,ignore_index=True)
    print(dfout)
    count +=1
    
dfout.to_excel(out_path)

'''

#CSV
Path = 'D:/LAB/Append Excel/'
In_Path = Path+"Input/*.csv"
out_path =  Path+"Output/Output.csv"
count = 0
for xlsx in glob.glob(In_Path, recursive=True): 
    print(count)
    if count == 0:
        data_In= pd.read_csv(xlsx)
        dfobj1 = pd.DataFrame(data_In)
        ColName = list(dfobj1.columns.values)
        dfout = dfobj1
        dfobj = pd.DataFrame([],columns=ColName)
    else :
        #data_In= pd.read_csv(xlsx,header=None,skiprows=1)
        data_In= pd.read_csv(xlsx)
        dfobj = pd.DataFrame(data_In,columns=ColName)   
    #print(dfobj)
    #print(dfout)
    dfout = dfout.append(dfobj,ignore_index=True)
    print(dfout)
    count +=1
    
dfout.to_csv(out_path)
