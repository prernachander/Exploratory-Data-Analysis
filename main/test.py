# -*- coding: utf-8 -*-
"""
Created on Sat Aug  6 00:45:34 2022

@author: bornf
"""
import lib.FeatureEngineering as fe
import lib.stats as st
import lib.viz as vz

# df = fe.data()
# df = df.data_cleanup('csv')
# df = fe.data(df)
# df = df.data_engineering()

df = vz.viz('data/iris.csv')
print(df.select_options(df))