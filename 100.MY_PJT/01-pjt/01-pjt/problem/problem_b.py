# TMDB API 키 설정
import requests
import pandas as pd
from time import sleep
import csv

API_KEY = '994dabb097794ef790ee2f932d28432b'
BASE_URL = 'https://api.themoviedb.org/3'


# 영화 ID 리스트를 movies.csv 파일에서 읽어옴
def load_movie_list(csv_path='movies.csv'):
    movie_ids = []
    with open(csv_path, 'r', encoding='utf-8-sig') as file:
        reader = csv.DictReader(file)
        for row in reader:
            movie_id = row.get('id') or row.get('\ufeffid') or row.get('movie_id')
            if movie_id:
                movie_ids.append(int(movie_id))
    return movie_ids


# API 호출 함수
def get_movie_detail(movie_id):
    url = f'{BASE_URL}/movie/{movie_id}'
    params = {
        'api_key': API_KEY,
        'language': 'ko-KR'
    }
    response = requests.get(url, params=params)
    if response.status_code != 200:
        print(f"[ERROR] 영화 ID {movie_id} 데이터 요청 실패: {response.status_code}")
        return None
    return response.json()

# 영화 상세 데이터 처리 함수
def parse_movie_detail(data):
    if data is None:
        return None
    return {
        'movie_id': data.get('id'),
        'budget': data.get('budget'),
        'revenue': data.get('revenue'),
        'runtime': data.get('runtime'),
        'genres': ', '.join([genre['name'] for genre in data.get('genres', [])])
    }

# CSV 파일에서 영화 ID 읽기
def main():
    movie_ids = load_movie_list()
    movie_details_list = []

    for movie_id in movie_ids:
        data = get_movie_detail(movie_id)
        parsed = parse_movie_detail(data)
        if parsed:
            movie_details_list.append(parsed)
        sleep(0.25)  

    df = pd.DataFrame(movie_details_list)
    df.to_csv('movie_details.csv', index=False, encoding='utf-8-sig')
    print('movie_details.csv 파일이 생성 완료.')

if __name__ == '__main__':
    main()

