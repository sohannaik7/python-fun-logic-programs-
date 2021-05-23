import random

myList1 = [0]*10
myList2 = [0]*20
for i in range(0,10):
    myList1[i]= random.randint(0,20)
    myList2[i] = random.randint(1,100)

name="sohan naik"
if 10 in myList1:
    print('30 is present')

if 20 not in myList1:
    print('120 is not present')

print("concatinated list=   ",myList1 + myList2)  
print("adding 3=    ",myList1 * 3)  
print("maximum=    ",max(myList2))
print("count of=    ",myList2.count(50))  

print("list2 index 2:8=     ",myList2[2:8])
print("list2 index 2:7:2    =",myList2[2:8:2])

myList1.append(30000)
print("after appending 60=  ",myList1)

myList2.insert(5, 8000)
print("after inserting 5,17=    ", myList2)

myList2.pop(15)
print("after deleting=  ",myList2)
myList1.reverse()
print("reversed list=   ",myList1)

myList1.clear()
print("clear list1=     ",myList1)

name.capitalize()
print("capitalize=  ",name)

name.center(3)
print("center(3)=   ",name)

e=name.endswith('a')
print("endswith=    ",e)

e=name.isalnum()
print("isalnum=     ",e)

e=name.isalpha()
print("isalpha=         ",e)

e=name.isdigit()
print("isdigit=     ",e)

e=name.islower()
print("islower=     ",e)

e=name.isspace()
print("isspace=     ",e)

e=name.isupper()
print("isupper=     ",e)

s = "___";
seq = ("a", "b", "c")
print("join=    ",s.join( seq ))

str = "Amanadli is fater of colve";
print(str.ljust(50, '0'))

print("lower=   ",name.lower())

str = "shawn spencer is best psychic dectetcive..!"
print("original str=    \n",str)
print("replace is with was=     ",str.replace("best", "worst"))
print("replace=",str.replace("shawn", "hanry",4))




str = "colve is niece of lucifer...";
print("rjust=",str.rjust(50, '0'))

str_list = str.split(sep=' ')
print("split=",str_list)


str_list = str.startswith("t")
print("startswith(t)=",str_list)

str_list = str.strip()
print("strip=",str_list)

str_list = str.swapcase()
print("swapcase=",str_list)

str_list = str.upper()
print("upper=",str_list)