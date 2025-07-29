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
def get_review(movie_id):
    reviews = []
    page = 1

    while True:
        url = f'{BASE_URL}/movie/{movie_id}/reviews'
        params = {
            'api_key': API_KEY,
            'page': page
        }
        response = requests.get(url, params=params)

        if response.status_code != 200:
            print(f"[ERROR] 영화 ID {movie_id} 리뷰 요청 실패: {response.status_code}")
            break

        data = response.json()
        results = data.get('results', [])

        for result in results:
            par = parser_movie_review(result,movie_id)
            if par:
                reviews.append(par)

        if not data.get('total_pages') or page >= data['total_pages']:
            break

    
        page += 1
        sleep(0.25)

    return reviews
    


# 리뷰 데이터 처리 함수
def parser_movie_review(data, movie_id):
    content = data.get('content')
    if data.get('content') is None:
        content = '리뷰 없음'
    
    rating = data.get('author_details', {}).get('rating')
    print(rating)
    
    if rating is None or rating < 5:
        return None

    return {
        'review_id': data.get('id'),
        'movie_id': movie_id,
        'author': data.get('author'),
        'content': content,
        'rating': data.get('author_details', {}).get('rating')
    }
    
# 데이터 수집 및 CSV 파일로 저장


def main():
    movie_ids = load_movie_list()
    reviews_list = []

    for movie_id in movie_ids:
        data = get_review(movie_id) 
        reviews_list.extend(data)   
        sleep(0.25)
        

    df = pd.DataFrame(reviews_list)
    df.to_csv('movie_reviews.csv', index=False, encoding='utf-8-sig')
    print('movie_reviews.csv 파일이 생성 완료.')

if __name__ == '__main__':
    main()