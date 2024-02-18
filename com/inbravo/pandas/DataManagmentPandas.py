import pandas as pd
import numpy as np
series1= pd.Series([10,20,30])
print(series1)

series2= pd.Series(['kavi','shyam','ravi'],
                   index= [1,2,3])
print(series2)

series3= pd.Series([2,3,4],
                   index= ['jan','feb','mar'])
print(series3)

array1= np.array([1,2,3,4])
series4= pd.Series(array1)
print(series4)

series5= pd.Series(array1, index= ['jan','feb','mar','apr'])
print(series5)

dict1= {'india':'new delhi','uk':'london','japan':'tokyo'}
series6= pd.Series(dict1)
print(series6)

series7= pd.Series([10,20,30,40,50])
print(series7[0])

series8= pd.Series([1,2,3,4],
                   index= ['january','feburary','march','april'])
print(series8['january'])
print(series6['india'])

series6.index= [1,2,3]
print(series6)

series9= pd.Series(['delhi','washingtondc','paris','tokyo'],
                   index= ['india','usa','france','japan'])
print(series9['india':'france'])
print(series9[::-1])

