# 383. Ransom Note
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # build counters for each str
        note = {}
        mag = {}
        for c in ransomNote:
            note[c] = note.get(c, 0) + 1
        for c in magazine:
            mag[c] = mag.get(c, 0) + 1
        for k,v in note.items():
            # if a letter is not in mag, return false
            if k not in mag:
                return False
            # if a letter appears more than in mag, return false
            if v > mag[k]:
                return False
        return True
