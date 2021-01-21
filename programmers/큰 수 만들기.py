def solution(number, k):
    # 입력된 첫 숫자를 스택에 입력
    stack = [number[0]]

    for num in number[1:]:
        # k가 0 이상, stack이 비어있지 않고 
        # stack 끝 값이 들어오는 수보다 작으면 stack에 값을 pop 해주며 k 카운트 -1
        while len(stack) > 0 and stack[-1] < num and k > 0: 
            k-=1
            stack.pop()
        stack.append(num)

    # k값이 남는 경우, ex) number = '100', k = 1
    # 남은 k만큼 stack에 있는 값들을 붙여줌
    if k != 0 : 
        stack = stack[:-k]

    answer = ''.join(stack)

    return answer