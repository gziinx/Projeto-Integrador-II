import pandas as pd

df_bronze = pd.read_csv('history.csv')
print(df_bronze.head())
print(df_bronze.head())
print(df_bronze.describe())
print(df_bronze.isnull().sum())

df_bronze.to_csv('t_history_ing.csv', index=False)