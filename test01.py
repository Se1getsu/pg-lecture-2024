# print("Hello, world!")

# print(1 + 2 * 3)

# attack = 500
# bonus = 0.2
# print(attack * (1+bonus))

# # 攻撃力を表示する。
# print(f"攻撃力は{attack}です。") # わわわわわ

# a = int(input("a > ")) # a = 12
# b = int(input("b > ")) # b = 5
# result = a + b
# print(f"合計 {result}")

# n = int(input("n > "))
# if n > 10:
#     print("10より大きい")
# elif n == 10:
#     print("10と同じ")
# else:
#     print("10より小さい")

# print("if文終了")

# import random

# def omikuji():
#     results = ["大吉", "大吉", "中吉", "中吉", "小吉", "凶"]
#     n = random.randint(0, 5)
#     return results[n]
#     # if n <= 2:
#     #     return "大吉"
#     # elif n <= 4:
#     #     return "中吉"
#     # elif n == 5:
#     #     return "小吉"
#     # else:
#     #     return "凶"

# for i in range(10):
#     print(f"{i+1}回目のループ")
#     print(omikuji())

# n = 1
# b = n > 0
# print(b)

# a = [1,2,3,4,5]
# print(a)
# print(a[3])
# a[4] = 0
# print(a)

# def calc_damage(attack, defence):
#     if attack < defence:
#         return 0
#     else:
#         return attack - defence

# damage = calc_damage(80, 30)
# print(damage)

# import random

# HAND_NAME = ["グー", "チョキ", "パー"]

# print("0:グー　1:チョキ　2:パー")
# my_hand = int(input("何を出す？ > "))
# teki_hand = random.randint(0, 2)

# # 敵が何を出したか表示する
# print(f"敵は{HAND_NAME[teki_hand]}を出した！")

# if my_hand == teki_hand:
#     print("あいこ")
# # elif my_hand == 0 and teki_hand == 1 or \
# #         my_hand == 1 and teki_hand == 2 or \
# #         my_hand == 2 and teki_hand == 0:
# elif (my_hand - teki_hand) % 3 == 2:
#     print("プレイヤーの勝ち！")
# else:
#     print("プレイヤーの負け！")

# class Quiz:
#     def __init__(self, content, answer):
#         self.content = content
#         self.__answer = answer

#     def is_correct(self, answer):
#         return self.__answer == answer

# quizzes = [
#     Quiz("薔薇", "ばら"),
#     Quiz("案山子", "かかし"),
#     Quiz("栗鼠", "りす")
# ]

# point = 0
# for quiz in quizzes:
#     print(quiz.content)
#     ans = input("> ")
#     if quiz.is_correct(ans):
#         print("正解！")
#         point += 1
#     else:
#         print("不正解！")

# print(f"最終結果：{point}点")


# import time

# print("aaaa")

# time.sleep(3)

# print("bbbbb")

# a = [1, 2, 3, 4, 5]
# print(id(a))

# a[2] = 9
# print(a)
# print(id(a))

# a = [1, 2, 3]
# b = a
# print(a, id(a))
# print(b, id(b))

# a[1] = 9
# print(a, id(a))
# print(b, id(b))
