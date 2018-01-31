def dist(vec1,vec2):
#Use scipy package to calculate Euclidean distance.
    from scipy.spatial import distance
    return(distance.euclidean(vec1,vec2))

def sortdist(df, vec):
#Use for loop, calculate Eulidean distance between input 1-D array and
#each row in input dataframe.
    distlist = []
    for index, row in df.iterrows():
        distlist.append([dist(row[0:2],vec),index])
#Output is ordered from min to max with its index.
    distlist.sort()
    return(distlist)

def classify(k,df,vec):
    import itertools as it
    countlist = []
    grouplist = []
    gpsorted = []
    makechoice = []
#Choose k numbers of sorted data.
    kdistlist = sortdist(df,vec)[0:k]
#Find out the group it belongs to.
    for i in range(k):
        grouplist.append(df.loc[kdistlist[i][1]]['Type'])
#Use groupby to get numbers of the same group and unduplicated group name.
    gp = sorted(grouplist)
#    print(grouplist)
    for key, group in it.groupby(gp):
        countlist.append(len(list(group)))
        gpsorted.append(key)
#    print(countlist)
#    print(gpsorted)
#Use a if loop to deal with 2 or more max values in countlist.
    if countlist.count(max(countlist))>1:
        for j in range(len(countlist)):
            if countlist[j] == max(countlist):
                makechoice.append(grouplist.index(gpsorted[j]))
#        print(makechoice)
#It will choose the group which appeared ahead in grouplist.
#(In most case, it is the shortest distance among equal numbers of same
#groups.)
        group = grouplist[min(makechoice)]
    else:
        group = gpsorted[countlist.index(max(countlist))]
    return group

def knn(traindf,inputdf,k):
#Wrap all functions and append a column called 'Knn Type'.
    group = []
    for index, row in inputdf.iterrows():
        group.append(classify(k,traindf,row[0:2]))
    inputdf['Knn Type'] = group
    return(inputdf)

def knnac(traindf,inputdf,k):
#Creat a dictionary, and calculate accuracy.
    k_ac = {}
    for i in k:
        n = 0
        for j in range(inputdf.shape[0]):
            if knn(traindf,inputdf,i)['Type'][j] == knn(traindf,inputdf,i)['Knn Type'][j]:
                n += 1
        k_ac[i] = '{0:.1%}'.format(n/inputdf.shape[0])
    return k_ac
