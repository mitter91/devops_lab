# !/usr/bin/python3

N = N1 = int(input())
list = []
for i in range(9, 1, -1):
    if N1 <= 9 and N1 == i:
        i -= 1
    else:
        while N % i == 0:
            N /= i
            list.append(i)

if len(list) == 1:
    print(-1)
else:
    list.reverse()
    print(''.join(map(str, list)))
