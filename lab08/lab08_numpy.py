import numpy as np

print('#1')
hours = np.arange(0, 22, 3)
print(hours)
line = np.linspace(0, 1, 5)
print(line)
zeros = np.zeros(6)
print(zeros)
unknown_table = np.array([[-1, -1, -1], [-1, -1, -1]])
print(unknown_table)
identity = np.eye(3)
print(identity)

print('#2')
id_1 = hours[3]
print(id_1)
id_2 = hours[-1]
print(id_2)
id_3 = hours[2:6]
print(id_3)
id_4 = hours[0::2]
print(id_4)
id_5 = hours[::-1]
print(id_5)

print('#3')
temperatures = np.array([
    [12, 14, 13, 15],
    [11, 13, 16, 17],
    [10, 12, 15, 18],
])
print(temperatures.shape)
print(temperatures.ndim) # число измерений
print(temperatures.size) # число элементов
print(temperatures[0]) # первое число - номер строки, второе - номер столбца
print(temperatures[:, -1])
print(temperatures[:2, 1:])
print(temperatures[:2, 1:3])

print('#4')
matrix = np.arange(1, 26).reshape(5, 5)
print(matrix)
print('1)')
print(matrix[:3, :])
print(matrix[:3, :].shape)
print('2)')
print(matrix[-2:, :])
print(matrix[-2:, :].shape)
print('3)')
print(matrix[:, :2])
print(matrix[:, :2].shape)
print('4)')
print(matrix[1:4, 2:5])
print(matrix[1:4, 2:5].shape)
print('5)')
print(matrix[-2:, -2:])
print(matrix[-2:, -2:].shape)

print('#5')

print('1)')
changed_hours = hours.copy() # нужна, чтобы мы не испортили оригинальный объект
print(changed_hours)
changed_hours[2:5] = 99
print(changed_hours)
changed_hours[::2] = -1
print(changed_hours)

print('2)')
changed_matrix = matrix.copy()
print(changed_matrix)
changed_matrix[1, :] = 0
print(changed_matrix)
changed_matrix[:, -1] = -1
print(changed_matrix)
changed_matrix[1:-1, 1:-1] = 100
print(changed_matrix)


print('#6')
numbers = np.arange(0, 12)
table = numbers.reshape(3, 4)
# table = numbers.reshape(5, 3)  требует 15 элементов вместо 12, число которое
# указано в numbers
transposed = table.T

print(numbers.shape)  # (12,)
print(table.shape)  # (3, 4)
print(transposed.shape)  # (4, 3)




