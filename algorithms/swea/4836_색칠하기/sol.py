import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())

    matrix = [[0 for _ in range(10)] for _ in range(10)]
    #색칠 시작
    for _ in range(N):
        rc_list = list(map(int, input().split())) #[1,1 / 3,3 / 1] = [시작 r, 시작 c, 끝 r, 끝 c, 색깔]
        color = rc_list[4]
        count = 0
        for row in range(rc_list[0], rc_list[2]+1):
            for col in range(rc_list[1], rc_list[3]+1):
                matrix[row][col]+= color

        for row in range(10):
            for col in range(10):
                if matrix[row][col] == 3:
                    count += 1

    print(f'#{tc} {count} ')

