# -*- codeing = utf-8 -*-
#@Time: 2021/2/18 11:41
#@Name: TakeCards.py


import random
import xlwt

lis = []    #记录总数
lis5 = []   #记录5*
i = 1       #记录抽卡次数(4*)
j = 1       #记录抽卡次数(5*)
h = 1       #记录抽卡次数(大保底)
r = 0       #记录抽卡次数

a = input("是否开始？（输入‘y’开始）")
if a == "y":
    while a == "y":
        print("1.单抽         2.十连        3.一键小保底")
        b = input()

#单抽
        if b == str(1):
            c = random.randint(1, 403000)
            if c <= 2148 and c >= 1:
                if c >= 1 and c <= 1074:
                    d = "胡桃(5*)"
                    print("\033[1;33m 胡桃(5*)\033[0m")
                    lis.append(d)
                    lis5.append(d)
                    i = 1
                    j = 1
                    h = 1
                    r += 1
                elif c > 1253 and c <= 1432:
                    d = "刻晴(5*)"
                    print("\033[1;33m 刻晴(5*)\033[0m")
                    lis.append(d)
                    lis5.append(d)
                    i = 1
                    j = 1
                    h += 1
                    r += 1
                elif c > 1432 and c <= 1611:
                    d = "莫娜(5*)"
                    print("\033[1;33m 莫娜(5*)\033[0m")
                    lis.append(d)
                    lis5.append(d)
                    i = 1
                    j = 1
                    h += 1
                    r += 1
                elif c > 1611 and c <= 1790:
                    d = "七七(5*)"
                    print("\033[1;33m 七七(5*)\033[0m")
                    lis.append(d)
                    lis5.append(d)
                    i = 1
                    j = 1
                    h += 1
                    r += 1
                elif c > 1790 and c <= 1969:
                    d = "迪卢克(5*)"
                    print("\033[1;33m 迪卢克(5*)\033[0m")
                    lis.append(d)
                    lis5.append(d)
                    i = 1
                    j = 1
                    h += 1
                    r += 1
                elif c > 1969 and c <= 2148:
                    d = "琴(5*)"
                    print("\033[1;33m 琴(5*)\033[0m")
                    lis.append(d)
                    lis5.append(d)
                    i = 1
                    j = 1
                    h += 1
                    r += 1

            # 大保底
            elif h == 180:
                d = "胡桃(5*)"
                print("\033[1;33m 胡桃(5*)\033[0m")
                lis.append(d)
                lis5.append(d)
                i = 1
                j = 1
                h = 1
                r += 1
            # 小保底
            elif j == 90:
                n = random.randint(1, 10)
                if n == 1:
                    d = "刻晴(5*)"
                    print("\033[1;33m 刻晴(5*)\033[0m")
                    lis.append(d)
                    lis5.append(d)
                    i = 1
                    j = 1
                    h += 1
                    r += 1
                elif n == 2:
                    d = "莫娜(5*)"
                    print("\033[1;33m 莫娜(5*)\033[0m")
                    lis.append(d)
                    lis5.append(d)
                    i = 1
                    j = 1
                    h += 1
                    r += 1
                elif n == 3:
                    d = "七七(5*)"
                    print("\033[1;33m 七七(5*)\033[0m")
                    lis.append(d)
                    lis5.append(d)
                    i = 1
                    j = 1
                    h += 1
                    r += 1
                elif n == 4:
                    d = "迪卢克(5*)"
                    print("\033[1;33m 迪卢克(5*)\033[0m")
                    lis.append(d)
                    lis5.append(d)
                    i = 1
                    j = 1
                    h += 1
                    r += 1
                elif n == 5:
                    d = "琴(5*)"
                    print("\033[1;33m 琴(5*)\033[0m")
                    lis.append(d)
                    lis5.append(d)
                    i = 1
                    j = 1
                    h += 1
                    r += 1
                else:
                    d = "胡桃(5*)"
                    print("\033[1;33m 胡桃(5*)\033[0m")
                    lis.append(d)
                    lis5.append(d)
                    i = 1
                    j = 1
                    h = 1
                    r += 1

            elif i == 10:
                d = "4*"
                print("\033[1;35m 4*\033[0m")
                lis.append(d)
                i = 1
                j += 1
                h += 1
                r += 1

            elif (c > 2148 and c <= 22701):
                d = "4*"
                print("\033[1;35m 4*\033[0m")
                lis.append(d)
                i = 1
                j += 1
                h += 1
                r += 1
            else:
                d = "3*"
                print("\033[1;34m 3*\033[0m")
                lis.append(d)
                i += 1
                j += 1
                h += 1
                r += 1

