# 46. Permutations
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        # recursion function
        def bt(curr):
            # basecase for recursion
            if len(curr) == len(nums):
                ans.append(curr[:])
                return
            # try all possible options
            for n in nums:
                # this is O(1) based on the problem, if we didnt have 
                # that restriction we could pass a seen set to check in O(1)
                if n not in curr:
                    # add option to curr
                    curr.append(n)
                    # dive into recursion
                    bt(curr)
                    # remove option from curr
                    curr.pop()
        # call bt to populate ans
        bt([])
        # return ans
        return ans
