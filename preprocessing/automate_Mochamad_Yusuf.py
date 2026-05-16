import pandas as pd
import numpy as np

if __name__ == "__main__":
    input_file = "../DATA RUMAH.xlsx"
    output_file = "data_rumah_preprocessing.csv"
    
    # Read Data
    raw_data = pd.read_excel(input_file, sheet_name='Sheet1')
    
    # Preprocessing
    df = raw_data.drop(columns=[
        'NO','NAMA RUMAH'
    ])

    df.rename(columns={'LB': 'Luas Bangunan', 
                   'LT': 'Luas Tanah', 
                   'KT': 'Kamar Tidur', 
                   'KM': 'Kamar Mandi', 
                   'GRS': 'Garasi', }, inplace=True)

    df = df.dropna()
    
    df = df.drop_duplicates()

    # Save Data
    df.to_csv(output_file, index=False)