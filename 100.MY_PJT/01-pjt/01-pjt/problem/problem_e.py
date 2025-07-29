import requests
import pandas as pd
import csv
import json
from time import sleep
from collections import Counter

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

# movie_reviews.csv 로드
def load_reviews(csv_path='movie_reviews.csv'):
    reviews = []
    with open(csv_path, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            reviews.append(row)
    return reviews

# TMDB 평점 정보 가져오기
def get_movie_average_rating(movie_id):
    url = f'{BASE_URL}/movie/{movie_id}'
    params = {'api_key': API_KEY}
    response = requests.get(url, params=params)
    if response.status_code != 200:
        print(f"[ERROR] 영화 ID {movie_id} 평점 요청 실패: {response.status_code}")
        return None
    data = response.json()
    return {
        'movie_id': data.get('id'),
        'average_rating': data.get('vote_average'),
        'vote_count': data.get('vote_count')
    }

# 평점 분포 딕셔너리 반환
def get_rating_distribution(movie_id, reviews):
    ratings = [
        int(float(r['rating']))
        for r in reviews
        if r['movie_id'] == str(movie_id) and r['rating']
    ]
    counter = Counter(ratings)
    return counter


def main():
    movie_ids = load_movie_list()  
    reviews = load_reviews()
    results = []

    for movie_id in movie_ids:
        base_info = get_movie_average_rating(movie_id)
        if base_info is None:
            continue

        dist = get_rating_distribution(movie_id, reviews)
        base_info['rating_distribution'] = json.dumps(dist, ensure_ascii=False) 
        results.append(base_info)
        sleep(0.3)

    df = pd.DataFrame(results)
    df.to_csv('movie_ratings.csv', index=False, encoding='utf-8-sig')
    print('movie_ratings.csv 생성 완료')

if __name__ == '__main__':
    main()
