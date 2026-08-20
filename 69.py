# 69. Sqrt(x)
class Solution:
    def mySqrt(self, x: int) -> int:
        # for x == 0, x == 1 case
        if x < 2:
            return x
        # these two bounds need to be valid, and beyond all possible answers
        # smallest possible answer, since 0 and 1 case is handled
        left = 2
        # largest possible answer, since the sqrt is less than or equal to x always
        right = x
        while left <= right:
            # find the mid point between the numbers
            mid = (left + right) // 2
            # if found, return the answer
            if mid ** 2 == x:
                return mid
            # if mid^2 is larger than x, we want to search smaller numbers
            elif mid ** 2 > x:
                right = mid - 1
            # if mid^2 is smaller than x, we want to search larger numbers
            else:
                left = mid + 1
        # return RIGHT because on the last iteration, left == right == mid
        # if mid^2 > x: 
        #     mid > sqrt(x), we need to make mid smaller so we return mid-1 == right
        # if mid^2 < x: 
        #     mid < sqrt(x), which means mid is the rounded down value or sqrt(x), so return mid == right
        return right
