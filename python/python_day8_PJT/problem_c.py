from pprint import pprint
import requests  # requests 모듈 호출\n",


def ranking():
    res = requests.get('https://api.themoviedb.org/3/movie/popular?api_key=04e69234d934c5dc3ccae54809f46a7b&language=en-US&page=1')  # URL 로 요청 보냄\n",
    data = res.json()  # 요청의 응답 JSON을 *dict*로 변환함\n",
    empty_list =[]
    sorted_data = sorted(data['results'], key=lambda key_name: (-key_name['vote_average']))
    for idx in range (0, 5):
        empty_list.append(sorted_data[idx])
    return empty_list


def ranking():
    res = requests.get('https://api.themoviedb.org/3/movie/popular?api_key=04e69234d934c5dc3ccae54809f46a7b&language=en-US&page=1')  # URL 로 요청 보냄\n",
    movies = res.json()['results']  # 요청의 응답 JSON을 *dict*로 변환함\n", # 변수명 알아보기 쉽게 변환 필요
    top_rated = sorted(movies, key=lambda movie: movie['vote_average'], reverse=True) # 내장 함수에 crtl 올리면 함수 사용법 알 수 있음
    return top_rated[:5] # 슬라이싱
    


if __name__ == '__main__':
    """
    popular 영화목록을 정렬하여 평점순으로 5개 영화.
    """
    pprint(ranking())
    # => 영화정보 순서대로 출력
