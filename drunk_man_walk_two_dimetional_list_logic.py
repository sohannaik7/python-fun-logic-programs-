import random


if __name__ == '__main__':  
    field = []
    i,j = 2,2
    for r in range(5):
        c = [0]*5
        field.append(c)
    field[2][2] = 1
    print(field)
    while True:
        ran = random.randint(0,3)
        if field[0][2] == 1:
            print("runk man reached the stright")
            break
        if field[2][0]==1:
            print("drunk man reached the left end")
            break
        if field[2][4]==1:
            print("drunk man reached the right side")
            break
        if field[4][2]==1:
            print("drunk man reached the backside")
            break
            
        if ran ==0:
            field[i][j] = 0
            i = i-1
            if i<0: break
            field[i][j]=1
            print(field)
        elif ran == 1:
            field[i][j]=0
            i = i+1
            if i>5: break
            field[i][j]=1
            print(field)
        elif ran == 2:    
            field[i][j]=0
            j = j-1
            if j<0: break

            field[i][j]=1
            print(field)
        elif ran==3:
            field[i][j] =0
            j = j+1
            if j>5: break
            field[i][j]=1
            print(field)
        





