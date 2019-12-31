#
# @lc app=leetcode id=74 lang=python3
#
# [74] Search a 2D Matrix
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix, target: int) -> bool:
        # 法一：直接二分法
        if matrix == []:
            return False
        lr = 0
        lc = 0
        rr = len(matrix) - 1
        rc = len(matrix[0]) - 1
        while rr * len(matrix[0]) + rc >=  lr*len(matrix[0]) + lc:
            mid = (rr*len(matrix[0])+rc + lr * len(matrix[0]) + lc)//2
            midr = mid//len(matrix[0])
            midc = mid % len(matrix[0])
            if matrix[midr][midc] > target:
                rc = midc - 1
                rr = midr
                if rc < 0:
                    rc = len(matrix[0]) - 1
                    rr = rr - 1
            elif matrix[midr][midc] < target:
                lc = midc + 1
                lr = midr
                if lc > len(matrix[0]) - 1:
                    lc = 0
                    lr += 1
            elif matrix[midr][midc] == target:
                return True
        return False

        # 法二：先拼接，再二分法：
        # ls = []
        # if matrix == []:
        #     return False
        # for i in matrix:
        #     ls.extend(i)
        # r = 0
        # l = len(ls) - 1
        # while r <= l:
        #     mid = (r + l) //2
        #     if ls[mid] == target:
        #         return True
        #     if ls[mid] > target:
        #         l = mid - 1
        #     if ls[mid] < target:
        #         r = mid + 1
        
        # return False
        
# @lc code=end
m = [[1,3,5,7],[10,11,16,20],[23,30,34,50]]
s = Solution()
s.searchMatrix(m, 7)