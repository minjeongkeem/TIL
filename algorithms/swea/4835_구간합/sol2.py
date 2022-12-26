import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))
    # n = 10, m =3 / 1 2 3 4 5 6 7 8 9 10 => 123/234/345/456/567/678/789/8910

    ans_list = []
    for idx in range(N-M+1):
        ans_list.append(sum(numbers[idx:idx+M]))
        ans = max(ans_list) - min(ans_list)
    print(f'#{tc} {ans}')
