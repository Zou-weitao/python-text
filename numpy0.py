import numpy as np
a = np.array([
    [1, 12, 3],
    [1, 3, 4]
])
# print(a.ndim)
# print(a.shape)
# print(a.size)

b = np.eye(3)
# print(b)

c = np.ones_like(a)
# print(c)
# np.where(t<10, 0, 10) #三元运算符 小于10 为0 大于10 为10
# np.clip(10, 18)小于10 为10 ，大于18 为18 其他值不变
# np.vstack(t1, t2) 竖直拼接 上下拼接
# np.hstack(t1, t2) 水平拼接 左右拼接
t = np.sqrt(a)
print(t)
np.savetxt('a.csv', a, fmt='%d', delimiter=',')