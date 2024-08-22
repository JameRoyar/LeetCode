# 73.
# 矩阵置零
# 已解答
# 中等
# 相关标签
# 相关企业
# 提示
# 给定一个
# m
# x
# n
# 的矩阵，如果一个元素为
# 0 ，则将其所在行和列的所有元素都设为
# 0 。请使用
# 原地
# 算法。
#
#
#
# 示例
# 1：
#
#
# 输入：matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
# 输出：[[1, 0, 1], [0, 0, 0], [1, 0, 1]]
# 示例
# 2：
#
#
# 输入：matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
# 输出：[[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]

class Solution:
    def setZeroes(self, matrix) -> None:
        m,n = len(matrix),len(matrix[0])
        #define the first line and fisrt column if cointain 0
        line_zero = column_zero = False
        for i in range(m):
            if matrix[i][0] == 0:
                column_zero = True
                break
        for j in range(n):
            if  matrix[0][j] == 0:
                line_zero = True
                break
        #scan the matrix and set the first line and first column if contain 0
        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0
        #set the first line and first column if contain 0
        for i in range(1,m):
                for j in range(1,n):
                    if matrix[i][0] == 0 or matrix[0][j] == 0:
                        matrix[i][j] = 0

        #set the first line and first column if contain 0
        if line_zero:
            for i in range(m):
                matrix[i][0] = 0
        if column_zero:
            for j in range(n):
                matrix[0][j] = 0

