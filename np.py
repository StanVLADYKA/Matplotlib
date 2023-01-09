import numpy as np




python_list = [1, 2, 3, 4, 5, 6]
numpy_array = np.array(python_list)

print(type(numpy_array))
print(numpy_array)

test = np.arange(1,20)
print(test)

matrix = np.eye(6)
print(matrix)

matrix2 = np.random.randint(0,20,(4,6))
print(matrix2)
print(type(matrix2))