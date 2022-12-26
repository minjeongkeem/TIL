import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range (1, T+1):
    N = int(input())
    str_numbers = list(input())
    numbers = list(map(int, str_numbers))
    cards = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    counts = [0] * 10
    for number in numbers:
        counts[number] += 1

    max_count = 0
    max_number = 0
    for number in range(10):
        if counts[number] >= max_count:
            max_count = counts[number]
            max_number = number

    print(f'#{tc} {max_number} {max_count}')



# counting sort - visualgo





    # dicts = {}
    # for idx1 in range(N):
    #     number = numbers[idx1]
    #     count = 0
    #     for idx2 in range(N):
#     #         if numbers[idx2] == number:
#     #             count += 1
#     #             dicts[f'{number}'] = count
    # sorted_dicts = sorted(dicts.values(), reverse=True)
    # sorted_key_lists = sorted(key_lists, reverse=True)
    # key_lists = list(dicts.keys())
    # val_lists = list(dicts.values())
    # position = val_lists.index(sorted_dicts[0])
    # if len(set(val_lists)) == 1:
    #     print(f'#{tc} {sorted_key_lists[0]} {sorted_dicts[0]}')
    # else:
    #     print(f'#{tc} {key_lists[position]} {sorted_dicts[0]}')
