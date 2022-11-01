import os
import pandas as pd
import numpy as np
import requests

# Pandas Quiz
'''
## Question 1
What is the result of the following code?
'''
# import pandas as pd

df = pd.DataFrame(np.random.randn(5, 3), columns=['col1', 'col2', 'col3'])
print(f'Qn1. \n{df.apply(lambda x: x.max() - x.min())}')

'''

A. col1    1.0
    col2    1.0
    col3    1.0
    dtype: float64

B. col1    1.0
    col2    1.0
    col3    1.0
    dtype: float64

C. col1    1.0
    col2    1.0
    col3    1.0
    dtype: float64

D. col1    1.0
    col2    1.0
    col3    1.0
    dtype: float64

'''



'''
## Question 2
Download a csv file from https://stats.govt.nz/assets/Uploads/Business-employment-data/Business-employment-data-June-2022-quarter/Download-data/business-employment-data-june-2022-quarter-csv.zip and load it into a pandas dataframe. How many rows and columns are there?
'''
from io import BytesIO
from urllib.request import urlopen
from zipfile import ZipFile

url = 'https://stats.govt.nz/assets/Uploads/Business-employment-data/Business-employment-data-June-2022-quarter/Download-data/business-employment-data-june-2022-quarter-csv.zip'

#download and extract zip
with urlopen(url) as zipdownloader:
    with ZipFile(BytesIO(zipdownloader.read())) as downloadedZip:
        downloadedZip.extractall(os.path.curdir)

#iterate and get csv name
for filename in os.listdir('.'):
    if filename.endswith('.csv'):
        fileName = filename

#load the file into a pandas dataframe
df = pd.read_csv(fileName)
rows = len(df)
columns = len(df.columns)
print(f'\nQtn2. The dataframe has {rows} rows and {columns} columns ')




'''
## Question 3
What method can be used to get the number of non-NA values in a pandas dataframe?

A. `df.count()`

B. `df.na_count()`

C. `df.na_values()`

D. `df.na_count()`
'''
print('\nQtn3: Answer is A. The count() function returns number of non -Na values in a dataframe')
'''



## Question 4
Create a dataframe with 10 rows and 3 columns, where the values are random numbers between 1 and 10 (inclusive). Then, replace all values greater than 5 with the value 10.
'''
df = pd.DataFrame(np.random.randint(1,11,size=(10, 3)))
print(f'\nQtn4. Dataframe before replaceing values is \n {df}')
#using apply method loop through the dataframe with lambda while setting value of y to 10 else shd remain same
df2 = df.apply(lambda x: [y if y <= 5 else 10 for y in x])
print(f'\nDataframe after replacing values is \n{df2}')
'''




## Question 5
create a dataframe from this link https://jsonplaceholder.typicode.com/albums
'''
# print(requests.get('https://jsonplaceholder.typicode.com/albums').json())
df_albums = pd.DataFrame(requests.get('https://jsonplaceholder.typicode.com/albums').json())
print(f'Qtn5. Dataframe from URL is \n{df_albums}')