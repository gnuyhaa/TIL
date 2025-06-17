import random
import matplotlib.pyplot as plt

# 승/무/패 횟수 저장
win = 0
lose = 0
draw = 0

# 게임 반복
while True:
    user = input("Player (가위/바위/보/승률/그래프/종료): ").strip()

    if user == '종료':
        print("게임을 종료합니다.")
        break

    elif user == '승률':
        total = win + lose + draw
        if total > 0:
            rate = (win / total) * 100
            print(f"현재까지 승률: {rate:.1f}%")
        else:
            print("아직 게임 기록이 없습니다.")
        continue

    elif user == '그래프':
        labels = ['win', 'lose', 'draw']
        values = [win, lose, draw]
        plt.bar(labels, values)
        plt.title("가위바위보 결과")
        plt.ylabel("횟수")
        plt.show()
        continue

    elif user not in ['가위', '바위', '보']:
        print("잘못된 입력입니다.")
        continue

    # 컴퓨터 선택
    computer = random.choice(['가위', '바위', '보'])
    print(f"Computer: {computer}")

    # 결과 판정
    if user == computer:
        print("무승부")
        draw += 1
    elif (user == '가위' and computer == '보') or \
         (user == '바위' and computer == '가위') or \
         (user == '보' and computer == '바위'):
        print("플레이어 승리!")
        win += 1
    else:
        print("컴퓨터 승리!")
        lose += 1
