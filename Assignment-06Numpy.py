import time
import numpy as np


python_list = list(range(1000000))


numpy_array = np.arange(1000000)

# Python list operation
start = time.time()
result_list = [x * 2 for x in python_list]
end = time.time()
print("Python List Time:", end - start)

# NumPy array operation
start = time.time()
result_array = numpy_array * 2
end = time.time()
print("NumPy Array Time:", end - start)