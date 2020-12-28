import pandas as pd

data = pd.read_csv("C:/Users/14254/Documents/Tableau DataSets/NYC Accidents 2020.csv")

data["BOROUGH"].fillna('N/A', inplace = True)
data["ZIP CODE"].fillna('N/A', inplace = True)
data["VEHICLE TYPE CODE 1"].fillna('Unspecified', inplace = True)
data["VEHICLE TYPE CODE 2"].fillna('None', inplace = True)
data["CONTRIBUTING FACTOR VEHICLE 2"].fillna('Unspecified', inplace = True)
data["ON STREET NAME"].fillna('Unspecified', inplace = True)
data["CONTRIBUTING FACTOR VEHICLE 2"].fillna('Unspecified', inplace = True)

df=data
df.to_csv("C:/Users/14254/Documents/Tableau DataSets/NYC_Accidents_2020_2.csv")
