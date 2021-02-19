# -*- codeing = utf-8 -*-
#@Time: 2021/2/19 22:11
#@Name: DrawYourCards.py



import random

lis = []    #记录总数
i = 1       #记录抽卡次数(4*)
j = 1       #记录抽卡次数(5*)

a = input("是否开始？")
if a == "y":
    while a == "y":
        print("1.单抽       2.十连")
        b = input()
        if b == str(1):
            c = random.randint(1, 1000)
            if c <= 6 and c >= 1 or j == 90:
                d = "5*"
                print("\033[1;33m 5*\033[0m")
                lis.append(d)
                i += 1
                j = 0
            elif c >6 and c <= 58 or i == 10:
                d = "4*"
                print("\033[1;35m 4*\033[0m")
                lis.append(d)
                i = 0
                j += 1
            else :
                d = "3*"
                print("\033[1;34m 3*\033[0m")
                lis.append(d)
                i += 1
                j += 1
        elif b == str(2):
            for k in range(0, 10):
                c = random.randint(1, 1000)
                if c <= 6 and c >= 1 or j == 90:
                    d = "5*"
                    print("\033[1;33m 5*\033[0m")
                    lis.append(d)
                    i += 1
                    j = 0
                elif c > 6 and c <= 58 or i == 10:
                    d = "4*"
                    print("\033[1;35m 4*\033[0m")
                    lis.append(d)
                    i = 0
                    j += 1
                else:
                    d = "3*"
                    print("\033[1;34m 3*\033[0m")
                    lis.append(d)
                    i += 1
                    j += 1

        e = input("是否展示抽卡记录？")
        if e == "y":
            for m in lis:
                print(m)
        a = input("再来？")
else:
    print("再见！")
print("再见！")
