def score_sort(ary):
    n = len(ary)
    for i in range(0, n-1):
        min_idx = i
        for k in range(i+1, n):
            if ary[min_idx][1] > ary[k][1]:
                min_idx = k
        tmp = ary[i]
        ary[i] = ary[min_idx]
        ary[min_idx] = tmp

    return ary


score_ary = [['선미', 88], ['초아', 99], ['화사', 71], ['영탁', 78], ['영웅', 67], ['민호', 92]]

if __name__ == "__main__":
    print('정렬 전 --> ', score_ary)
    print('정렬 후 --> ', score_sort(score_ary))
    print('## 성적별 조 편성표 ##')
    for i in range(len(score_ary)//2):
        print(score_sort(score_ary)[i][0], ':', score_sort(score_ary)[len(score_ary)-i-1][0])