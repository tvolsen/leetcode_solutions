# 18. 4Sum
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        ans = set({})
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                left = j + 1
                right = len(nums) - 1
                if right <= j:
                    continue
                while left < right:
                    val = nums[i] + nums[j] + nums[left] + nums[right]
                    if val == target:
                        ans.add((nums[i],nums[j],nums[left],nums[right]))
                        left += 1
                    elif val > target:
                        right -= 1
                    else:
                        left += 1
        return list(ans)
