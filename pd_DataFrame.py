import pandas as pd

a={
    "calories":[120,230,580],
    "duration":[12,23,45]
}

x=pd.DataFrame(a,index=[1,2,3])
print(x.loc[[1,2]])