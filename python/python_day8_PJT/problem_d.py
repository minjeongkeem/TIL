from pprint import pprint
import requests

def recommendation(title):
    
    res = requests.get(f'https://api.themoviedb.org/3/search/movie?api_key=04e69234d934c5dc3ccae54809f46a7b&language=en-US&query={title}&page=1&include_adult=false')  # URL 로 요청 보냄\n",
    data = res.json()  # 요청의 응답 JSON을 *dict*로 변환함\n",
    
    # if data['results'] != []:
    if not data['results']:
        movie_id = data['results'][0]['id']
        res2 = requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}/recommendations?api_key=04e69234d934c5dc3ccae54809f46a7b&language=en-US&page=1')  # URL 로 요청 보냄\n",
        data2 = res2.json()  # 요청의 응답 JSON을 *dict*로 변환함\n"
        movie_names = []
        for idx in range(0, len(data2['results'])):
            movie_names.append(data2['results'][idx]['title'])
        return movie_names
    else:
        return 'None'


    


if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면
    해당 영화의 id를 기반으로 추천 영화 목록 구성.
    추천 영화가 없을 경우 [].
    영화 id검색에 실패할 경우 None.
    """
    pprint(recommendation('기생충'))
    # ['조커', '조조 래빗', '1917', ..., '토이 스토리 4', '스파이더맨: 파 프롬 홈']
    pprint(recommendation('그래비티'))
    # []  => 추천 영화 없음
    pprint(recommendation('검색할 수 없는 영화'))
    # => None
