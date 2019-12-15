def longestCommomPrefix(ls:list) -> str:
    lprf = ''
    l = len(ls)
    if l == 0:
        return lprf
    for i, ss in enumerate(ls[0]):
        flag = 1
        for j in ls[1:]:
            if ss != j[i] or i > len(j):
                flag = -1
                break
        if flag == 1:
            lprf = lprf + ss
        if flag == -1:
            break
    return lprf

