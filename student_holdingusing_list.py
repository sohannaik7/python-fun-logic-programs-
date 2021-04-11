from operator import itemgetter
def resultt(avg):
    if(avg>90): return "s"
    elif(avg>70): return "a"
    elif(avg>65): return "b"
    elif(avg>55): return "c"
    elif(avg>40): return "d"
    else: return "fail"
if __name__ == '__main__':
    stdlist=[]
    gr = ""
    n = int(input('enter the number of students '))

    for i in range(0, n):
        stdid=input("enter the student register number")
        name= input("Enter student name")
        print("Enter Marks Obtained in 5 Subjects: ")
        m1 = int(input("m1.."))
        m2 = int(input("m2.."))
        m3 = int(input("n3.."))
        total = m1 + m2 + m3 
        print("total====", total)
        avg=(total/300)* 100
        print("averag====", avg)
        gr = resultt(avg)
        stdlist.append([stdid,name,m1,m2,m3,total,gr])

        
    print("Sno \t name \t m1 \t m2 \t m3 \t total \t grade")
    #stdlist.sort(key=lambda x: x.gr)
    for i in stdlist:
        print(stdid,"\t",name,"\t",m1,"\t",m2,"\t",m3,"\t",total,"\t",gr)
    
    






