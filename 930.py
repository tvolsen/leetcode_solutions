# 930. Binary Subarrays With Sum
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        # construct the prefix array
        prefix = [nums[0]]
        for i in range(1, len(nums)):
            prefix.append(prefix[-1] + nums[i])
        # starting, there is 1 way to have 0 sum, the empty array
        counts = {0:1}
        ans = 0
        # loop over prefix
        for i in range(len(prefix)):
            # we are looking for p[i] - p[j-1] = goal
            # solving for this we get p[i] - goal = p[j-1] (earlier term)
            # hence we need to look up p[i] - goal in counts 
            if prefix[i] - goal in counts:
                ans += counts[prefix[i] - goal]
            # add the current prefix value to counts, to later look up as the j above
            counts[prefix[i]] = counts.get(prefix[i], 0) + 1  
        return ans
