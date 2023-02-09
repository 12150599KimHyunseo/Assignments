def sort(ary):
    n = len(ary)
    for i in range(0, n-1):
        min_idx = i
        for k in range(i+1, n):
            if ary[min_idx] > ary[k]:
                min_idx = k
        tmp = ary[i]
        ary[i] = ary[min_idx]
        ary[min_idx] = tmp

    return ary


ary2 = [[55, 33, 250, 44],
        [88,  1,  67, 23],
        [199, 222, 38, 47],
        [155, 145, 20, 99]]
ary1 = []

for i in range(len(ary2)):
    for k in range(len(ary2[i])):
        ary1.append(ary2[i][k])

print('1차원 변경 후, 정렬 전 --> ', ary1)
print('1차원 변경 후, 정렬 후 --> ', sort(ary1))
print('중앙값 --> ', sort(ary1)[len(ary1)//2])
