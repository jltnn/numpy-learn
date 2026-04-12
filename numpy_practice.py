import numpy as np

scores = np.array([72, 85, 90, 60, 78, 95, 55, 88])
print("Average:", np.mean(scores))
print("Highest:", np.max(scores))
print("Lowest:", np.min(scores))

passed = scores[scores >= 70]
print("Passing scores:", passed)