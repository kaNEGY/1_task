F = open('B_2.txt')
n, k = map(int, F.readline().split())
c = [int(F.readline()) for i in range(n)]
last = [-1] * k
max_step = [0] * k
max2_step = [0] * k

for i in range(n):
    step = i - last[c[i] - 1]
    if step > max_step[c[i] - 1]:
        max2_step[c[i] - 1] = max_step[c[i] - 1]
        max_step[c[i] - 1] = step
    elif step > max2_step[c[i] - 1]:
        max2_step[c[i] - 1] = step
    last[c[i] - 1] = i

for i in range(k):
    step = n - last[i]
    if step > max_step[i]:
        max2_step[i] = max_step[i]
        max_step[i] = step
    elif step > max2_step[i]:
        max2_step[i] = step

ans = 10 ** 10
for i in range(k):
    ans = min(ans, max((max_step[i] + 1) // 2, max2_step[i]))

print(ans - 1)
