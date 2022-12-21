import sys
sys.stdin = open('input.txt')

T = int(input())

def solve(numbers):
    total = 0
    
    for num in numbers:
        if num % 2:
            total += num
            
    return total

for tc in range(1, T+1):
    numbers = list(map(int, input().split()))
    print(f'#{tc} {solve(numbers)}')
    
                
