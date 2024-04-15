import pandas as pd

def csv_add_coordinates(csv_file_path, result_file_path, latitude, longitude):
    df = pd.read_csv(csv_file_path)
    df['latitude'] = latitude
    df['longitude'] = longitude

    df.to_csv(result_file_path, index=False)