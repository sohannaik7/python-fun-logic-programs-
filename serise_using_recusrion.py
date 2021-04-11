import math

def factoriall(n):
    return(math.factorial(n))

global total
def sum(x):
    def summ(i,n):
        if i==n:
            return total
        total = total + ((x ** i) / factoriall(i))
        print(total)
        i=i+1
        return summ(i,n)

if __name__ == '__main__':
    x = int(input("enter the x value of series"))
    n = int(input("enter the limit"))
    i = 1
    mm = sum(x)
    temo = mm(i,n)
    print(temo)