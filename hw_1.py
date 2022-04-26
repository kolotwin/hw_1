import math
import numpy as np
from numpy import dot
from numpy.linalg import norm


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
    distance = dot(a, b)/(norm(a)*norm(b))
    return distance

a = np.random.randint(-10, 10, size=10)
b = np.random.randint(-10, 10, size=10)
print('Euclidean:', cal_euclidean(a, b))
print('Manhattan:', cal_manhattan(a, b))
print('Cosine:', cal_cosine(a, b))


# task №5
my_array = np.random.rand(100)
Z = (my_array - np.min(my_array))/(np.max(my_array)-np.min(my_array))
print('max_array =', np.max(Z), '; min_array =', np.min(Z))
print("array:\n", Z)

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