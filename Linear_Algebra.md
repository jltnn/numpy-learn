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
- Vectors are mathematical objects characterised by their magnitude(or length) and direction. We draw vectors as directed line segments(or arrows) in the (x,y)-plane.
- The set of all vectors in thr plane is denoted by R^2
- Vectors in the plane are considered to be floating, and are completely determined by their length and direction, not their position. 
### Algrbraic notation:
- If A=(a1,a2) is a point in the plane, we consider the vector from the origin O=(0,0) to A
- We denote the vector by OA->=[a1,a2] [a1
                                        a2]
- OA-> is the position vector of the point A. The scalars a1 and a2 are the components of )A->
- If A=(a1,a2) and B=(b1,b2) are points, then we consider the vector from A to B. We say that A is the tail and B is the head/tip of the vector. 
- The arrow determines a vector:
AB->=[b1-a1, b2-a2]
which is the displacement vector from A to B
### Vector addition
- Given 2 vectors a~=[a1,a2] and b~=[b1,b2], the sum of a~ and b~ is a~ + b~ = [a1+b1, a2+b2]
- Since a~ + b~ = b~ + a~ --> this is called commutativity
- add component by component (combine 2 movements in space).
    Ex: 
    ```py
        a = np.array([1, 2])
        b = np.array([3, 4])
        print(a + b) #[4 6]
### Scalar multiplication
- The scalar multiple c.a~ is the vector -> c.a~ = [ c.a1, c.a2]
- Geometrically, scaling might stretch, shrink, and/or flip the direction of vectors
- The length of c.a~ is c times the length of a~.
- Special cases:
    1. 1.a~ = a~ and (-1)a~ = -a~ is the negative of a ~
    2. 0.a~ = O~ for all vector a~
- In this case, the vector will just move along the direction of vectors but not change its roots.
### Vector subtraction
- Given by: a~ - b~ = [a1, a2] - [b1, b2] = [a1 - b1, a2 - b2]
- If A=(a1,a2) and B=(b1,b2) are points then we have position vectors
    OA-> = [a1, a2], OB-> = [b1, b2]
and displacement vector:
    AB-> = [b1-a1, b2-a2]
    --> AB-> = OB-> - OA->
### Dot product - Linear combination
- The dot product of vectors u~=[u1,u2,...,un], v~=[v1,v2,...vn] belongs to Rn is the scalar
    u~.v~ = u1.v1 + u2.v2 + ... + un.vn
    *Can not leave out the dot u~v~ makes no sense*
- Ex: Find u~.v~ for u~=[1,3] and v~=[2,-4]
        u~.v~ = 1(2) + 3(-4)
              = 2 - 12
              = -10
- TheoremL Let u~,v~,w~ belong to Rn and c belongs to Rn. Then
    1. u~.v~ = v~.u~
    2. u~.(v~+w~) = u~.v~ + u~.w~
    3. (cu~).v~ = c(u~.v~)
    4. u~.u~ >= 0 and u~.u~ = 0 <=> u~=o~
    5. ||u~|| = sqrt(u~.u~)
    6. |u~.v~| <= ||u~||||v~||
    7. ||u~ + v~|| <= ||u~|| + ||v~||
- Measures how much two vectors "point in the same direction". Returns a single number.
    `np.dot()`
    Ex: 
    ```py
        a = np.array([1, 2])
        b = np.array([3, 4])
        print(np.dot(a, b)) #11 (= 1x3 + 2x4)
        ```
- Linear combination of v-> and w->: a*v-> + b*w-> (in what a and b being calles scalars)
    - The span of v-> and w-> is the set of all their linear combinations (let a and b vary over all real numbers). If the vectors line up, it will 
### Vector length (norm)
- the length of a vector a~ = [ a1,a2,a3,...,an] is: ||a~|| = sqrt(a1^2 + a2^2 +...+an^2)

- the length of a vector - its "magnitude". the pythagorean theorem generalized. 
    `np.linalg.norm()`
    Ex: 
    ```py 
        v = np.array([3, 4])
        length = np.linalg.norm(v)
        print(length) #5 (=sqrt(3^2 + 4^2))
        ```
### Projection:
- The shadown cast one vector onto another one is the projection. It tells "How much of vector A is pointing in the direction of vector B?"
- In ML, projections are being used for:
    1. Dimensionality Reduction (PCA)
    Principle Component Analysis (PCA) is one of the most common ways to simplify huge data sets. It works by projecting high-dimensional data (like a 100-variable spreadsheet) onto a lower-dimensional "best-fit" line or plane
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