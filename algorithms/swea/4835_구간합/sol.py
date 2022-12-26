import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))


    for idx1 in range(N):
        first_value = numbers[idx1]
        for idx2 in range(N):
            if first_value < numbers[idx2]:
                first_value, numbers[idx2] = numbers[idx2], first_value
                numbers[idx1] = first_value

    min_sum_list = numbers[:M]
    min_sum = sum(min_sum_list)
    max_sum_list = numbers[-M:]
    max_sum = sum(max_sum_list)
    ans = max_sum - min_sum
    print(f'#{tc} {ans}')
