class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        mat3 = []
        for rows in range(len(mat1)):
            a_temp = [0]*len(mat2[0])
            mat3.append(a_temp)

        for m in range(len(mat1)):
            for n in range(len(mat2)):
                if mat1[m][n]:
                    for k in range(len(mat2[0])):
                        mat3[m][k] = mat3[m][k] + mat1[m][n]* mat2[n][k]
        return mat3