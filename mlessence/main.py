from scipy import sparse

a = sparse.lil_matrix((4, 5))
a[0, 1] = 1
a[0, 3] = 2
a[2, 2] = 3
a[3, 4] = 4
print(a.toarray())
