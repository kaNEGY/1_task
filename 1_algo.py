F = open('A.txt')
M, n = map(int, F.readline().split())
a = [int(F.readline()) for i in range(M)]
ok = [0] * M
for i in range(M - 1):
    ok[i] = (a[i] < 2 * a[i + 1])
tot = 0
for i in range(n):
    tot += ok[i]
res = 0
if tot == n:
    res += 1
for i in range(n, M - 1):
    tot += ok[i]
    tot -= ok[i - n]
    if tot == n:
        res += 1
print(res)
