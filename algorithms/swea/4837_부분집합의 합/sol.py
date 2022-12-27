import sys
sys.stdin = open('input.txt')

T = int(input())
origin_set = [i for i in range(1, 13)] # 1부터 12까지 원소가 담겨있는 집합 생성
n = len(origin_set) # 집합의 개수

for tc in range(1, T+1):
    N, K = map(int, input().split())
    count = 0

    for all_subset in range(1 << n): # 모든 부분 집합의 조합 확인
        subset = [] # 부분 집합을 담을 공간 생성
        for origin_set_idx in range(n): # origin_set의 원소가 이번 부분집합에 들어가는지 확인
            if all_subset & (1 << origin_set_idx):
              # 모든 부분 집합 조합(all_subset) 중에서origin_set 원소에 해당하는 부분집합 조합이
              # 겹치는 경우 (&연산자 값이 True인경우) => 우리가 원하는 부분집합 조합 확인
              # c.f> 5&2 => 101 010 (2진법) => 000 => 0 => False
                subset.append(origin_set[origin_set_idx])
                # 우리가 원하는 부분집합 조합 추가
        if len(subset) == N and sum(subset) == K:
          # 그 부분집합 조합 중에서 원소 개수가 N개이고, 원소의 총합이 K 인 경우 count 1 추가
            count += 1

    print(f'#{tc} {count}')
