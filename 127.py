# 127. Word Ladder
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        from collections import deque
        wordList = set(wordList)
        q = deque([(beginWord, 1)])
        seen = set()
        while q:
            v,d = q.popleft()        
            if v == endWord:
                return d
            seen.add(v)
            for ch in "abcdefghijklmnopqrtusvwxyz":
                for i in range(len(beginWord)):
                    new_word = v[:i] + ch + v[i+1:]
                    if new_word in wordList:
                        if new_word == endWord:
                            return d+1
                        if new_word not in seen:
                            q.append((new_word, d+1))
                            seen.add(new_word)
        return 0
