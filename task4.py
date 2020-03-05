#!/usr/bin/env python


def task4(N):
    N1 = N
    if N < 0:
        raise ValueError('Negative number is not allowed')
    list = []
    for i in range(9, 1, -1):
        if N1 <= 9 and N1 == i:
            i -= 1
        else:
            while N % i == 0:
                N /= i
                list.append(i)
    if len(list) <= 1:
        res = '-1'
    else:
        list.reverse()
        res = ''.join(map(str, list))
    return res


if __name__ == "__main__":
    N = int(input())
    result = task4(N)
    print('\n'.join(map(str, result)))
    result = []
