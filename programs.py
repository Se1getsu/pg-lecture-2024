import os, sys

__FILE_NAME = os.path.basename(__file__)
USAGE = f'''\
Usage:
    py {__FILE_NAME} <function_number>
    python {__FILE_NAME} <function_number>'''


# 標準出力・計算・変数
def func_01():
    print("Hello, world!")

    print(1 + 2 * 3) # 9になるかな？ 7になるかな？

    attack = 500
    bonus = 0.2
    print(attack * (1+bonus)) # 600

    # ここまで来たら コメント と コメントアウト を説明する。

def func_02():
    # うまくいかない例
    a = input("a > ") # a = "12"
    b = input("b > ") # b = "5"
    result = a + b
    # result = "12" + "5"
    print(f"a + b = {result}")

def func_03():
    # うまくいく例
    a = int(input("a > "))
    b = int(input("b > "))
    result = a + b
    # result = 12 + 5
    print(f"a + b = {result}")

def func_04():
    name = input("名前 > ")
    print(f"私は{name}です")

def func_05():
    n = int(input("n > "))
    if n > 10:
        print("10より大きい")
    elif n == 10:
        print("10と同じ")
    else:
        print("10より小さい")

def func_06():
    import random
    print(random.randint(1, 6)) # 1 以上 6 以下のランダムな整数

def func_07():
    import random
    n = random.randint(1, 6)
    if n == 1:
        print("大吉")
    elif n == 2:
        print("中吉")
    elif n == 3:
        print("吉")
    else:
        print("凶")  # 確率配分はお好みで

def func_08():
    import random

    def omikuji():
        n = random.randint(1, 6)
        if n == 1:
            print("大吉")
        elif n == 2:
            print("中吉")
        elif n == 3:
            print("吉")
        else:
            print("凶")  # 確率配分はお好みで

    # omikuji()
    # omikuji()
    # omikuji()
    # omikuji()
    # omikuji()
    # omikuji()
    # omikuji()
    # omikuji()
    # omikuji()
    # omikuji()

    for i in range(10):
        print(f"{i}回目：", end="") # これだと 0 回目からスタートする
        omikuji()

def func_09():
    import random

    def omikuji():
        results = ["大吉", "中吉", "吉", "凶", "凶", "凶"]
        return random.choice(results)

    for i in range(10):
        print(f"{i}回目：", end="") # これだと 0 回目からスタートする
        result = omikuji()
        print(result)

def func_10():
    import random

    print("0:グー　1:チョキ　2:パー")
    my_hand = int(input("何を出す？ > "))
    teki_hand = random.randint(0, 2)

    if teki_hand == 0:
        print("敵はグーを出した！")
    elif teki_hand == 1:
        print("敵はチョキを出した！")
    else:
        print("敵はパーを出した！")

    if my_hand == teki_hand:
        print("あいこ")
    elif my_hand == 0 and teki_hand == 1 or \
        my_hand == 1 and teki_hand == 2 or \
        my_hand == 2 and teki_hand == 0:
        print("プレイヤーの勝ち！")
    else:
        print("プレイヤーの負け！")

def func_11():
    import random

    print("0:グー　1:チョキ　2:パー")
    HAND_LIST = ["グー", "チョキ", "パー"]
    my_hand = int(input("何を出す？ > "))
    teki_hand = random.randint(0, 2)

    print(f"敵は{HAND_LIST[teki_hand]}を出した！")

    if my_hand == teki_hand:
        print("あいこ")
    elif (my_hand - teki_hand) % 3 == 2:
        print("プレイヤーの勝ち！")
    else:
        print("プレイヤーの負け！")

# TODO: High & Low

if __name__ == "__main__":
    args = sys.argv[1:]
    if len(args) != 1:
        print(USAGE)
        sys.exit(1)

    i = int(args[0])
    f = eval(f"func_{i:02d}")
    f()
