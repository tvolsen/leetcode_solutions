# 205. Isomorphic Strings
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapping = {}
        if len(s) != len(t):
            return False
        for i,c in enumerate(s):
            if c not in mapping:
                if t[i] in mapping.values():
                    return False
                mapping[c] = t[i]
            else:
                if mapping[c] != t[i]:
                    return False
        return True
