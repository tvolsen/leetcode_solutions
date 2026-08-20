# 35. Search Insert Position
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # pointer at left end of nums
        left = 0
        # pointer at right end of nums
        right = len(nums) - 1
        # until pointers pass each other, this is 
        while left <= right:
            # take the middle index between the pointers
            mid = (left + right) // 2
            # if the value at this index is target, return index
            if nums[mid] == target:
                return mid
            # if the mid point is larger, need to make search values smaller
            elif nums[mid] > target:
                right = mid - 1
            # otherwise need to make search values larger
            else:
                left = mid + 1
        # return mid because on the last iteration, left == right == mid
        # if nums[mid] > target: 
        #     the target is just before mid, ie, inserted at index mid == left
        # if nums[mid] < target: 
        #     the target is just after mid, since left += 1 here, we return left
        # this is often the hardest part of these problems, which variable to return
        return left 
            
            
