import random

def roll():
    dice1 = random.randint(1, 6)
    print("dice 1")
    if dice1 == 1:
        print("*", "1")
    elif dice1 == 2:
        print("* *", "2")
    elif dice1 == 3:
        print("* * *", "3")
    elif dice1 == 4:
        print("* * * *", "4")
    elif dice1 == 5:
        print("* * * * *", "5")
    else:
        print("* * * * * *", "6")

    dice2 = random.randint(1, 6)
    print("dice 2")
    if dice2 == 1:
        print("*", "1")
    elif dice2 == 2:
        print("* *", "2")
    elif dice2 == 3:
        print("* * *", "3")
    elif dice2 == 4:
        print("* * * *", "4")
    elif dice2 == 5:
        print("* * * * *", "5")
    else:
        print("* * * * * *", "6")

    return dice1, dice2


if __name__ == '__main__':
    won = False
    add = 0
    add2 = 0
    count = 0
    cnt1 = 0
    cnt2 = 0
    while not won:
        print("person 1 playing")
        dice1, dice2 = roll()
        add = dice1 + dice2
        if add == 7 or add == 11:
            won = False
            cnt1=cnt1+1

        print("person 2 playing")
        dice1, dice2 = roll()
        add2 = dice1 + dice2

        if add2 == 1 or add2 == 12 or add2 == 2 or add2 == 3:
            won = False
            cnt2=cnt2+1

        if cnt1 == 5:
            print("person 1 won the match, by",cnt1-cnt2,"score")
            print("total number of attemps were .",count)
            break
        elif cnt2==5:
            print("person 2 won the match, by",cnt2-cnt1,"score")
            print("total number of attemps were .",count)

            break
        print("no one won, moving toi next round .............................")
        count = count + 1

    print("person 1",cnt1)
    print("person 2",cnt2)