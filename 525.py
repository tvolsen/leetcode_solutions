# 525. Contiguous Array
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        ans = 0
        # replace 0 with -1 and look for 0 sum subarray
        for i in range(len(nums)):
            if nums[i] == 0:
                nums[i] = -1
        prefix = [nums[0]]
        for i in range(1, len(nums)):
            prefix.append(prefix[-1] + nums[i])
        # we have sum 0 at index just before 0, ie right before we start
        seen = {0:-1}
        for i in range(len(prefix)):
            p = prefix[i]
            # here since we are looking for 0, we have p-0 = p
            if p in seen:
                # find the index of the first found occurrence
                j = seen[prefix[i]]
                # replace the ans with longer interval length
                ans = max(ans, i - j)
            # add found sum at first possible index
            if p not in seen:
                seen[p] = i
        return ans
