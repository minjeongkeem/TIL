import requests  # requests 모듈 호출\n",


def popular_count():

    res = requests.get('https://api.themoviedb.org/3/movie/popular?api_key=04e69234d934c5dc3ccae54809f46a7b&language=en-US&page=1')  # URL 로 요청 보냄\n",
    data = res.json()  # 요청의 응답 JSON을 *dict*로 변환함\n",
    return len(data['results']) # data 확인(list or dict일 확률이 높음)\n",




if __name__ == '__main__': 
    """
    popular 영화목록의 개수 출력.
    """
    print(popular_count())
    # => 20