#十连
        elif b == str(2):
            for k in range(0, 10):
                c = random.randint(1, 403000)
                if c <= 2148 and c >= 1:
                    if c >= 1 and c <= 1074:
                        d = "胡桃(5*)"
                        print("\033[1;33m 胡桃(5*)\033[0m")
                        lis.append(d)
                        lis5.append(d)
                        i = 1
                        j = 1
                        h = 1
                        r += 1
                    elif c > 1253 and c <= 1432:
                        d = "刻晴(5*)"
                        print("\033[1;33m 刻晴(5*)\033[0m")
                        lis.append(d)
                        lis5.append(d)
                        i = 1
                        j = 1
                        h += 1
                        r += 1
                    elif c > 1432 and c <= 1611:
                        d = "莫娜(5*)"
                        print("\033[1;33m 莫娜(5*)\033[0m")
                        lis.append(d)
                        lis5.append(d)
                        i = 1
                        j = 1
                        h += 1
                        r += 1
                    elif c > 1611 and c <= 1790:
                        d = "七七(5*)"
                        print("\033[1;33m 七七(5*)\033[0m")
                        lis.append(d)
                        lis5.append(d)
                        i = 1
                        j = 1
                        h += 1
                        r += 1
                    elif c > 1790 and c <= 1969:
                        d = "迪卢克(5*)"
                        print("\033[1;33m 迪卢克(5*)\033[0m")
                        lis.append(d)
                        lis5.append(d)
                        i = 1
                        j = 1
                        h += 1
                        r += 1
                    elif c > 1969 and c <= 2148:
                        d = "琴(5*)"
                        print("\033[1;33m 琴(5*)\033[0m")
                        lis.append(d)
                        lis5.append(d)
                        i = 1
                        j = 1
                        h += 1
                        r += 1

                # 大保底
                elif h == 180:
                    d = "胡桃(5*)"
                    print("\033[1;33m 胡桃(5*)\033[0m")
                    lis.append(d)
                    lis5.append(d)
                    i = 1
                    j = 1
                    h = 1
                    r += 1
                # 小保底
                elif j == 90:
                    n = random.randint(1, 10)
                    if n == 1:
                        d = "刻晴(5*)"
                        print("\033[1;33m 刻晴(5*)\033[0m")
                        lis.append(d)
                        lis5.append(d)
                        i = 1
                        j = 1
                        h += 1
                        r += 1
                    elif n == 2:
                        d = "莫娜(5*)"
                        print("\033[1;33m 莫娜(5*)\033[0m")
                        lis.append(d)
                        lis5.append(d)
                        i = 1
                        j = 1
                        h += 1
                        r += 1
                    elif n == 3:
                        d = "七七(5*)"
                        print("\033[1;33m 七七(5*)\033[0m")
                        lis.append(d)
                        lis5.append(d)
                        i = 1
                        j = 1
                        h += 1
                        r += 1
                    elif n == 4:
                        d = "迪卢克(5*)"
                        print("\033[1;33m 迪卢克(5*)\033[0m")
                        lis.append(d)
                        lis5.append(d)
                        i = 1
                        j = 1
                        h += 1
                        r += 1
                    elif n == 5:
                        d = "琴(5*)"
                        print("\033[1;33m 琴(5*)\033[0m")
                        lis.append(d)
                        lis5.append(d)
                        i = 1
                        j = 1
                        h += 1
                        r += 1
                    else:
                        d = "胡桃(5*)"
                        print("\033[1;33m 胡桃(5*)\033[0m")
                        lis.append(d)
                        lis5.append(d)
                        i = 1
                        j = 1
                        h = 1
                        r += 1

                elif i == 10:
                    d = "4*"
                    print("\033[1;35m 4*\033[0m")
                    lis.append(d)
                    i = 1
                    j += 1
                    h += 1
                    r += 1

                elif (c > 2148 and c <= 22701):
                    d = "4*"
                    print("\033[1;35m 4*\033[0m")
                    lis.append(d)
                    i = 1
                    j += 1
                    h += 1
                    r += 1
                else:
                    d = "3*"
                    print("\033[1;34m 3*\033[0m")
                    lis.append(d)
                    i += 1
                    j += 1
                    h += 1
                    r += 1

