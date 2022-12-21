import sys
sys.stdin = open('input.txt')

T = int(input())

def solve(numbers):
    total = 0
    avg = len(numbers)
    
    for num in numbers:
        total += num
    return round (total / avg)

for tc in range(1, T+1):
    
    numbers = list(map(int, input().split()))
    ans = solve(numbers) 
    print(f'#{tc} {ans}')