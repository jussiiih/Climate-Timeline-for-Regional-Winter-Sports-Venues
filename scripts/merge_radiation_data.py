import pandas as pd

def merge_radiation_data (csv_file: str, radiation_data_file_path: str, result_file_path: str):
    
    df = pd.read_csv(csv_file)
    radiation_data = pd.read_csv(radiation_data_file_path)
    radiation_data.drop_duplicates(subset='Date',inplace=True, ignore_index=True)
    
    df = df.merge(radiation_data, how='left', on='Date')

    df.to_csv(result_file_path, index=False)

    
file = "C:\\Code\\Miniproject 2\\combined data\\peuramaa.csv"
radiation_file = "C:\\Code\Miniproject 2\\data_per_variable\\radiation\\fin_radiation_variable.csv"
result_file = "C:\\Users\\Jussi\\OneDrive - Brights\\Desktop\\New folder\\add_radiation_data\\peuramaa.csv"
merge_radiation_data(file, radiation_file, result_file)


file = "C:\\Code\\Miniproject 2\\combined data\\pyha.csv"
radiation_file = "C:\\Code\Miniproject 2\\data_per_variable\\radiation\\fin_radiation_variable.csv"
result_file = "C:\\Users\\Jussi\\OneDrive - Brights\\Desktop\\New folder\\add_radiation_data\\pyha.csv"
merge_radiation_data(file, radiation_file, result_file)

file = "C:\\Code\\Miniproject 2\\combined data\\himos.csv"
radiation_file = "C:\\Code\Miniproject 2\\data_per_variable\\radiation\\fin_radiation_variable.csv"
result_file = "C:\\Users\\Jussi\\OneDrive - Brights\\Desktop\\New folder\\add_radiation_data\\himos.csv"
merge_radiation_data(file, radiation_file, result_file)

file = "C:\\Code\\Miniproject 2\\combined data\\koli.csv"
radiation_file = "C:\\Code\Miniproject 2\\data_per_variable\\radiation\\fin_radiation_variable.csv"
result_file = "C:\\Users\\Jussi\\OneDrive - Brights\\Desktop\\New folder\\add_radiation_data\\koli.csv"
merge_radiation_data(file, radiation_file, result_file)

file = "C:\\Code\\Miniproject 2\\combined data\\levi.csv"
radiation_file = "C:\\Code\Miniproject 2\\data_per_variable\\radiation\\fin_radiation_variable.csv"
result_file = "C:\\Users\\Jussi\\OneDrive - Brights\\Desktop\\New folder\\add_radiation_data\\levi.csv"
merge_radiation_data(file, radiation_file, result_file)

file = "C:\\Code\\Miniproject 2\\combined data\\messila.csv"
radiation_file = "C:\\Code\Miniproject 2\\data_per_variable\\radiation\\fin_radiation_variable.csv"
result_file = "C:\\Users\\Jussi\\OneDrive - Brights\\Desktop\\New folder\\add_radiation_data\\messila.csv"
merge_radiation_data(file, radiation_file, result_file)

file = "C:\\Code\\Miniproject 2\\combined data\\ruka.csv"
radiation_file = "C:\\Code\Miniproject 2\\data_per_variable\\radiation\\fin_radiation_variable.csv"
result_file = "C:\\Users\\Jussi\\OneDrive - Brights\\Desktop\\New folder\\add_radiation_data\\ruka.csv"
merge_radiation_data(file, radiation_file, result_file)

file = "C:\\Code\\Miniproject 2\\combined data\\saariselka.csv"
radiation_file = "C:\\Code\Miniproject 2\\data_per_variable\\radiation\\fin_radiation_variable.csv"
result_file = "C:\\Users\\Jussi\\OneDrive - Brights\\Desktop\\New folder\\add_radiation_data\\saariselka.csv"
merge_radiation_data(file, radiation_file, result_file)

file = "C:\\Code\\Miniproject 2\\combined data\\tahko.csv"
radiation_file = "C:\\Code\Miniproject 2\\data_per_variable\\radiation\\fin_radiation_variable.csv"
result_file = "C:\\Users\\Jussi\\OneDrive - Brights\\Desktop\\New folder\\add_radiation_data\\tahko.csv"
merge_radiation_data(file, radiation_file, result_file)

file = "C:\\Code\\Miniproject 2\\combined data\\vuokatti.csv"
radiation_file = "C:\\Code\Miniproject 2\\data_per_variable\\radiation\\fin_radiation_variable.csv"
result_file = "C:\\Users\\Jussi\\OneDrive - Brights\\Desktop\\New folder\\add_radiation_data\\vuokatti.csv"
merge_radiation_data(file, radiation_file, result_file)