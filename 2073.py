# 2073. Time Needed to Buy Tickets
class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        # import and build q
        from collections import deque
        q = deque([])
        # need to keep track of index and remaining ticket counter
        for i,n in enumerate(tickets):
            q.append([i,n])
        time = 0
        while q:
            # store index and count of tickets left
            i,remaining_tickets = q.popleft()
            # if index is k and only 1 ticket left to buy, buy it and return ans
            if i == k and remaining_tickets == 1:
                return time + 1
            # if more than 1 ticket, add it to back of q
            if remaining_tickets > 1:
                q.append([i, remaining_tickets-1])
            # increment number of iterations
            time += 1
