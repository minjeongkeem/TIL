import sys
sys.stdin = open ('input.txt')

T = int(input())


for tc in range (1, T+1):
    N = int(input())  # 다른 언어는 N을 가지고 배열 수를 잡기 때문에 필요
    numbers = list(map(int, input().split()))

    max_value = numbers[0]
    min_value = numbers[-1]
    for number1 in numbers:
        if number1 > max_value:
            max_value = number1
    for number2 in numbers:
        if number2 < min_value:
            min_value = number2

    ans = max_value - min_value
    print(f'#{tc} {ans}')

    #max(numbers) - min(numbers)
    #[477162, 658880, 751280, 927930, 297191]
    # Refactoring => 결과는 달라지지 않되, 내부적으로 더 개선된 코드 (clean code)
