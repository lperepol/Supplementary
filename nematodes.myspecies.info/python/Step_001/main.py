import pandas as pd
#import xlrd
import openpyxl
import json
from sortedcontainers import SortedList, SortedSet, SortedDict

def read_csv(fn):
    df = pd.read_csv(fn)
    df = df.fillna('Not Specified')
    return df

def fixFileNames(df):
    df['ext'] = ''
    for index, row in df.iterrows():
        FileName = str(row['FileName']).strip()
        FileNameSp = FileName.split('.')
        l= len(FileNameSp)
        if l > 0:
            ext = FileNameSp[l-1]
            if len(ext) < 5 :
                df.loc[index, 'ext'] = ext
    return df

def main():
    fn = "../../Images.txt"
    df = read_csv(fn)
    df = fixFileNames(df)

    fn = "../../ImagesFixed.csv"
    df.to_csv(fn, index=False)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()