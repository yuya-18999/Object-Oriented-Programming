from baseball import Baseball

B = Baseball
print("hello world!!")

y = B('ヤクルト', 143, 73, 52, 18)
ha = B('阪神', 143, 77, 56, 10)
k = B('巨人', 143, 61, 62, 20)
hi = B('広島', 143, 63, 68, 12)
t = B('中日', 143, 55, 71, 17)
d = B('DeNA', 143, 54, 73, 16)
o = B('オリックス', 143, 70, 55, 18)
ro = B('ロッテ', 143, 67, 57, 19)
ra = B('楽天', 143, 66, 62, 15)
so = B('ソフトバンク', 143, 60, 62, 21)
n = B('日本ハム', 143, 55, 68, 20)
se = B('西部', 143, 55, 70, 18)

central_team = [y, ha, k, hi, t, d]
pacific_team = [o, ro, ra, so, n, se]

print('セントラルリーグ')
for central in central_team:
    central.team_grades_c()

print('パシフィックリーグ')
for pacific in pacific_team:
    pacific.team_grades_p()
