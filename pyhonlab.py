def palin(s,cnt):
    if len(s) <= 1: return True
    elif s[0]!=s[-1]: return False
    else: 
        print(s[0],".....",s[-1])
        print(cnt)
        return palin(s[1:len(s)-1],cnt+1)

def isLetter(c): return ('a' <= c <= 'z') or ('A' <= c <= 'Z')

def palindromeTest(s,cnt):
    print("..........",s)        # srtring yet to be compared
    if len(s)<=1: return True
    elif not isLetter(s[0]): 
        cnt +=1
        return palindromeTest(s[1:],cnt)
    elif not isLetter(s[-1]): 
        cnt+=1
        return palindromeTest(s[:-1],cnt)
    elif s[0].lower() != s[-1].lower(): return False
    else:
        print(cnt)
        cnt +=1
        print(s[0],"....",s[-1])
        return palindromeTest(s[1:len(s)-1],cnt)


if __name__ == '__main__':
    strr = input("string herer .")
    print(palin(strr,0))
    print(palindromeTest(strr,0))
