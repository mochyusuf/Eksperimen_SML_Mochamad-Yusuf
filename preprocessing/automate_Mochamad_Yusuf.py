import pandas as pd
import numpy as np

if __name__ == "__main__":
    input_file = "../covid_19_indonesia_time_series_all_raw.csv"
    output_file = "covid_19_indonesia_time_series_all_clean.csv"
    
    # Read Data
    raw_data = pd.read_csv(input_file)
    
    # Preprocessing
    df = raw_data.drop(columns=[
        'Date','Location ISO Code', 'Location Level','City or Regency', 'Province', 'Country', 'Continent', 'Island', 'Time Zone', 'Special Status',
        'Area (km2)', 'Population', 'Population Density', 'New Cases per Million', 'Total Cases per Million', 'New Deaths per Million',
        'Total Deaths per Million', 'Total Deaths per 100rb', 'Growth Factor of New Cases', 'Growth Factor of New Deaths', 'Case Fatality Rate',
        'Case Recovered Rate', 'Total Regencies', 'Total Cities', 'Total Districts', 'Total Urban Villages', 'Total Rural Villages', 'Longitude', 'Latitude',
        'New Active Cases', 'New Cases', 'New Deaths', 'New Recovered', 'Total Active Cases'
    ])

    df = df.drop(df[df['Location'] == 'Indonesia'].index)

    df.drop_duplicates(inplace=True)

    # Save Data
    raw_data.to_csv(output_file, index=False)