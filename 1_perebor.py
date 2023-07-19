F = open('A.txt')
M, n = map(int, F.readline().split())
a = [int(F.readline()) for i in range(M)]
goods = 0
for i in range(M - n):
    last_el = -1
    k = 0
    for j in a[i:i+n+1]:
        if 2 ** k * j <= last_el:
            break
        last_el = 2 ** k * j
        k += 1
    else:
        goods += 1
print(goods)
