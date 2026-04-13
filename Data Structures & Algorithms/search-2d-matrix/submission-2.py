class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # find correct row to check
        possible_row = 0

        i = 0 
        j = len(matrix)
        while i < j:
            m = (i+j) // 2
            if matrix[m][0] == target:
                possible_row = m
                break
            elif matrix[m][0] < target:
                # print("shift left")
                possible_row = max(possible_row,m)
                i = m + 1
            else: 
                # print("shift right")
                j = m

        print(possible_row)

        i = 0 
        j = len(matrix[0])
        
        while i < j :
            m = i+ (j - i) // 2

            if matrix[possible_row][m] ==  target:
                return True
            elif matrix[possible_row][m] <  target:
                i = m + 1
            else:
                j = m

        return False
                
