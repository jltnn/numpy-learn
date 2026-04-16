import numpy as np
A = np.array([[1, 2, 3], [4, 5, 6]])
print(A.T)
print(A.T.shape) 

#Challenge: Imagine a line on the floow (X-axis). There is a drone hovering at a point in the air. We want to find the perpendicular height of that drone directly above the line
#The line direction(b): [1, 0, 0] (Points straight along the X-axis)
#The drone's position(a): [3, 4, 0] (It's 3 units "down" the line and 4 units "away" from it)

drone = np.array([3, 4, 0])
line_dir = np.array([1, 0, 0])
#Find the projection of drone onto line_dir
dot_product = np.dot(drone, line_dir)
projection = dot_product * line_dir
#Normally we need to divide dot_product to magnitude of line_dir but since it is a unit vector(=1) we skip that step
height_vector = drone - projection
#Actual distance
distance = np.linalg.norm(height_vector)
print(f"The drone is {distance} units away from the line.")

def cosine_similarity(v1, v2):
        dot_prod = np.dot(v1, v2)
        mag1 = np.linalg.norm(v1)
        mag2 = np.linalg.norm(v2)
        return dot_prod / (mag1 *mag2)
    
user = np.array([5, 4, 0])
    #Suppose user likes action(5), sci-fi(4), Romance(0)
movie_a = np.array([4, 5, 1])
    #Suppose move a is ation/sci-fi
movie_b = np.array([0, 1, 5])
print(cosine_similarity(user, movie_a))
print(cosine_similarity(user, movie_b))