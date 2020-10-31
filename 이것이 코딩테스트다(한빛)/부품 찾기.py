def binary_search(list, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if list[mid] == target:
            return mid
        elif list[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

    return None

n = int(input())
part_list = list(map(int, input().split()))
part_list.sort()

m = int(input())
ask_list = list(map(int, input().split()))

for i in ask_list:
    result = binary_search(part_list, i, 0, n-1)
    if result != None:
        print('yes', end=' ')
    else:
        print('no', end=' ')