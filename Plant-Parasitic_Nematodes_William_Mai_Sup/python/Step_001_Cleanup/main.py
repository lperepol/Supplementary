import pandas as pd
import openpyxl
import xml.etree.ElementTree as ET
import xmltodict
import os
import unicodedata

#def test():
#    f = open("../../../Identification_keys_redo/BoldSystems/Bold_data/BoldSystems.csv", "r")
#    f.write("Now the file has more content!")
#    f.close()
#    for index, row in df.iterrows():
#        #ImgIndex = str(row['ImageIndex']).strip()
#        #df.loc[index, 'ImageIndex'] = ImgIndex
#        #count = count + 1

def read_excel(fn, sheet):
    df = pd.read_excel(fn, sheet_name=sheet)
    df = df.fillna('Not Specified')
    return df

def remove_control_characters(s):
    return "".join(ch for ch in s if unicodedata.category(ch)[0]!="C")

def fix_up(df):
    df = df.replace(r'\\n', ' ', regex=True)
    imageCount = 13514
    for index, row in df.iterrows():
        ImageIndex = f'ImageIndex_{imageCount:05d}'
        df.loc[index, 'image_index'] = ImageIndex
        identification_method = str(row['identification_method']).strip().replace("\n", " ")
        df.loc[index, 'identification_method'] = identification_method
        phylum = str(row['phylum']).strip().replace("\n", " ")
        df.loc[index, 'phylum'] = phylum
        class1 = str(row['class']).strip().replace("\n", " ")
        df.loc[index, 'class'] = class1
        order = str(row['order']).strip().replace("\n", " ")
        df.loc[index, 'order'] = order
        family = str(row['family']).strip().replace("\n", " ")
        df.loc[index, 'family'] = family
        genus = str(row['genus']).strip().replace("\n", " ")
        df.loc[index, 'genus'] = genus
        species = str(row['species']).strip().replace("\n", " ")
        df.loc[index, 'species'] = species
        sex = str(row['sex']).strip().replace("\n", " ")
        df.loc[index, 'sex'] = sex
        lifestage = str(row['lifestage']).strip().replace("\n", " ")
        df.loc[index, 'lifestage'] = lifestage
        caption = str(row['caption']).strip().replace("\n", " ")
        df.loc[index, 'caption'] = caption
        media_descriptor = str(row['media_descriptor']).strip().replace("\n", " ")
        df.loc[index, 'media_descriptor'] = media_descriptor
        diagnostic_descriptor = str(row['diagnostic_descriptor']).strip().replace("\n", " ")
        df.loc[index, 'diagnostic_descriptor'] = diagnostic_descriptor
        image_file = str(row['image_file']).strip().replace("\n", " ")
        df.loc[index, 'image_file'] = image_file
        copyright_institution = str(row['copyright_institution']).strip().replace("\n", " ")
        df.loc[index, 'copyright_institution'] = copyright_institution
        photographer = str(row['photographer']).strip().replace("\n", " ")
        df.loc[index, 'photographer'] = photographer
        source = str(row['source']).strip().replace("\n", " ")
        df.loc[index, 'source'] = source
        scientific_name_accepted = str(row['scientific_name_accepted']).strip().replace("\n", " ")
        df.loc[index, 'scientific_name_accepted'] = scientific_name_accepted
        scientific_name = str(row['scientific_name']).strip().replace("\n", " ")
        df.loc[index, 'scientific_name'] = scientific_name
        citation = str(row['citation']).strip().replace("\n", " ")
        df.loc[index, 'citation'] = citation
        common_name = str(row['common_name']).strip().replace("\n", " ")
        df.loc[index, 'common_name'] = common_name

        imageCount = imageCount +1
    fn = '../../MasterMetadata_001_fixed.csv'
    df = df.fillna('Not Specified')
    df.to_csv(fn, encoding='utf-8', index=False)


def main():
    #fn = '../The_MasterMetadata_001.xlsx'
    #master_df = read_excel(fn,'Sheet1')
    fn = '../../MasterMetadata_001.xlsx'
    fixing_df = read_excel(fn,'Sheet1')
    fix_up(fixing_df)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()