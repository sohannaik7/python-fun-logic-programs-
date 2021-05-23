
if __name__ == '__main__':
    fil = open("extfile1.txt","rt")
    cnt = 0
    while True:
        line = fil.readline()
        if not line:
            break
        for word in line.split():
            cnt +=1
        print(line.strip())
        print("number of words in that line were: =",cnt)
        cnt = 0
    