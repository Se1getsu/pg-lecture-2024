import numpy as np

a = np.array([[1, 2], [3, 4]])

# a = np.array([
#     [1, 2],
#     [3, 4]
# ])

print(a + a.T)  # 和　転置
print(np.dot(a, a))  # a @ a ドット積
# linear algebra (リニア アルジブラ 線形代数)
print(np.linalg.inv(a))  # 逆行列
