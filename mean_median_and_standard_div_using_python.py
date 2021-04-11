import statistics as stat
import random

def calculate(lists):
    for i in range(1,n):
        lists.append(random.randint(1,r))
    meanlist=stat.mean(lists)
    medList=stat.median(lists)
    stddev=stat.stdev(lists,meanlist)
    return meanlist, medList, stddev
    

if __name__ == '__main__':

    lists,Devlist=[],[]
    n=int(input("enter the siz of list"))
    m =int(input("enter the starting range"))
    r=int(input("enter the ending range till"))
    meanlist, midlist, stddev = calculate(lists)
    print("list--:",lists,"....")

    for i in lists:
        foo=i-meanlist
        if foo < 0:
            foo=foo*-1
        Devlist.append(foo)

    print("dev list:",Devlist,"\n")
    print("max st Dev:,...",max(Devlist),"\n")
    print("min st Dev:",min(Devlist),"\n")
    print("mean",meanlist,"\n")
    print("median",midlist,"\n")
        
        
