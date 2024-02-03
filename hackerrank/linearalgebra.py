import numpy as np


n = int(input())
arr = np.array([input().split() for _ in range(n)], dtype=float)
print(np.round((np.linalg.det(arr)), decimals=2))