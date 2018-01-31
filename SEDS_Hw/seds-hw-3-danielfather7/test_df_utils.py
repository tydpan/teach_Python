import df_utils as du
import pandas as pd

def test_pairwise_correlation():
    df = pd.DataFrame([[-1, 0, 1], [1, 0, -1], [.5, 0, .5]])
    assert int(du.pairwise_correlation(df).iloc[0,0]) == 1, "Diagonal elements not handled properly"
    assert int(du.pairwise_correlation(df).iloc[0,1]) == -1, "Anticorrelated elements not handled properly"
    assert int(du.pairwise_correlation(df).iloc[0,2]) == 0, "Uncorrelated elements not handled properly"
    assert int(du.pairwise_correlation(df).iloc[1,2]) == int(du.pairwise_correlation(df).iloc[2,1]), "Data not appended properly"
    return

def test_corr_rowi_rowj():
    df = pd.DataFrame([[-1, 0, 1], [1, 0, -1], [.5, 0, .5]])
    assert int(du.corr_rowi_rowj(df,1,1)) == 1, "Diagonal elements not handled properly"
    assert int(du.corr_rowi_rowj(df,1,2)) == -1, "Anticorrelated elements not handled properly"
    assert int(du.corr_rowi_rowj(df,1,3)) == 0, "Uncorrelated elements not handled properly"
    return

def test_corr_rowi_vs_all1():
    df = pd.DataFrame([[-1, 0, 1], [1, 0, -1], [.5, 0, .5]])
    assert type(du.corr_rowi_vs_all1(df).iloc[0,0]) == str, "Diagonal elements not handled properly"
    assert int(du.corr_rowi_vs_all1(df).iloc[0,1]) == -1, "Anticorrelated elements not handled properly"
    assert int(du.corr_rowi_vs_all1(df).iloc[0,2]) == 0, "Uncorrelated elements not handled properly"
    assert int(du.corr_rowi_vs_all1(df).iloc[1,2]) == int(du.corr_rowi_vs_all1(df).iloc[2,1]), "Data not appended properly"
    return

def test_corr_rowi_vs_all2():
    df = pd.DataFrame([[-1, 0, 1], [1, 0, -1], [.5, 0, .5]])
    assert type(du.corr_rowi_vs_all2(df,2).iloc[0,1]) == str, "Diagonal elements not handled properly"
    assert int(du.corr_rowi_vs_all2(df,2).iloc[0,0]) == -1, "Anticorrelated elements not handled properly"
    assert int(du.corr_rowi_vs_all2(df,2).iloc[0,2]) == 0, "Uncorrelated elements not handled properly"
    return
