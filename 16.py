# 16. 3Sum Closest
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # sort the numbers
        nums.sort()
        # starting ans
        ans = sum(nums[:3])
        for i in range(len(nums)):
            # 2 pointers in subarray right of i
            left = i + 1
            right = len(nums) - 1
            # must be distinct, thus < not <=
            while left < right:
                a = nums[i]
                b = nums[left]
                c = nums[right]
                # if triple is closer to ans, update ans
                if abs(target - ans) > abs(target - (a+b+c)):
                    ans = a+b+c
                # if we exceed target, make sum smaller by moving right pointer
                if a+b+c >= target:
                    right -= 1
                # if we are under target, make sum larger by moving left pointer
                else:
                    left += 1
        return ans
