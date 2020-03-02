# !/usr/bin/python3

N = int(input())
M = []
for i in range(N):
    M.append((input()).split())

length = len(M)
d1 = int(0)
d2 = int(0)
for i in range(N):
    d1 += int(M[i][i])
    d2 += int(M[i][N - i - 1])

print(abs(d1 - d2))
