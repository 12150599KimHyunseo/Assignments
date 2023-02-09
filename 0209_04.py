import random
import time


def select_sort(ary):
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


def quick_sort(ary):
    n = len(ary)
    if n <= 1:
        return ary
    pivot = ary[n//2]
    left_ary, right_ary = [], []
    for num in ary:
        if num < pivot:
            left_ary.append(num)
        elif num > pivot:
            right_ary.append(num)
    return quick_sort(left_ary) + [pivot] + quick_sort(right_ary)


count_ary = [1000, 10000, 12000, 15000]

if __name__ == "__main__":
    for count in count_ary:
        temp_ary = [random.randint(0, 15000) for _ in range(count)]
        select_ary = temp_ary[:]
        quick_ary = temp_ary[:]

        print('## 데이터 수 : ', count, '개')
        start = time.time()
        select_sort(select_ary)
        end = time.time()
        print("	선택 정렬 --> %10.3f 초" % (end - start))
        start = time.time()
        quick_sort(select_ary)
        end = time.time()
        print("	퀵 정렬  --> %10.3f 초" % (end - start))
        print()
