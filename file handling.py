Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> import pandas as pd
>>>  df = pd.read_csv("C:/Users/Sushanth/OneDrive/Documents/Desktop/python/prog5.csv.csv"
...                   
SyntaxError: unexpected indent
>>> df = pd.read_csv("C:/Users/Sushanth/OneDrive/Documents/Desktop/python/prog5.csv.csv")
...                   
>>> print(df)
...                   
   YearsExperience
0              1.1
1              1.3
2              1.5
3              2.0
4              2.2
5              2.9
6              3.0
7              3.2
8              3.2
>>>  print(df.shape)
...                   
SyntaxError: unexpected indent
>>> print(df.shape)
...                   
(9, 1)
>>> 
>>> print(len(df))
...                   
9
>>> print(df.head(2))
...                   
   YearsExperience
0              1.1
1              1.3
