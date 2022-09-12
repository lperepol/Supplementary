import pandas as pd
#import xlrd
import openpyxl
import json
from sortedcontainers import SortedList, SortedSet, SortedDict
import os

def read_csv(fn):
    df = pd.read_csv(fn)
    df = df.fillna('Not Specified')
    return df

def add_Column(df):
    df['Join'] = ''
    for index, row in df.iterrows():
        FileName = str(row['FileName']).strip()
        FileNameSp = FileName.split('/')
        df.loc[index, 'Join'] = str(FileNameSp[0]).strip()
    return df




def main():
    fn = "./ImagesFixed.csv"
    df = read_csv(fn)
    df = add_Column(df)
    fn = "./ImagesFixed_001.csv"
    df.to_csv(fn, index=False)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()