import copy
A = [1, 2, [3, 4, 5], 6]
print(id(A))  # 4563404232

print('id of elements in A:', [
    id(i) for i in A
])  # id of elements in A: [4339573248, 4339573280, 4355775304, 4339573408]

print('------------------------------')

B = A[:]  # 浅拷贝
print(id(B))  # 4341880200
print(A is B)  # False
print(A[1] is B[1])  # True

A[0] = 'huang'
A[2][2] = 100

print(id(A), id(B))

print(A, B)  # 因为B是A的一份引用，所以当修改A[0]的值的时候，B不会收到影响。

print('id of elements in A', [id(i) for i in A])
print('id of elements in B', [id(i) for i in B])

C = copy.deepcopy(A)  # 深拷贝
print(id(C))  # 4483827080
print(A is C)  # False
print(A[2] is C[2])  # False
