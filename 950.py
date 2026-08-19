# 950. Reveal Cards In Increasing Order
class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        from collections import deque
        # sort to get the correct draw order
        drawn = sorted(deck)
        # add the largest card back into deck
        q = deque([drawn.pop()])
        # while cards are still drawn, work backwards
        while drawn:
            # add the bottom of the deck to the top
            q.appendleft(q.pop())
            # add the drawn card to top of deck
            q.appendleft(drawn.pop())            
        # return list of deck order
        return list(q)
