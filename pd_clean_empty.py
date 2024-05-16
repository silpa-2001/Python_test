import pandas as pd
#removing empty rows
"""
a = pd.read_csv("datat.csv")
x = a.dropna()
print(x.to_string())
#change og dataset
a = pd.read_csv("datat.csv")
x = a.dropna(inplace=True)
print(x.to_string())

#replace with value
a = pd.read_csv("datat.csv")
a.fillna(130,inplace=True)
#replace specified cols with value
a = pd.read_csv("datat.csv")
df.fillna({"Calories": 130}, inplace=True)"""
#replace with mean, meadian, mode
a = pd.read_csv("datat.csv")
x = a["Calories"].mean()
a.fillna({"Calories": x}, inplace=True)
print(a.to_string())

a = pd.read_csv("datat.csv")
x = a["Calories"].median()
a.fillna({"Calories": x}, inplace=True)
print(a.to_string())

a = pd.read_csv("datat.csv")
x = a["Calories"].mode()
a.fillna({"Calories": x}, inplace=True)
print(a.to_string())