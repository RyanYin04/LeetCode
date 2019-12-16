def longestCommonPrefix(ls:list) -> str:
    lprf = ''
    l = len(ls)
    if l == 0:
        return lprf
    for i, ss in enumerate(ls[0]):
        flag = 1
        for j in ls[1:]:
            if i > len(j) - 1 or ss != j[i]:
                flag = -1
                break
        if flag == 1:
            lprf = lprf + ss
        if flag == -1:
            break
    return lprf