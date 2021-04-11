#drunk man
import random
if __name__ == '__main__':  
    field = [0] * 11   
    pos, field[pos] = 5,1
    print(field)
    print("...........starts.........")
    while 0<=pos <=len(field):
        ran = random.randint(0,1)
        if ran == 1:
            field[pos] = 0
            pos +=1
            field[pos] = 1
            print(field)
        else:
            field[pos] = 0
            pos -=1
            field[pos] = 1
            print(field)
        if field[0] ==1:
            print("Drunk man reached the left end")
            break
        loc = len(field)
        if field[loc-1] ==1:
            print("The drunken man reached right end")
            break
     

            
