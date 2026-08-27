# 846. Hand of Straights
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hand.sort()
        counts = {}
        for card in hand:
            counts[card] = counts.get(card, 0) + 1
        lows = sorted(list(set(hand)))
        low_idx = 0
        while low_idx < len(lows):
            curr = lows[low_idx]
            if curr not in counts:
                low_idx += 1
                continue
            for i in range(groupSize):
                if curr + i not in counts:
                    return False
                counts[curr + i] -= 1
                if counts[curr + i] == 0:
                    del counts[curr + i]
        return True