#直接保底
        elif b == str(3):
            for m in range(1, 91):
                c = random.randint(1, 403000)
                if c <= 2148 and c >= 1:
                    if c >= 1 and c <= 1074:
                        d = "胡桃(5*)"
                        print("\033[1;33m 胡桃(5*)\033[0m")
                        lis.append(d)
                        lis5.append(d)
                        i = 1
                        j = 1
                        h = 1
                        r += 1
                    elif c > 1253 and c <= 1432:
                        d = "刻晴(5*)"
                        print("\033[1;33m 刻晴(5*)\033[0m")
                        lis.append(d)
                        lis5.append(d)
                        i = 1
                        j = 1
                        h += 1
                        r += 1
                    elif c > 1432 and c <= 1611:
                        d = "莫娜(5*)"
                        print("\033[1;33m 莫娜(5*)\033[0m")
                        lis.append(d)
                        lis5.append(d)
                        i = 1
                        j = 1
                        h += 1
                        r += 1
                    elif c > 1611 and c <= 1790:
                        d = "七七(5*)"
                        print("\033[1;33m 七七(5*)\033[0m")
                        lis.append(d)
                        lis5.append(d)
                        i = 1
                        j = 1
                        h += 1
                        r += 1
                    elif c > 1790 and c <= 1969:
                        d = "迪卢克(5*)"
                        print("\033[1;33m 迪卢克(5*)\033[0m")
                        lis.append(d)
                        lis5.append(d)
                        i = 1
                        j = 1
                        h += 1
                        r += 1
                    elif c > 1969 and c <= 2148:
                        d = "琴(5*)"
                        print("\033[1;33m 琴(5*)\033[0m")
                        lis.append(d)
                        lis5.append(d)
                        i = 1
                        j = 1
                        h += 1
                        r += 1

#大保底
                elif h == 180:
                    d = "胡桃(5*)"
                    print("\033[1;33m 胡桃(5*)\033[0m")
                    lis.append(d)
                    lis5.append(d)
                    i = 1
                    j = 1
                    h = 1
                    r += 1
#小保底
                elif j == 90:
                    n = random.randint(1, 10)
                    if n == 1:
                        d = "刻晴(5*)"
                        print("\033[1;33m 刻晴(5*)\033[0m")
                        lis.append(d)
                        lis5.append(d)
                        i = 1
                        j = 1
                        h += 1
                        r += 1
                    elif n == 2:
                        d = "莫娜(5*)"
                        print("\033[1;33m 莫娜(5*)\033[0m")
                        lis.append(d)
                        lis5.append(d)
                        i = 1
                        j = 1
                        h += 1
                        r += 1
                    elif n == 3:
                        d = "七七(5*)"
                        print("\033[1;33m 七七(5*)\033[0m")
                        lis.append(d)
                        lis5.append(d)
                        i = 1
                        j = 1
                        h += 1
                        r += 1
                    elif n == 4:
                        d = "迪卢克(5*)"
                        print("\033[1;33m 迪卢克(5*)\033[0m")
                        lis.append(d)
                        lis5.append(d)
                        i = 1
                        j = 1
                        h += 1
                        r += 1
                    elif n == 5:
                        d = "琴(5*)"
                        print("\033[1;33m 琴(5*)\033[0m")
                        lis.append(d)
                        lis5.append(d)
                        i = 1
                        j = 1
                        h += 1
                        r += 1
                    else:
                        d = "胡桃(5*)"
                        print("\033[1;33m 胡桃(5*)\033[0m")
                        lis.append(d)
                        lis5.append(d)
                        i = 1
                        j = 1
                        h = 1
                        r += 1

                elif i == 10:
                    d = "4*"
                    print("\033[1;35m 4*\033[0m")
                    lis.append(d)
                    i = 1
                    j += 1
                    h += 1
                    r += 1

                elif (c > 2148 and c <= 22701) :
                    d = "4*"
                    print("\033[1;35m 4*\033[0m")
                    lis.append(d)
                    i = 1
                    j += 1
                    h += 1
                    r += 1
                else:
                    d = "3*"
                    print("\033[1;34m 3*\033[0m")
                    lis.append(d)
                    i += 1
                    j += 1
                    h += 1
                    r += 1


        print("")
        print("已抽卡次数：%d"%(int(r)))
        print("共消耗原石：%d"%(int(r) * 160))
        print("")
        e = input("是否展示抽卡记录？")
        if e == "y":
            for m in lis:
                print(m)
        p = input("展示获得5*？")
        if p == "y":
            for q in lis5:
                print(q)

        print("")
        a = input("再来？")
else:
    print("好吧")
print("溜了！")