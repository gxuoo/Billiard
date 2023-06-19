from vpython import *

# 변수 선언
# 물리법칙 상수
gravity = 9.8           # 중력가속도
e = 0.5                 # 반발계수
mu = 0.1                # 마찰계수

# 당구공 반지름
ball_radius = 0.5

# 벽에 닿는 횟수 설정
flag_wall = 0

# 당구공끼리 부딪치는 횟수 설정
flag_W_to_O = 0   # 수구와 1목적구
flag_W_to_R = 0      # 수구와 2목적구
flag_O_to_R = 0     # 1목적구와 2목적구

# 시간 간격 설정
dt = 0.01

# 게임 진행 여부를 나타내는 변수
playing = True  

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

# 점수 UI 설정
score = 0
score_text = label(text="Score: " + str(score), pos=vector(0, 7, -10), height=25, box = False, opacity = 0)

# 게임 플레이 UI 설정
how_to_play = label(text="Click the mouse to move the white ball", pos=vector(0, 3, -10), height=20, color=color.yellow, box = False, opacity = 0)

# 게임 종료, 재시작 UI 설정
game_over_text = label(text="Game Over", pos=vector(0,0,0), height=50, color=color.red, visible=False, box = False, opacity = 0)
Restart_text = label(text="Press 'r' key to Restart", pos=vector(-15,-25,0), height=25, color=color.red, visible=False, box = False, opacity = 0)
Exit_text = label(text="Press 'q' key to Exit", pos=vector(15,-25,0), height=25, color=color.red, visible=False, box = False, opacity = 0)

# UI 업데이트 함수 정의
def score_update(score):        
    score_text.text = "Score: " + str(score)

# 당구공 충돌 함수
def ball_collision(b1, b2, e):
    x = b2.pos - b1.pos
    x_hat = norm(x)
    distance = mag(x)
    
    if dot(b1.velocity-b2.velocity, x_hat) < 0:
        return False
    
    v1_x = dot(b1.velocity, x_hat) * x_hat
    v1_p = b1.velocity - v1_x
    v2_x = dot(b2.velocity, x_hat) * x_hat
    v2_p = b2.velocity - v2_x
    total_m = b1.mass + b2.mass
    
    if distance < b1.radius + b2.radius:
        v1 = ((b1.mass - e * b2.mass) * v1_x + (1+e) * b2.mass * v2_x) / total_m
        v2 = ((b2.mass - e * b1.mass) * v2_x + (1+e) * b1.mass * v1_x) / total_m
        b1.velocity = v1 + v1_p
        b2.velocity = v2 + v2_p
        return True
    else:
        return False

    
# 당구공과 쿠션의 충돌 감지 함수
def wall_collision(ball):
    flag = 0
    if ball.pos.z - ball_radius <= wall_1.pos.z + wall_1.size.z / 2 or ball.pos.z + ball_radius >= wall_2.pos.z - wall_2.size.z / 2:    # 위아래 벽과의 충돌 검사
        ball.velocity.z = -ball.velocity.z  # 벽에 닿으면 z 방향 속도를 반전
        flag += 1
    if ball.pos.x - ball_radius <= wall_3.pos.x + wall_3.size.x / 2 or ball.pos.x + ball_radius >= wall_4.pos.x - wall_4.size.x / 2:    # 옆 벽과의 충돌 검사
        ball.velocity.x = -ball.velocity.x  # 벽에 닿으면 x 방향 속도를 반전
        flag += 1
        
    if flag >= 1:       # 벽과 충돌한 경우
        return True
    else:
        return False

# 구역마다 다른 마찰계수로 인한 당구공의 속도 설정
def ball_velocity(ball, mu, dt):
    ball.f = -mu * 1 * 9.8 * norm(ball.velocity)        # 마찰력 적용
    ball.velocity = ball.velocity + ball.f * dt
    
    # 당구공의 속도가 0.01보다 작아지면 속도를 0으로 설정
    if mag(ball.velocity) < 0.01:
        ball.velocity = vector(0,0,0)

# 게임 루프
while playing:
    rate(100)
    
    # 당구공과 바닥 충돌 검사 (공이 바닥 아래로 떨어지는 것을 방지하기 위해)
    if ball_white.pos.y - ball_radius <= floor_1.pos.y + floor_1.size.y / 2:
        ball_white.velocity.y = 0       # 바닥에 닿으면 y 방향 속도를 0으로 설정
    if ball_orange.pos.y - ball_radius <= floor_1.pos.y + floor_1.size.y / 2:
        ball_orange.velocity.y = 0      # 바닥에 닿으면 y 방향 속도를 0으로 설정
    if ball_red.pos.y - ball_radius <= floor_1.pos.y + floor_1.size.y / 2:
        ball_red.velocity.y = 0         # 바닥에 닿으면 y 방향 속도를 0으로 설정
        
    # 당구공과 쿠션 충돌 검사
    if wall_collision(ball_white):
        flag_wall += 1              # 3쿠션 조건을 확인하기 위한 변수
    wall_collision(ball_orange)
    wall_collision(ball_red)

    # 당구공들 간의 충돌 검사
    if ball_collision(ball_white, ball_orange, e):
        flag_W_to_O += 1            # 수구와 1목적구의 충돌을 확인하기 위한 변수
    if ball_collision(ball_white, ball_red, e):
        flag_W_to_R += 1            # 수구와 2목적구의 충돌을 확인하기 위한 변수
    if ball_collision(ball_red, ball_orange, e):
        flag_O_to_R += 1            # 1목적구와 2목적구의 충돌을 확인하기 위한 변수

    # 당구공의 속도 (각 영역에 따라 마찰력이 다르게 작용)
    if (-15 <= ball_white.pos.x and ball_white.pos.x < -5):
        ball_velocity(ball_white, 0, dt)
    elif (-5 <= ball_white.pos.x and ball_white.pos.x < 5):
        ball_velocity(ball_white, mu, dt)
    else:
        ball_velocity(ball_white, mu*2, dt)
    
    if (-15 <= ball_orange.pos.x and ball_orange.pos.x < -5):
        ball_velocity(ball_orange, 0, dt)
    elif (-5 <= ball_orange.pos.x and ball_orange.pos.x < 5):
        ball_velocity(ball_orange, mu, dt)
    else:
        ball_velocity(ball_orange, mu*2, dt)
    
    if (-15 <= ball_red.pos.x and ball_red.pos.x < -5):
        ball_velocity(ball_red, 0, dt)
    elif (-5 <= ball_red.pos.x and ball_red.pos.x < 5):
        ball_velocity(ball_red, mu, dt)
    else:
        ball_velocity(ball_red, mu*2, dt)
    
    # 당구공 이동
    ball_white.pos += ball_white.velocity * dt
    ball_orange.pos += ball_orange.velocity * dt
    ball_red.pos += ball_red.velocity * dt 
        
