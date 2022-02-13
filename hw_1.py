import math
import numpy as np
import scipy.spatial.distance as ds

# task №1
def share_bread(N, K):
    x = K//N
    y = K%N
    return x, y

assert share_bread(N=3, K=14) == (4, 2)



# task №2
def leap_year(year):
    text_result = ""
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        text_result = "YOU SHALL PASS"
    else:
        text_result = "YOU SHALL NOT PASS"
    return text_result

assert leap_year(5) == 'YOU SHALL NOT PASS'



# task №3
def amulet_area(a, b, c):
    p = (a+b+c)/2;
    S = math.sqrt(p*(p-a)*(p-b)*(p-c))
    return S

assert amulet_area(3, 4, 5) == 6



# task №4
def cal_euclidean(a, b):
    square = np.square(a - b)
    sum_square = np.sum(square)
    distance = np.sqrt(sum_square)
    return distance

def cal_manhattan(a, b):
    abs_1 = np.abs(a - b)
    distance = np.sum(abs_1)
    return distance

def cal_cosine(a, b):
    distance = ds.cosine(a, b)
    return distance


a = np.random.randint(-10, 10, size=10)
b = np.random.randint(-10, 10, size=10)
print(cal_euclidean(a, b))
print(cal_manhattan(a, b))
print(cal_cosine(a, b))



# task №5
my_array = np.random.randint(0, 2, size=100)
print(np.max(my_array), np.min(my_array))
print(my_array)

my_array = np.random.randint(0, 51, size=(5,6))
selected_column = my_array[:, np.argmax(my_array.max(axis=0))]
print('Shape:\n',my_array)
print('Array')
print(np.max(my_array))
print(selected_column)

def get_unique_rows(X):
    X_unique = np.unique(X, axis=0)
    return X_unique
X = np.random.randint(4, 6, size=(10,3))
print(X)
print(get_unique_rows(X))