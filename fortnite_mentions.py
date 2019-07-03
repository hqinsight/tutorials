# Copyright 2019 HQ Insight Ltd.
# https://www.hqinsight.com/
#
# Fortnite Mentions - Earnings Conference Call Transcripts

import os
import pandas as pd
from datetime import datetime

path_to_index = 'C:/PATH_TO_INDEX.TXT/'
os.chdir(path_to_index)

df = pd.read_csv('index.txt', sep='|', header=0, index_col=0)

total_rows = len(df)
df_final = pd.DataFrame(columns=df.columns)

for file_index, row in df[df['reporting_year'] >= 2017].iterrows():
    with open('transcripts/'+str(file_index)+'.txt', 'r') as f:
        if 'fortnite' in f.read().lower():
            df_final = df_final.append(df.loc[file_index])

    if file_index % 1000 == 0:
        print(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + ' - '+str(file_index)+'/'+str(total_rows))

print('Done!')

print(len(df_final))

print(df_final['stock_symbol'].value_counts())

df_final['long_name'] = df_final['stock_symbol'] + ' - ' + df_final['stock_name']
print(df_final['long_name'].value_counts())

df_final[df_final['stock_symbol']=='EA'][['reporting_year', 'reporting_quarter']]
