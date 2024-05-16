import pandas as pd

x=pd.read_csv('datat.csv')
#print(x.duplicated())
x.drop_duplicates(inplace=True)
print(x.to_string())