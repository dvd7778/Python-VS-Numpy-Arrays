import time
import random as rand
import numpy as np
import csv
import statistics

# Maximum and minimum values for number within the arrays
MAX_NUMBER_SIZE = 100001
MIN_NUMBER_SIZE = 1

# Creating Arrays in python
def py_1D_array(size):
    array = []
    for i in range(size):
        array.append(rand.randint(MIN_NUMBER_SIZE, MAX_NUMBER_SIZE))
    return array

def py_2D_array(size):
    # row  = size
    array = []
    for i in range(size):
        array.append(py_1D_array(size))
    return array

# Creating Arrays in numpy
def numpy_1D_array(size):
    return np.random.randint(MIN_NUMBER_SIZE, MAX_NUMBER_SIZE, size)

def numpy_2D_array(size):
    return np.random.randint(MIN_NUMBER_SIZE, MAX_NUMBER_SIZE, size=(size,size))

# Python iterative multiplication
def py_1D_product(arr_A, arr_B):
    sum = 0
    for i in range(len(arr_A)):
        for j in range(len(arr_B)):
            if i == j:
                product = arr_A[i] * arr_B[j]
                sum = sum + product
    return sum

def py_2D_product(arr_A, arr_B):
    arr_C = []
    arr_C = py_2D_array(len(arr_A))
    for i in range(len(arr_A)):
        for j in range(len(arr_B[0])):
            sum = 0
            for k in range(len(arr_A[0])):
                sum = sum + arr_A[i][k] * arr_B[k][j]

            arr_C[i][j] = sum

    return arr_C


def iter_time_1D(array_size, arrays_amount):
    T = 0
    arrays = []
    for i in range(arrays_amount):
        arrays.append(py_1D_array(array_size))

    for i in arrays:
        start = time.time()
        py_1D_product(i,i)
        end = time.time()
        T = T + (end - start)
    avg = T/len(arrays)
    print("Avergae Time calculating the product of 2 1D arrays of", array_size, "elements through iteration:\n", avg)
    return(avg)

def numpy_time_1D(array_size, arrays_amount):
    T = 0
    arrays = []
    for i in range(arrays_amount):
        arrays.append(py_1D_array(array_size))
    for i in arrays:
        start = time.time()
        np.dot(i,i)
        end = time.time()
        T = T + (end - start)
    avg = T/len(arrays)
    print("Avergae Time calculating the product of 2 1D arrays of", array_size, "elements through numpy:\n", avg)
    return(avg)

def iter_time_2D(array_size, arrays_amount):
    T = 0
    arrays = []
    for i in range(arrays_amount):
        arrays.append(py_2D_array(array_size))

    for i in arrays:
        start = time.time()
        py_2D_product(i,i)
        end = time.time()
        T = T + (end - start)
    avg = T/len(arrays)
    print("Avergae Time calculating the product of 2 2D arrays of dimensions", array_size, "x", array_size, "through iteration:\n", avg)
    return(avg)

def numpy_time_2D(array_size, arrays_amount):
    T = 0
    arrays = []
    for i in range(arrays_amount):
        arrays.append(py_2D_array(array_size))

    for i in arrays:
        start = time.time()
        np.dot(i,i)
        end = time.time()
        T = T + (end - start)
    avg = T/len(arrays)
    print("Avergae Time calculating the product of 2 2D arrays of dimensions", array_size, "x", array_size, "through numpy:\n", avg)
    return(avg)


if __name__=='__main__':
    array_size = 5
    arrays_amount = 10

    print("#################\n### 1D ARRAYS ###\n#################")
    array_size = 5
    iter_time_1D(array_size, arrays_amount)
    numpy_time_1D(array_size, arrays_amount)

    array_size = 10
    iter_time_1D(array_size, arrays_amount)
    numpy_time_1D(array_size, arrays_amount)

    array_size = 20
    iter_time_1D(array_size, arrays_amount)
    numpy_time_1D(array_size, arrays_amount)

    array_size = 50
    iter_time_1D(array_size, arrays_amount)
    numpy_time_1D(array_size, arrays_amount)

    array_size = 100
    iter_time_1D(array_size, arrays_amount)
    numpy_time_1D(array_size, arrays_amount)

    array_size = 200
    iter_time_1D(array_size, arrays_amount)
    numpy_time_1D(array_size, arrays_amount)

    array_size = 500
    iter_time_1D(array_size, arrays_amount)
    numpy_time_1D(array_size, arrays_amount)

    array_size = 1000
    iter_time_1D(array_size, arrays_amount)
    numpy_time_1D(array_size, arrays_amount)

    array_size = 2000
    iter_time_1D(array_size, arrays_amount)
    numpy_time_1D(array_size, arrays_amount)

    array_size = 5000
    iter_time_1D(array_size, arrays_amount)
    numpy_time_1D(array_size, arrays_amount)

    array_size = 10000
    iter_time_1D(array_size, arrays_amount)
    numpy_time_1D(array_size, arrays_amount)
    
    print("#################\n### 2D ARRAYS ###\n#################")
    array_size = 5
    iter_time_2D(array_size, arrays_amount)
    numpy_time_2D(array_size, arrays_amount)

    array_size = 10
    iter_time_2D(array_size, arrays_amount)
    numpy_time_2D(array_size, arrays_amount)

    array_size = 20
    iter_time_2D(array_size, arrays_amount)
    numpy_time_2D(array_size, arrays_amount)

    array_size = 50
    iter_time_2D(array_size, arrays_amount)
    numpy_time_2D(array_size, arrays_amount)

    array_size = 100
    iter_time_2D(array_size, arrays_amount)
    numpy_time_2D(array_size, arrays_amount)

    array_size = 200
    iter_time_2D(array_size, arrays_amount)
    numpy_time_2D(array_size, arrays_amount)

    array_size = 500
    iter_time_2D(array_size, arrays_amount)
    numpy_time_2D(array_size, arrays_amount)

    array_size = 1000
    iter_time_2D(array_size, arrays_amount)
    numpy_time_2D(array_size, arrays_amount)

    array_size = 2000
    iter_time_2D(array_size, arrays_amount)
    numpy_time_2D(array_size, arrays_amount)

    array_size = 5000
    iter_time_2D(array_size, arrays_amount)
    numpy_time_2D(array_size, arrays_amount)

    array_size = 10000
    iter_time_2D(array_size, arrays_amount)
    numpy_time_2D(array_size, arrays_amount)