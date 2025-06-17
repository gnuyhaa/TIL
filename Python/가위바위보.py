import random
select = ['가위', '바위','보']
computer = random.choice(select)

print(computer)


while True:
    user = input("Player: ")

    if user == '가위' and computer == '보' or user == '바위' and computer == '가위' or user == '보' and computer == '바위':
        print('Player:', user + ', Computer:', computer + ", 플레이어 승리")
    
    break

