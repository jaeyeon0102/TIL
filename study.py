import math

# 흰 공과 목표 공의 좌표
white_ball_x = 100
white_ball_y = 50
target_ball_x = 150
target_ball_y = 100

# x, y 좌표 간의 차이 (벡터)
dx = target_ball_x - white_ball_x
dy = target_ball_y - white_ball_y

# atan2를 사용하여 각도(라디안) 계산
radian = math.atan2(dy, dx)

# 라디안을 도로 변환 (0~360도 범위로 보정)
angle = (180.0 / math.pi) * radian
if angle < 0:
    angle += 360

print(f"Angle: {angle} degrees")