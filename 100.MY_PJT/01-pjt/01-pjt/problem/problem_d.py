import requests
from pprint import pprint
import csv
# TMDB API 키 설정
API_KEY = '51e9593e154174a4d3c4d2cf3a730039'
BASE_URL= "https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key=" + API_KEY + "&language=ko-KR"

# 문제 a에서 생성된 movies.csv 파일을 기반으로 영화 ID 목록 가져오기
MOVIE_IDS = []
with open('movies.csv', 'r', encoding='utf-8-sig') as file:
    reader = csv.DictReader(file)
    for row in reader:
        MOVIE_IDS.append(row['id'])



# 배우 데이터 처리 함수
def extract_casts(movie_id):
    url = BASE_URL.format(movie_id=movie_id)
    response = requests.get(url).json()
    
    cast_list = []
    for cast in response.get('cast', []):
        if cast.get('order') <=10:

            cast_info = {
                'movie_id': movie_id,
                'cast_id': cast.get('cast_id', ''),
                'name': cast.get('name', ''),
                'character': cast.get('character', ''),
                'order': cast.get('order', '')
            }
        
            cast_list.append(cast_info)
    
    return cast_list

all_casts = []
for movie_id in MOVIE_IDS:
    casts = extract_casts(movie_id)
    all_casts.extend(casts)  # 전체 리스트에 추가


# 데이터 수집 및 CSV 파일로 저장
import requests
from pprint import pprint
import csv
# TMDB API 키 설정
API_KEY = '51e9593e154174a4d3c4d2cf3a730039'
BASE_URL= "https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key=" + API_KEY + "&language=ko-KR"

# 문제 a에서 생성된 movies.csv 파일을 기반으로 영화 ID 목록 가져오기
MOVIE_IDS = []
with open('movies.csv', 'r', encoding='utf-8-sig') as file:
    reader = csv.DictReader(file)
    for row in reader:
        MOVIE_IDS.append(row['id'])



# 배우 데이터 처리 함수
def extract_casts(movie_id):
    url = BASE_URL.format(movie_id=movie_id)
    response = requests.get(url).json()
    
    cast_list = []
    for cast in response.get('cast', []):
        if cast.get('order') <=10:

            cast_info = {
                'movie_id': movie_id,
                'cast_id': cast.get('cast_id', ''),
                'name': cast.get('name', ''),
                'character': cast.get('character', ''),
                'order': cast.get('order', '')
            }
        
            cast_list.append(cast_info)
    
    return cast_list

all_casts = []
for movie_id in MOVIE_IDS:
    casts = extract_casts(movie_id)
    all_casts.extend(casts)  # 전체 리스트에 추가

pprint(all_casts)

# 데이터 수집 및 CSV 파일로 저장
def save_to_csv(data_list, filename):
    fields = ['movie_id', 'cast_id', 'name', 'character', 'order']

    with open(filename, 'w', newline='',encoding='utf-8-sig') as file:
        writer = csv.DictWriter(file, fieldnames=fields)
        writer.writeheader()
        writer.writerows(data_list)

save_to_csv(all_casts, 'movie_cast.csv')

print('저장 완료')