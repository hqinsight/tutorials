# Copyright 2019 HQ Insight Ltd.
# https://www.hqinsight.com/
#
# Word Count - Earnings Conference Call Transcripts

import os
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer

path_to_index = 'C:/PATH_TO_INDEX.TXT/'
os.chdir(path_to_index)

df = pd.read_csv('index.txt', sep='|', header=0, index_col=0)
print(df.dtypes)

amzn_2018 = df[(df['stock_symbol']=='AMZN') & (df['reporting_year']==2018)].index.to_list()
print(amzn_2018)

texts = []
for file_index in amzn_2018:
    with open('transcripts/'+str(file_index)+'.txt', 'r') as f:
        texts.append(f.read())

cv = CountVectorizer(stop_words='english')   
cv_fit=cv.fit_transform(texts)    
word_list = cv.get_feature_names();    
count_list = cv_fit.toarray().sum(axis=0)    

df_words = pd.DataFrame({'word':word_list, 'count':count_list}).sort_values(by=['count'], ascending=False).reset_index(drop=True)
df_words.head(10)
