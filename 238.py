# 238. Product of Array Except Self
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # build the forward prefix
        prefix_forward = [nums[0]]
        for i in range(1, len(nums)):
            prefix_forward.append(prefix_forward[-1] * nums[i])
        # reverse nums
        nums = nums[::-1]
        # build the backward prefix (suffix)
        prefix_backward = [nums[0]]
        for i in range(1, len(nums)):
            prefix_backward.append(prefix_backward[-1] * nums[i])
        # reverse suffix
        prefix_backward = prefix_backward[::-1]
        # add 1 as the default value to the left of 0
        prefix_forward = [1] + prefix_forward
        # add 1 as the default value to the right of len(nums)
        prefix_backward.append(1)
        ans = []
        for i in range(len(nums)):
            # multiply these values together
            ans.append(prefix_forward[i] * prefix_backward[i+1])
        return ans
