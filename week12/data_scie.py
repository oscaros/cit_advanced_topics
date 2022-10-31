# Numpy Array Quiz
from random import random
import numpy as np
import statistics as st
import pandas as pd

## Question 1
'''
What is the result of the following code?

```python
    import numpy as np
    a = np.array([1, 2, 3])
    b = np.array([4, 5, 6])
    c = a + b
    print(c)
```
'''
print(f'Qtn.1: Answer is {[579] }')
print("numpy will sum each of  the columns and return a single array containing the sum of columns")

## Question 2
'''
Create a numpy array of 10 zeros. and reshape it to (2, 5)
'''
# TenZeros = np.array([i*0 for i in range(10)])
TenZeros = np.zeros(10)
print(f'\nQtn.2: {TenZeros.reshape(2,5)}')

## Question 3
'''
Find Mean, Mode, Median, Standard Deviation of the following data

```python
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
```
'''
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
num_data_arr = np.array(data)
mean = num_data_arr.mean()
mode = st.mode(num_data_arr.flatten())
median = np.median(num_data_arr)
std_dev = st.stdev(num_data_arr)

print(f'\nQtn.3: Mean is {mean}, Mode is {mode}, median is {median}, and Standard Deviation is {std_dev}')


## Question 4
'''
create a 6x6 numpy array with random values and find the min and max values
'''
num_arr = np.random.randint(0, 9, (6,6))
# num_arr = np.random.random((6,6))
# print(num_arr.shape)
print(f'\nQtn.4: Original random 6x6 array is {num_arr} \nits min value is {num_arr.min()} and max value is {num_arr.max()}')

## Question 5
'''
create a 3D numpy array and reshape it to 2D
'''
num_three_D = np.array([[[1,2,3], [4,5,6]], [[7,8,9], [10,11,12]]]).reshape(6,2)
print(f'\nQtn.5: new 2D array is {num_three_D}')

## Question 6
'''
create 1D array from this data

```python
    data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
```
'''
data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(f'\nQtn.6: 1D array is {np.array(data).flatten()}')