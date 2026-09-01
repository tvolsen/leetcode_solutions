# 22. Generate Parentheses
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # store answers
        ans = []
        # recusion function
        def bt(curr, left, right):
            # basecase, ie n open and close parentheses
            if left == n and right == n:
                ans.append(curr)
                return
            # if there are less than n ('s, add another and recurse
            if left < n:
                curr = curr + "("
                bt(curr, left+1, right)
                # remove (
                curr = curr[:-1]
                # you can also replace this block with
                # bt(curr + "(", left+1, right)
            # if there are more ( than ), add ) and recurse
            if right < left:
                curr = curr + ")"
                bt(curr, left, right+1)
                # remove )
                curr = curr[:-1]
                # you can also replace this block with
                # bt(curr + ")", left, right+1)
        # search starting with empty string and left=right=0
        bt("", 0, 0)
        return ans
