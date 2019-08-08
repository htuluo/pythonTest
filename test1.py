import random

game_count = 0
all_counts = []
while True:
    game_count += 1
    guess_count = 0
    answer = random.randint(0, 99)
    while True:
        guess = int(input("猜个数字（0-99）："))
        guess_count += 1
        if guess == answer:
            print("恭喜你拆对了")
            print("你一共拆了" + str(guess_count) + "次")
            all_counts.append(guess_count)
            break
        elif guess > answer:
            print("拆得太大了")
        else:
            print("拆得太小了")
    # 必须用raw_input，如果用input，输入时需要打双引号才能识别，识别不了string
    onemore = raw_input("再来一次可好(Y/N)？")
    if onemore != "Y" and onemore != "y":
        print
        onemore
        print("舍不得你，下次再来哈")
        print("您的成绩如下：")
        print(all_counts)
        print("平均拆中次数" + str(sum(all_counts) / float(len(all_counts))))
        break
    else:
        print("马上再来")
