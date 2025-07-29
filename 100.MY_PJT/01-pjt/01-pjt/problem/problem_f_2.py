import pandas as pd

df = pd.read_csv('movie_cast.csv', encoding='utf-8-sig')
# print(df.head())


#배우별 출연 영화 개수 세기
name_cnt = df.groupby('name')['movie_id'].nunique()

ans_name_cnt = name_cnt[name_cnt >= 2]

ans_name_cnt.to_csv('many_movie.csv', encoding='utf-8-sig')

print(ans_name_cnt)