# Numpy notes:
## Introduction:
- Numpy as a supercharged list for Python (it’s a library, a toolbox you add to Python) that makes working w numbers much faster and easier
- Why numpy - for faster solution to regular lists:
    Normal Python - u need a loop:
    numbers = [ 1, 2, 3, 4, 5]
    doubled = [ x * 2 for x in numbers]
    --> This is tedious for big data

    Numpy:
    import numpy as np
    numbers np.array([1, 2, 3, 4, 5])
    doubled = numbers * 2 
    Output: [2, 4, 6, 8, 10]
- Core idea: array
    Everything in Numpy revolves around one thing: the array (like a list, but more powerful)

    The 3 Types of Arrays (by shape)
    1D array - vector - a single row of numbers
    2D array - matrix - a table (rows & columns)
    3D array - tensor - a cube/stack of tables
    Ex: one_d = np.array([1, 2, 3])
        two_d = np.array([[1,2], [3,4], [5,6]])
        three_d np.array([[[1,2],[3,4]], [[5,6],[7,8]]])
- Some useful way to use Numpy:
    Math on entire arrays at once
    Ex: a = np.array([1, 2, 3, 4])
        a + 10    --> [11, 12, 13, 14]
        a * 3.    --> [3, 6, 9, 12]
        a ** 2    --> [1, 4, 9, 16]
        np.sqrt(a)--> [1.0, 1.41, 1.73, 2.0]
    Array info
    Ex: a = np. array([[1, 2, 3], [4, 5, 6]])
        a.shape  --> (2,3) (2 rows, 3 columns)
        a.ndim.  --> 2.    (it's 2D)
        a.size.  --> 6.    (ttl num of elements)
        a.dtype. --> int64.(type of data store)
        