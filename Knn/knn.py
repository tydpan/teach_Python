import pandas as pd
def datainput(datacsv,testcsv):
    data_fram = pd.read_csv(datacsv)
    test_fram = pd.read_csv(testcsv)
    return data_fram,test_fram
def distance(data_fram,test_fram):
    for a in range(len(test_fram.index)):
        data_fram[a] = ((data_fram.rWC-test_fram.rWC[a])**2+(data_fram.rCh-test_fram.rCh[a])**2)**0.5
    return data_fram
def accuracy (test_fram,data_fram,k):
    ac = 0
    acpercentage = 0
    data_fram_sort = pd.DataFrame()
    test_fram['pre'] = '0'
    for a in range(len(test_fram.index)):        
        for ik in reversed(range(1, k+1)):
            data_fram_sort = data_fram.sort_values([a], ascending=True).head(n=ik)
            if (len(pd.value_counts(data_fram_sort['Type']))) == 1 or (pd.value_counts(data_fram_sort['Type'])[0] > pd.value_counts(data_fram_sort['Type'])[1]):
                test_fram.loc[a,'pre'] = pd.value_counts(data_fram_sort['Type']).idxmax()   
                break
        if test_fram.loc[a,'pre'] == test_fram.loc[a,'Type']:
            ac += 1
            acpercentage = ac/len(test_fram.index)
    return test_fram,acpercentage


def knn(datacsv,testcsv,k):
    data,test = datainput('atomsradii.csv','testing.csv')
    data_fram = distance(data,test)
    accuracy_dic = {}
    for ii in range(1,k+1): 
        test_pred,ack = accuracy(test,data_fram,ii)
        key = {ii:ack}
        accuracy_dic.update(key)
    return test,accuracy_dic
