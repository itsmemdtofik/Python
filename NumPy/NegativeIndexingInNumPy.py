# Negative Indexing: Use negative indexing to access an array from the end

import numpy as np

nums = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(f"Last element from 2nd dim: {nums[1, -1]}")
