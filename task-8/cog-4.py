#Question-4
import pandas as pd
#Convert the first character of each element in a series to uppercase
ser = pd.Series(['amrita', 'school', 'of', 'engineering', 'chennai', 'campus'])
for i in ser:
    x = i
    y= x.capitalize()
    print(y , end = " ")