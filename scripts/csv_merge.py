import pandas as pd

def merge_csvs (csv_file_path_list: list, result_file_path: str):
    
    df = pd.read_csv(csv_file_path_list[0])

    for i in range(1, len(csv_file_path_list)):
        df = df.merge(pd.read_csv(csv_file_path_list[i]), how='outer', on='Date')

    df.to_csv(result_file_path, index=False)

    
file_list =  []

result_file = ""

merge_csvs(file_list, result_file)
