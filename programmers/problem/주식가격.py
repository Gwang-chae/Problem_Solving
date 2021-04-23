from collections import deque

def solution(prices):
    answer = []
    # prices 리스트를 que에 담음
    price_in_que = deque(prices)
    
    while price_in_que:
        # popleft로 que 앞쪽부터 빼가면서
        # 언제 주식가격이 떨어지는지 확인
        now_price = price_in_que.popleft()
        time = 0

        for price_que in price_in_que:
            time += 1
            # now_price보다 작은 원소를 만난 순간이
            # 주식가격이 떨어진 때 
            if now_price > price_que:
                break
        answer.append(time)
    
    return answer