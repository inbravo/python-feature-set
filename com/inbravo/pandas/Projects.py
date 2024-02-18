import pandas as pd
import numpy as np

alphabets= pd.Series(['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'])
print(alphabets)

vowels= pd.Series(['a','e','i','o','u'],
                  index= ['a','e','i','o','u'])
print(vowels)

friends= pd.Series([1,2,3,4,5],
                   index= ['aarav','aniket','arihant','aviraat','rudra'])
print(friends)

mtseries= pd.Series()
print(mtseries.empty)

array1= np.array([1,2,3,4,5,6,7,8,9,10,11,12])
monthsdays= pd.Series(array1,
                      index=['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec'])
print(monthsdays)

alphabets.index= ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
print(alphabets)

vowels[:]=10
print(vowels/2)

vowels1= pd.Series([2,5,6,3,8],
                   index= ['a','e','i','o','u'])
print(vowels1)
vowels2= vowels1+vowels
print((vowels2))

print(vowels-vowels1)
print(vowels*vowels1)
print(vowels+vowels1)
print(vowels/vowels1)

vowels.index= ['A','E','I','O','U']
print(vowels)

print('size of the series alphabets is', alphabets.size)
print('dimensions of the series alphabets is', alphabets.ndim)
print('values of the series alphabets is', alphabets.values)

mtseries= mtseries.rename('seriesempty')
print(mtseries)

friends.index.name= 'fname'
print(friends)

monthsdays.index.name= 'monthno'
print(monthsdays)

print(friends['aniket'])
print(friends['aarav'])

print(alphabets[4:16])
print(alphabets.head(10))
print(alphabets.tail(10))

print(mtseries)

print(monthsdays[0:7])
print(monthsdays[::-1])