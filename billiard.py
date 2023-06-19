from vpython import *

# 변수 선언
# 물리법칙 상수
gravity = 9.8           # 중력가속도
e = 0.5                 # 반발계수
mu = 0.1                # 마찰계수

# 당구공 반지름
ball_radius = 0.5

# 시뮬레이션 환경 설정
scene = canvas(title='Strange Billiards', width=800, height=600, center=vector(0,3,0))
scene.camera.pos = vector(0, 2, 2)      # 카메라 위치 설정
scene.camera.axis = vector(0, -1, -1)   # 카메라가 바라보는 방향 설정
scene.range = 15                        # 화면 표시 범위

# 바닥 생성 (가로:세로 = 2:1)
floor_1 = box(pos=vec(-10, 0, 0), size=vec(10, 0.2, 15), color=color.hsv_to_rgb(vec(0.48,0.4,1)))   # 마찰X
floor_2 = box(pos=vec(0, 0, 0), size=vec(10, 0.2, 15), color=color.hsv_to_rgb(vec(0.48,0.7,1)))     # 기본 마찰
floor_3 = box(pos=vec(10, 0, 0), size=vec(10, 0.2, 15), color=color.hsv_to_rgb(vec(0.48,1,1)))      # 기본 마찰*2

# 벽 생성
wall_1 = box(pos=vec(0,0.35,-7.6), size=vec(30.4, 0.5, 0.2), color=color.hsv_to_rgb(vec(0.6,1,1)))  # 위쪽
wall_2 = box(pos=vec(0,0.35,7.6), size=vec(30.4, 0.5, 0.2), color=color.hsv_to_rgb(vec(0.6,1,1)))   # 아래쪽
wall_3 = box(pos=vec(-15.1,0.35,0), size=vec(0.2, 0.5, 15), color=color.hsv_to_rgb(vec(0.6,1,1)))   # 왼쪽
wall_4 = box(pos=vec(15.1,0.35,0), size=vec(0.2, 0.5, 15), color=color.hsv_to_rgb(vec(0.6,1,1)))    # 오른쪽

# 공 생성
ball_white = sphere(pos=vec(7.5, 1+ball_radius, -1.875), radius=ball_radius, mass=1, color=color.white)     # 수구
ball_orange = sphere(pos=vec(7.5, 1+ball_radius, 0), radius=ball_radius, mass=1,color=color.orange)         # 1목적구
ball_red = sphere(pos=vec(-7.5, 1+ball_radius, 0), radius=ball_radius, mass=1, color=color.red)             # 2목적구

# 공 초기속도 설정
ball_white.velocity = vec(0, -gravity, 0)
ball_orange.velocity = vec(0, -gravity, 0)
ball_red.velocity = vec(0, -gravity, 0)
