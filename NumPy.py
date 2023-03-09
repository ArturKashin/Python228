import numpy as np

# ======================================================
# x = [1, 2, 3, 4, 5.5]
# z = [45,45,43,3,4]
#
# y = np.array([x, z], int)
# print(y)
# print(y[0:])
# print(y.shape)

# ======================================================
# array = np.array(range(10), float)
# print(array)
# array = array.reshape((5,2))
# print(array)

# ======================================================
# a = np.array([1, 2, 3, 4, 5], float)
# b = a
# c = a.copy()
# c[0] = 10
# print(a)
# print(b)
# print(c)

# ======================================================
# a = np.array([1, 2, 3, 4, 5], float)
# print(a.tolist())
# print(a)
# print(list(a))

# ======================================================
# a = np.array([1, 2, 3, 4, 5], float)
# s = a.tobytes()
# print(s)
# s = np.frombuffer(s)
# print(s)

# ======================================================
# a = np.array([1, 2, 3, 4, 5], float)
# print(a)
# a.fill(8)
# print(a)

# ======================================================
# a = np.array([1, 2, 3, 4, 5, 6], float).reshape(2, 3)
# print(a)
# print()
# a = a.transpose()
# print(a)

# ======================================================
# a = np.array([[1, 2, 3], [4, 5, 6]], float)
# print(a)
# a = a.flatten()
# print(a)

# ======================================================
# a = np.array([1, 2], float)
# b = np.array([3, 4, 5, 6], float)
# c = np.array([7, 8, 9], float)
# abc = np.concatenate((a, b, c))
# print(abc)

# ======================================================
# a = np.array([1, 2, 3, 4, 5, 6], float)
# print(a)
# print(a[:, np.newaxis])
# print(a[:, np.newaxis].shape)
# b = a[np.newaxis, :]
# print(b)
# a = array([1, 2, 3], float)