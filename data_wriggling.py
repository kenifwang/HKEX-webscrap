import pandas as pd



data = pd.read_csv('hk_stocks.csv')
data['Stock Code'] = pd.to_numeric(data['Stock Code'], errors='coerce', downcast='integer')
data_sorted = data.sort_values(by='Stock Code', ascending=True).reset_index(drop=True)
data_sorted.to_csv('hk_stocks_sorted.csv', index=False)