# J’s code challenge Engineering in Japan

def make_grid(k):
    top = []
    bottom = []
    for i in range(2*k):
        if i <= (k-1):
            row = [True] * k
            # print(row)
            top.append(row)
        else:
            row = [True] * (2*k)
            bottom.append(row)
    return top, bottom

def solution(A):
    n = len(A)
    m = len(A[0])
    k = (min(n,m) // 2)

    while k != 0:
        t,b = make_grid(k)
        for i in range(m-(2*k)+1):
            for j in range(n-(2*k)+1):
                grid = list(row[i:i+(2*k)] for row in A[j:j+(2*k)])
                mid = len(grid) // 2
                top = list(row[:k] for row in grid[:mid])
                bottom = grid[k:2*k]
                if t == top and b == bottom:
                    return k
                
        k -= 1
    if k == 0:
        return 0