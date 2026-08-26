# 433. Minimum Genetic Mutation
class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        from collections import deque
        bank = set(bank)
        seen = set()
        q = deque([(startGene, 0)])
        while q:
            v, dist = q.popleft()
            seen.add(v)
            for ch in "ACGT":
                for i in range(len(v)):
                    mutation = v[:i] + ch + v[i+1:]
                    if mutation in bank:
                        if mutation == endGene:
                            return dist + 1
                        if mutation not in seen:
                            q.append((mutation, dist+1))
                            seen.add(mutation)
        return -1
