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

def rename():
    return
    path = "X:/0program/nemtode/general/Supplimenatay_Key_Images/nematodes.myspecies.info/Images"
    count = 1
    for root, dirs, files in os.walk(path):
        for d in dirs :
            dir =  d
            if '%' in d:
                dir = str(d).replace('%', '=')
                os.rename(os.path.join(root, d),os.path.join(root, dir))
            count += 1
        for i in files:
            if '%' in i:
                dir = str(i).replace('%', '=')
                os.rename(os.path.join(root, i),os.path.join(root, dir))
            #os.rename(os.path.join(root, i), os.path.join(root, "changed" + str(count) + ".txt"))
            count += 1




def fixFileNames(df):
    df['ext'] = ''
    path = "X:/0program/nemtode/general/Supplimenatay_Key_Images/nematodes.myspecies.info/Images"
    for index, row in df.iterrows():
        FileName = str(row['FileName']).strip()
        old_name = dir + FileName
        new_name =  old_name
        old_name = "'" + old_name + "'"
        new_name = new_name.replace('%20','-')
        new_name = new_name.replace(' ','-')
        x = 0
        os.rename(old_name, new_name)
    return df

def main():
    fn = "../../ImagesFixed.csv"
    df = read_csv(fn)
    df = fixFileNames(df)

    fn = "../../ImagesFixed_001.csv"
    df.to_csv(fn, index=False)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()