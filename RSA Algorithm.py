import math

def isprimenum(n):
    if n > 0:
        for i in range(2,n):
            if n%i == 0:
                return False
        return True


def getE(fn):
    t = 2
    while t<fn:
        if (math.gcd(t,fn) == 1):
            return t
        else:
            t= t+1

def findD(e, fn):
    t = 2
    while t<fn:
        if ((t*e) % fn) == 1:
            return t
        else:
            t = t+1


if __name__ == '__main__':
    p,q = 0,0
    p = int(input("Enter the value of p, prime number 1 "))
    q = int(input("Enter the value of ,q prime number 2 "))
    if (isprimenum(p) == True) and (isprimenum(q) == True):
        n =  p * q
        fn = (p-1) * (q-1)
        e = getE(fn)
        d = findD(e,fn)
        print(n, " ", fn, "  ", e, " ",d)

        mess = int(input("enter the message"))

        encry = pow(mess,e) % n
        print(encry)

        decry = pow(encry,d) % n
        print(decry)
    else:
        print("one of p and q arent prime number")
        exit()

         
     
