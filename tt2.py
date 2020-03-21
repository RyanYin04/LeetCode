# class Solution:
#     def uniquePathsWithObstacles(self, cols, obstacleGrid) -> int:
#         if cols == 0 or obstacleGrid[0][0] == 'X':
#             return 0
#         obstacleGrid[0][0] = 1
#         rows = len(obstacleGrid)
#         columns = len(obstacleGrid[0])
#         # 遍历第一行：
#         for c in range(1, columns):
#             if obstacleGrid[0][c] == 1 or obstacleGrid[0][c - 1] == 0:
#                 obstacleGrid[0][c] = 0
#             else:
#                 obstacleGrid[0][c] = 1
        
#         # 遍历第一列：
#         for r in range(1, rows):
#             if obstacleGrid[r][0] == 1 or obstacleGrid[r - 1][0] == 0:
#                 obstacleGrid[r][0] = 0
#             else:
#                 obstacleGrid[r][0] = 1
        
#         # 按列-行遍历所有剩余位置：
#         for r in range(1, rows):
#             for c in range(1, columns):
#                 if obstacleGrid[r][c] == 1:
#                     obstacleGrid[r][c] = 0
#                 else:
#                     obstacleGrid[r][c] = obstacleGrid[r-1][c] + obstacleGrid[r][c-1]
#         return obstacleGrid[rows - 1][columns - 1]



# a, b, c = input()

def helper(n, s, L, R):
    c = 0
    if n == 0:
        return 0
    elif n == 1:
        if s < L or s > R:
            return 0
        else:
            return 1
    else:
        for d in range(L, R + 1):
            # print(d)
            c += helper(n - 1, s - d, L, R)
    return c + 1

def ways(n, k, L, R):
    max_sum = R * n
    min_sum = L * n
    count = 0

    for times in range(min_sum//k + 1, max_sum //k + 1 ):
        count += helper(n, times * k, L, R)
    return count

ways(9, 1, 1, 3)


def     gcd(a,b):
        while a!=0:
            a,b = b%a,a
        return b
#定义一个函数，参数分别为a,n，返回值为b
def     findModReverse(a,m):#这个扩展欧几里得算法求模逆

        if gcd(a,m)!=1:
            return None
        u1,u2,u3 = 1,0,a
        v1,v2,v3 = 0,1,m
        while v3!=0:
            q = u3//v3
            v1,v2,v3,u1,u2,u3 = (u1-q*v1),(u2-q*v2),(u3-q*v3),v1,v2,v3
        return u1%m

def shoot(rounds, ps):
    if rounds <= 0:
        return [0, 0, 0]
    if rounds == 1:
        return [ps[0], 1-ps[0], 0]
    else:
        p0 = 1
        p1 = 1
        p2 = 1
        
        p0 = shoot(rounds-1, ps[:rounds-1])[0] * ps[rounds - 1]
        p1 = shoot(rounds - 1, ps[:rounds - 1])[0] * (1 - ps[rounds - 1]) + shoot(rounds - 1, ps[:rounds - 1])[1] * ps[rounds - 1]
        if rounds == 2:
            p2 = shoot(rounds - 1, ps[:rounds - 1])[1] * (1 - ps[rounds - 1])
        elif rounds > 2:
            p2 = shoot(rounds - 1, ps[:rounds - 1])[1] * (1 - ps[rounds - 1]) + shoot(rounds - 1, ps[:rounds - 1])[0] * ps[rounds - 1]
        return [findModReverse(1/p0, 998244353), findModReverse(1/p1,998244353), findModReverse(1/p2, 998244353)]


res = shoot(2, [0.5, 0.5])


print(res)
res