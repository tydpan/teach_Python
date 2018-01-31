import numpy as np
import pandas as pd

def pairwise_correlation(df):
    print("data:")
    print(df,"\n\nP value:")
    metrix = pd.DataFrame()
    labels=[]
    for index, row in df.iterrows():
        labels.append('row'+str(index+1))
        for index2, row2 in df.iterrows():
            P = np.corrcoef(row.tolist(), row2.tolist())[0,1]
            print("P value of row%d and row%d is %.2f." %(index+1,index2+1,P))
            metrix.loc[index,index2] = P
    metrix.columns = labels
    metrix.index = labels
    print("\nTable for P values:")
    print(metrix)
    return metrix

def corr_rowi_rowj(df,i,j):
    print("data:")
    print(df,"\n\nP value:")
    P = np.corrcoef(df.iloc[i-1].tolist(), df.iloc[j-1].tolist())[0,1]
    print("P value of row%d and row%d is %.2f." %(i,j,P))
    return P

def corr_rowi_vs_all1(df):
    print("data:")
    print(df,"\n\nP value:")
    metrix = pd.DataFrame()
    labels = []
    for index, row in df.iterrows():
        labels.append('row'+str(index+1))
        for index2, row2 in df.iterrows():
            if index==index2:
                metrix.loc[index,index] = "P=1"
            else:
                P = np.corrcoef(row.tolist(), row2.tolist())[0,1]
                print("P value of row%d and row%d is %.2f." %(index+1,index2+1,P))
                metrix.loc[index, index2] = P
    metrix.columns = labels
    metrix.index = labels
    print("\nTables for P values:")
    print(metrix)
    return metrix

def corr_rowi_vs_all2(df,i):
    print("data:")
    print(df,"\n\nP value:")
    metrix = pd.DataFrame()
    labels = []
    for index, row in df.iterrows():
        labels.append('row'+str(index+1))
        if (index+1)==i:
            metrix.loc[index,index] = "P=1"
        else:
            P = np.corrcoef(df.iloc[i-1].tolist(), row.tolist())[0,1]
            metrix.loc[i-1,index] = P
            print("P value of row%d and row%d is %.2f." %(i,index+1,P))       
    metrix.columns = labels
    metrix.index = ["row"+str(i)]
    print("\nTable for P values:")
    print(metrix)
    return metrix
