# 977. Squares of a Sorted Array
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # start and both ends of nums
        left = 0
        right = len(nums) - 1
        ans = []
        while left <= right:
            # calculate which end squared is larger
            a = nums[left] ** 2
            b = nums[right] ** 2
            # add the larger square to ans and adjust pointer
            if a >= b:
                ans.append(a)
                left += 1
            else:
                ans.append(b)
                right -= 1
        # return reverse of pointer because ans is largest to smallest
        return ans[::-1]
