# quizgame
print('ようこそ　ゲームクイズへ！！')

playing = input('遊びますか？ y or n')

if playing.lower() == 'y':
    print('スタート!!')
else:
    print('バイバイ')
    quit()

score = 0

answer = input('FPSはなんの略称？')
if answer.lower() == 'first-person shooting' or answer == 'ファーストパーソンシューティング':
    print('正解')
    score += 1
else:
    print('不正解')

answer = input('TPSはなんの略称？')
if answer.lower() == 'third-person shooting' or answer == 'サードパーソンシューティング':
    print('正解')
    score += 1
else:
    print('不正解')

answer = input('RPGはなんの略称？')
if answer.lower() == 'role-playing game' or answer == 'ロールプレイングゲーム':
    print('正解')
    score += 1
else:
    print('不正解')

answer = input('RTSはなんの略称？')
if answer.lower() == 'real-time strategy' or answer == 'リアルタイムストラテジー':
    print('正解')
    score += 1
else:
    print('不正解')

print('あなたの成績' + str(score), '正解率' + str((score / 4) * 100) + '%')
