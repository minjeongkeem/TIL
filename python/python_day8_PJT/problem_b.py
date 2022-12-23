from pprint import pprint
import requests  # requests 모듈 호출\n", 모듈 호출은 항상 맨 상단에 사용 


def vote_average_movies():
    res = requests.get('https://api.themoviedb.org/3/movie/popular?api_key=04e69234d934c5dc3ccae54809f46a7b&language=en-US&page=1')  # URL 로 요청 보냄\n",
    data = res.json()  # 요청의 응답 JSON을 *dict*로 변환함\n",
    good_movies =[]
    for idx in range(0, len(data['results'])):
        if data['results'][idx]['vote_average']>= 8.0:
            good_movies.append(data['results'][idx])

    movies = data['results']


    for movie in movies: # 뽑고 싶은 것이 인덱스인지, element인지 확인 필요
        if movie['vote_average'] >= 8.0:
            good_movies.append(movie)

    # filter

    return good_movies

if __name__ == '__main__':
    """
    popular 영화목록중 vote_average가 8 이상인 영화목록 출력.
    """
    pprint(vote_average_movies())
    # => 영화정보 순서대로 출력
