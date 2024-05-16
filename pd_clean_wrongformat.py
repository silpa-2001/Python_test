import pandas as pd

df = pd.read_csv('datat.csv')

df['Date'] = pd.to_datetime(df['Date'], format='mixed', errors='coerce')

df.dropna(subset=['Date'],inplace=True)
#print(df.to_string())
#df.loc[7,'Duration']=45
#print(df.loc[7])

for x in df.index:
    if df.loc[x,'Duration']>120:
        #df.loc[x,'Duration']=120
        df.drop(x,inplace=True)
print(df.to_string())