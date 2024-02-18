import pandas as pd
import numpy as np

data= {2014:[100.5,150.8,200.9,30000,40000],
       2015:[12000,18000,22000,30000,45000],
       2016:[20000,50000,70000,100000,125000],
       2017:[50000,60000,70000,80000,90000],
       2018:[160000,110000,500000,340000,900000]}
index= ['Madhu','Kusum','Kinshuk','Ankit','Shruti']
sales= pd.DataFrame(data, index=index)
print(sales)
print('\n')

print(sales.index)
print(sales.columns)
print(sales.dtypes)
print(sales.ndim)
print(sales.size)
print(sales.shape)
print(sales.tail(2))
print(sales[[2016,2017]])


print(sales.T)
print(sales[2017])
print(sales.loc[['Madhu','Ankit'],[2017,2018]])
print(sales.loc[['Shruti'],[2016]])

sales.loc['Sumeet']= [196.2,37800,52000,78438,38852]
print(sales)

print(sales.drop(columns= 2014))
print(sales.drop('Kinshuk', axis=0))

sales= sales.rename({'Ankit':'Vivaan','Madhu':'Shailesh'}, axis= 'index')
print(sales)

sales.loc[sales.index== 'Shailesh', 2018]= 100000
print(sales)

# sales.to_csv('D:\personal\mygithub\python-feature-set\com\inbravo\pandas', index= False, header= False)

