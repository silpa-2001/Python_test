import pandas as pd

"""a=["qwerty","asdf","zxcvb"]
var=pd.Series(a,index=['a','b','c'])
print(var.loc['b'])"""

s={
    "day1":123,
    "day2":567,
    "day3":789
}

var=pd.Series(s,index=["day1","day2"])
print(var)