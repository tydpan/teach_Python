import pandas as pd
def datainput(datacsv,testcsv):
    data=pd.read_csv(datacsv)
    test=pd.read_csv(testcsv)
    return data,test
def distance(data,test):
    d = pd.DataFrame()
    for a in range(len(test.index)):
        data[a] = ((data.rWC-test.rWC[a])**2+(data.rCh-test.rCh[a])**2)**0.5
        d = data
    return d
def acck(test,d,k):
    ac = 0
    acc = 0
    i = pd.DataFrame()
    test['pre']='0'
    for a in range(len(test.index)):        
        for ik in reversed(range(1,k+1)):
            i = d.sort_values([a], ascending=True).head(n=ik)
            test.loc[a,'pre'] = pd.value_counts(i['Type']).idxmax()
            if (len(pd.value_counts(i['Type']))) == 1 or (pd.value_counts(i['Type'])[0] > pd.value_counts(i['Type'])[1]):
                break    
        if test.loc[a,'pre'] == test.loc[a,'Type']:
            ac +=1
            acc = ac/len(test.index)
    return test,acc
def knn(datacsv,testcsv,k):
    data,test = datainput('atomsradii.csv','testing.csv')
    d = distance(data,test)
    dic={}
    for ii in range(1,k+1): 
        te,ack = acck(test,d,ii)
        key={ii:ack}
        dic.update(key)
    return te,dic
