# 1209. Remove All Adjacent Duplicates in String II
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        # start stack
        stack = []
        # keep track of how many consecutive symbols in a row
        counts = []
        for i,c in enumerate(s):
            # check if stack is empty and last element is same as current element
            if stack and stack[-1] == c:
                # add current element to stack
                stack.append(c)
                # since elements match, add 1 to counts
                counts.append(counts[-1] + 1)
                # if counts is k, remove the most recent k elements
                if counts[-1] == k:
                    for j in range(k):
                        stack.pop()
                        counts.pop()
            # otherwise, add element and new fresh count
            else:
                stack.append(c)
                counts.append(1)
        # return list as a string
        return "".join(stack)
