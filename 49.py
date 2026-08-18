# 49. Group Anagrams
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # note, two strings are anagrams if sorted values are equal
        # previously seen strings, keyed by sorted value
        seen = {}
        ans = []
        for s in strs:
            # casts to list and sorts
            x = sorted(s)
            # casts back to sorted str
            x = "".join(x)
            # if you have not seen sorted value, add to dict as list
            if x not in seen:
                seen[x] = [s]
            # otherwise append it 
            else:   
                seen[x].append(s)
        # create list of lists from dict values
        for v in seen.values():
            ans.append(v)
        return ans
