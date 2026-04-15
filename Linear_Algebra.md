# Linear Algebra with Python
## VECTORS
- A vector is an ordered list of numbers - like coordinates in space. In 2D it's [x, y], in 3D it's [x, y, z]. Numpy represents these as 1D array
    Ex: import numpy as np
        # A 2D vector (x=3, y=4)
    ```py
        v = np.array([3, 4])
        # A 3D vector
        w = np.array([1, 2, 3])
        print(v)  #[3, 4]
        print(v.shape) (2,)  #2 elements
    ```
### Vector addition
- add component by component (combine 2 movements in space).
    Ex: 
    ```py
        a = np.array([1, 2])
        b = np.array([3, 4])
        print(a + b) #[4 6]
### Dot product
- Measures how much two vectors "point in the same direction". Returns a single number.
    `np.dot()`
    Ex: 
    ```py
        a = np.array([1, 2])
        b = np.array([3, 4])
        print(np.dot(a, b)) #11 (= 1x3 + 2x4)
        ```
### Vector length (norm)
- the length of a vector - its "magnitude". the pythagorean theorem generalized. 
    `np.linalg.norm()`
    Ex: 
    ```py 
        v = np.array([3, 4])
        length = np.linalg.norm(v)
        print(length) #5 (=sqrt(3^2 + 4^2))
        ```
### Unit vector
- Shrink a vector to length 1 while keeping its direction. Useful for "direction only" comparisons.
    `np.linalg.norm()`
    Ex: 
    ```py
    v = np.array([3, 4])
    unit = v / np.linalg.norm(v)
    print(unit) #[0.6 0.8]
    print(np.linalg.norm(unit)) #1.0
## Matrices
- A matrix is a 2D grid of numbers, with rows and columns. A "3x2 matrix" has 3 rows and 2 columns. In Numpy, it's a 2D array.
    Ex:
    ```py
    import numpy as np
    # A 2x3 matrix (2 rows, 3 columns)
    A = np.array([[1, 2, 3], [4, 5, 6]])
    print(A.shape) #(2, 3)
    print(A[0]) #(1 2 3) <- first row
    print(A[:, 1]) #[2 5] <- second column
### Useful Matrix creators
- All zeros: 
`np.zeros((3, 3))`
- All ones:
`np.ones(2, 4)`
- Identity matix (like "1" for matrices)
`np.eye(3)`
#[[1,0,0],[0,1,0],[0,0,1]]
- Random matrix
`np.random.rand(2, 2)`
### Tranpose
- Flip rows and column. A(2x3) matrix becomes (3x2)
Ex: 
```py
    A = np.array([[1, 2, 3], [4, 5, 6]])
    print(A.T)
    #[[1 4]] [2 5] [3 6]]
    print(A.T.shape) #(3, 2)