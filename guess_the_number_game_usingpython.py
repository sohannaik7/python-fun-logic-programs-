import random


def check(val,ran):
    if ran == val:
        print("you have guessed correct number that is ", ran)
        return False
    elif ran > val:
        print("it woant that far, was't ", val)
        return True
    elif ran < val:
        print("you have gonne too far, it was", val)
        return True




if __name__ == '__main__':
    won = False
    while not won:
        ran = random.randint(1000, 1020)
        u1 = int(input("enter your choice person 1..."))
        won = check(u1,ran)
        if won == False:
            print("you have won this round")
            break

        u2 = int(input("enter your choice person 2..."))
        won = check(u2, ran)
        if won == False:
            print("you have won this round")
            break

        u3 = int(input("enter your choice person 3..."))
        won = check(u3, ran)
        if won == False:
            print("you have won this round")
            break

        u4 = int(input("enter your choice person 4..."))
        won = check(u4, ran)
        if won == False:
            print("you have won this round")
            break

        u5 = int(input("enter your choice person 5..."))
        won = check(u5, ran)
        if won == False:
            print("you have won this round")
            break

        won = False
        print("next round.............................")