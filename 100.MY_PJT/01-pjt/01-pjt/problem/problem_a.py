import requests
from pprint import pprint
import csv
# TMDB API 키 설정
API_KEY = '51e9593e154174a4d3c4d2cf3a730039'
BASE_URL = f"https://api.themoviedb.org/3/movie/popular?api_key={API_KEY}&language=ko-KR&page=1"

# API 호출 함수 
# API 조회
response = requests.get(BASE_URL).json()

# pprint(response)

# 영화 데이터 처리 함수
def extract_movies(response_data):
    fields = ['id', 'title', 'release_date', 'popularity']
    completed_todos = []

    for item in response_data.get('results', []):
        temp_item = {key: item.get(key, '') for key in fields}
        completed_todos.append(temp_item)

    return completed_todos, fields

# 데이터 수집 및 CSV 파일로 저장
def save_to_csv(data_list, fields, filename):
    with open(filename, 'w', newline='', encoding='utf-8-sig') as file:
        writer = csv.DictWriter(file, fieldnames=fields)
        writer.writeheader()
        writer.writerows(data_list)

movies, movie_fields = extract_movies(response)
pprint(movies)  # 보기용

save_to_csv(movies, movie_fields, 'movies.csv')