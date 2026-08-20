# 162. Find Peak Element
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            # if value at mid is larger than at mid+1, mid may be peak
            if nums[mid] > nums[mid+1]:
                right = mid
            # otherwise mid cannot be peak, move past it
            else:
                left = mid + 1
            # note this could be rewritten as:
            # if nums[mid] < nums[mid + 1]:
            #     left = mid + 1
            # else:
            #     right = mid
        # return left or right since loop ends on left == right
        return left
