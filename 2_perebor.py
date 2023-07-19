F = open('A_2.txt')
n, k = map(int, F.readline().split())
c = [int(F.readline()) for i in range(n)]
answers = []
for i in range(len(c)): 
    for j in range(-1, len(c)): 
        for k in range(1, k + 1):
            c1 = c.copy()
            if j != -1:
                c1[j] = k
            steps_left = i
            step = -1
            flg = True
            while step < len(c): 
                    step += 1
                    if step == len(c):
                        break
                    if c1[step] == k:
                        steps_left = i
                    else:
                        steps_left -= 1
                    if steps_left < 0:
                        flg = False
                        break
            if flg:
                print(i)
                break
        if flg:
            break
    if flg:
        break
