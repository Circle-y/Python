"""
1.出拳
     玩家
     电脑
2.判断输赢
     1.玩家
     2.平局
     3.电脑
"""
# 玩家
player = int(input("输入 0-石头 1-剪刀 2-布 "))
# 电脑
import random
computer = random.randint(0,2)
# print(computer)
if player+1 == computer or player-2 == computer:
    print("玩家获胜")
elif player == computer:
    print("平局")
else:
    print("电脑获胜")
