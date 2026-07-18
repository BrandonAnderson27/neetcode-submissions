class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) -1
        
        while l <= r:
            m = ( l + r ) // 2
            if target >= matrix[m][0] and target <= matrix[m][-1]:
                lr, rr = 0, len(matrix[m]) - 1

                while lr <= rr:
                    mr = (lr + rr) // 2
                    if target == matrix[m][mr]:
                        return True

                    if target < matrix[m][mr]:
                        rr = mr - 1

                    elif target > matrix[m][mr]:
                        lr = mr + 1
                return False

            elif target > matrix[m][-1]:
                l = m + 1
            elif target < matrix[m][0]:
                r = m - 1

        return False