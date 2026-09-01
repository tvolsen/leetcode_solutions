# 90. Subsets II
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = set()
        def bt(curr, i):
            if i == len(nums):
                ans.add(curr)
                return
            # add an element to the subset
            curr = curr + tuple([nums[i]])
            bt(curr, i+1)
            curr = curr[:-1]
            # skip the element in the subset
            bt(curr, i+1)
        bt(tuple([]), 0)
        return [list(x) for x in ans]
