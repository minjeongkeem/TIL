import sys
sys.stdin = open ('input.txt')

T = int(input())

def get_max_min_diff(numbers):
    max_value = min_value = numbers[0]
    for number in numbers[1:]:
        if number > max_value:
            max_value = number
        elif number < min_value:
            min_value = number

        ans = max_value - min_value
        return ans


for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))
    print(f'#{tc} {get_max_min_diff(numbers)}')