#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#ques1
class Count:
    def counting(self,num):
        x=num
        i=0
        e=0
        o=0
        z=1
        count=4
        while(count>0):
            z=x%10
            if z==0:
                i+=1
            elif z%2==0:
                e+=1
            elif z%2 !=0:
                o+=1
            x=x//10
            count-=1
        print("Zeroes={},Evens={}, Odds={}".format(i,e,o))
        
c=Count()
num=int(input("Enter a four digit number:"))
c.counting(num)




#ques2
class MaxMin:
    def MaxandMin(self,list):
        z=min(list)
        y=max(list)
        print("{} is minimum and {} is maximum".format(z,y))
        
m=MaxMin()
list=[]
n=int(input("Enter how many numbers to input:"))
while(n>0):
    a=int(input())
    list.append(a)
    n-=1
m.MaxandMin(list)





#ques3 
database = {}
z=True
while(z):
    class Library:
        print("------MENU-----")
        print("1.ADD BOOK INFORMATION\n2.DISPLAY BOOK INFORMATION\n3.LIST ALL BOOKS OF GIVEN AUTHOR \n4.LIST THE COUNT OF BOOKS IN THE LIBRARY \n5.EXIT") 

        def inputdata(self,author,book):
            database[book]=author
            print("add complete")
        def display(self):
            print(*database)
        def liststep(self,author):
            def fill(n):
                if database[n]==author:
                    return True
                else:
                    return False
            res=filter(fill,database)
            for i in res:
                print(i)
        def countbook(self):
            print("total number of books present in library is ",len(database.keys()))

    l=Library()
    ch=input("Enter your choice:\n")
    if ch=='1':
        a=input("Enter the name of autnhor:\n")
        b=input("Enter the book name:\n")
        l.inputdata(a,b)
    elif ch=='2':
        l.display()
    elif ch=='3':
        aut=input("Enter the name of author to list books:\n")
        l.liststep(aut)
    elif ch=='4':
        l.countbook()
    else:
        print("thaks")
    k=input("do you want to continue? Enter (y/n):\n")
    if k!="y":
        z=False





#ques4 
n=int(input("Enter number of inputs:"))
arr=[]
brr=[]
i=0
j=0
while(n>0):
    a=int(input())
    arr.append(a)
    n-=1
print(arr)
arr.sort()
print(arr)





#ques7 
class Sum:
    def sumation(self,num):
        num1=num
        add=0
        
        while num>0:
            num1=num%10
            add+=num1
            num=num//10
        print("the addition is",add)
            
        
c=Sum()
num=int(input("Enter a number:"))
c.sumation(num)





#ques9 
class Sum:
    def sumation(self,num):
        num1=num%10;
        num2=num
        while num2>=10:
            num2=num2//10;
           
        add=num1+num2
        print("the addition is",add)
        
c=Sum()
num=int(input("Enter a number:"))
c.sumation(num)





#Ques5 
class Customer:
    acc_no=[]
    names=[]
    balance=[]
    def __init__(self,ac=[],name=[],bal=[]):
        self.acc_no=ac
        self.names=name
        self.balance=bal
    def check(self):
        for x in self.balance:
            if x<100:
                print("Account number:",acc_no)
                print("Name:",names)

ac_no=[]
names=[]
balance=[]
for x in range(1,4):
    ac=int(input("Account no:"))
    ac_no.append(ac)
    name=input("Enter Name:")
    names.append(name)
    bal=int(input("Enter Balance"))
    balance.append(bal)
print("Acc_no={}, Name={}, balance={}".format(ac_no,names,balance))
c=Customer(ac_no[:],names=[],balance=[])
c.check()





#ques10 
msg=input("Enter a string:")
z=msg.split()
print(z)
i=0
for x in z:
    m=x.split()
    for y in m:
        if y in "aeiou":
            del x[i]
        i+=1
print(msg)





#ques16 
class Letr:
    def Ascii(self,c):
        
        y=ord(c)
        nex=chr(ord(c)+1)
        pre=chr(ord(c)-1)
        print("{}={} next letter={} prev letter ={}".format(c,y,nex,pre))
l=Letr()
c=input("enter c\t")
l.Ascii(c)




#ques15
class Calc:
    def calculate(self,x,y,z):
        add=y+z
        total=x**add
        print("the power of it is\t",add)
        print("the calculation is\t",total)
        
c=Calc()
x=int(input("enter x\t"))
y=int(input("enter y\t"))
z=int(input("enter z\t"))
c.calculate(x,y,z)

#ques8
n=int(input("Enter the first number"))
m=int(input("Enter the second number"))
temp=n
n=m
m=temp
print("the swapped  values of n after the swapping is",format(n))
print("the swapped value of m afetr the swapping is",format(m))

#ques6
arr2=list()
s=int(input("Enter the number of name that is to be printed "))
for i in range(s):
    name=input("Enter the names:")
    arr2.append(name)
    print("the names are in the array",arr2)
    print("the sorted",sorted(arr2))
 
 #ques16
c=input("enter a character :")
print("the ASCII value of '"+ c +"' is",ord(c))





#ques18
def power(base,exp):
    if(exp==1):
        return(base)
    if(exp!=1):
        return(base*power(base,exp-1))
base=int(input("enter base:"))
exp=int(input("enter exponential value:"))
print("result:",power(base,exp))





#ques24
num=int(input("choose a number:"))
for i in range(1,11):
    print(num,'x',i,'=',num*i)




#ques25
ch = input("enter a character:")
if((ch>='a' and ch<= 'z') or (ch>='A' and ch<='Z')):
    print(ch,"is an alphabet")
else:
    print(ch,"is an digit")




#ques26
salary=int(input("enter salary \n"))
if salary>=5000:
    print("the hra",(salary*15)/100)
    print("the da",(salary*150)/100)
else:
   print("the hra",(salary*10)/100)
   print("the da",(salary*110)/100)

    
#ques20
fun3 =lambda x: x.replace("a","*")

print(fun3("my name is sraboni"))

   


# In[ ]:




