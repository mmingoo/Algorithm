import sys, heapq
input = sys.stdin.readline

card_num , n = map(int, input().split())

heap = []
cards = [int(x) for x in input().split()]

for card in cards:
    heapq.heappush(heap, card)

for _ in range(n):
    card1 = heapq.heappop(heap)
    card2 = heapq.heappop(heap)

    heapq.heappush(heap, card1+card2)
    heapq.heappush(heap, card1 + card2)

print(sum(heap))
