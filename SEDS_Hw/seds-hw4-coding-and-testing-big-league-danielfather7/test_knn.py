def test_dist():
    import knn
    vec1 = [0, 0, 0, 1]
    vec2 = [0, 0, 0, 0]
    assert int(knn.dist(vec1, vec2)) == 1, "Distance calculate not correct."

def test_sortdist():
    import knn
    import pandas as pd
    df = pd.DataFrame([[0,3], [0,1], [0,2]])
    vec = [0,0]
    assert int(knn.sortdist(df,vec)[0][0]) == 1, "Sort not handled properly"
    assert int(knn.sortdist(df,vec)[0][1]) == 1, "Index finding not handled properly."

def test_classify():
    import knn
    import pandas as pd
    df = pd.DataFrame([[0,3,'C'], [0,1,'B'], [0,2,'A']],columns = [1,2,'Type'])
    vec = [0,0]
    assert knn.classify(1,df,vec) == 'B', "Group finding not handled properly."
    assert knn.classify(2,df,vec) == 'B', "Group finding not handled properly."
    assert knn.classify(3,df,vec) == 'B', "Group finding not handled properly."

def test_knn():
    import knn
    import pandas as pd
    df1 = pd.DataFrame([[0,3,'C'], [0,1,'B'], [0,2,'A']],columns = [1,2,'Type'])
    df2 = pd.DataFrame([[0,3.1], [0,1.1], [0,2.1]])
    assert list(knn.knn(df1,df2,1)['Knn Type']) == ['C', 'B', 'A'], "Knn not handled properly."
    assert knn.knn(df1,df2,1).shape[1] == 3, "Column appending not handled properly."

def test_knnac():
    import knn
    import pandas as pd
    df1 = pd.DataFrame([[0,3,'C'], [0,1,'B'], [0,2,'A']],columns = [1,2,'Type'])
    df2 = pd.DataFrame([[0,3.1,'C'], [0,1.1,'B'], [0,2.1,'A']],columns = [1,2,'Type'])
    assert len(knn.knnac(df1,df2,[1,2,3])) == 3, "Maybe miss a calculation of a k value."
    assert knn.knnac(df1,df2,[1,2,3])[1] == '100.0%', "Accuracy not handled properly."
    assert type(knn.knnac(df1,df2,[1,2,3])) == dict, "Dictionary not handled properly"

