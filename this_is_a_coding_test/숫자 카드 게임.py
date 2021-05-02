n,m = map(int,input().split())
cards_min = []
for tmp in range(n):
    cards = list(map(int,input().split()))
    cards_min.append(min(cards))

answer = max(cards_min)
print(answer)