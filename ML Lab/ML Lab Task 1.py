# import pandas as pd
# import os

# script_dir = os.path.dirname(__file__) 
# file_path = os.path.join(script_dir, 'cars.csv')

# df_csv = pd.read_csv(file_path)
# print("CSV Data: ")
# print(df_csv.head())

# online_csv_url = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv'

# df_online_csv = pd.read_csv(online_csv_url)
# print("\nOnline CSV Data: ")
# print(df_online_csv.head())


from sklearn import datasets

iris = datasets.load_iris()
print("Features Data - First Five Rows: ")
print(iris.data[:5])

print("\nTarget Data - First Five Rows: ")
print(iris.target[:5])