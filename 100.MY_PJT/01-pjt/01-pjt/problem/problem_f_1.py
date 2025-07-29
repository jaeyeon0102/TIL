import pandas as pd

# 수익률 (%) = (수익 - 예산) / 예산 * 100
        #    = (revenue - budget) / budget * 100

df = pd.read_csv('movie_details.csv')
# print(df.head())

best = df[['movie_id','budget','revenue']].copy()

best['budget'] = best['budget'].astype(int)
best['revenue'] = best['revenue'].astype(int)

# budget이 0인 경우 0으로 출력, 나머지는 수익률 계산
best['profit'] = best.apply(
    lambda row: 0 if row['budget'] == 0 else (row['revenue'] - row['budget']) / row['budget'] * 100,
    axis=1
)

best['profit'] = best['profit'].astype(int)

best_sorted = best.sort_values(by='profit',ascending=False)

best_movie = best_sorted.iloc[0]

print(best_movie)