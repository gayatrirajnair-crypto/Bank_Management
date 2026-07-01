import csv
da=[]
h=["Employee Number","Name","Salary"]
with open('d.csv','w',newline='') as c:
    n=int(input("enter no. of records you wish to enter: "))
    for i in range(n):
        en=input('enter employee number: ')
        na=input("enter name: ")
        s=input("enter salary: ")
        l=[[en,na,s]]
        da.extend(l)
    w=csv.writer(c)
    w.writerow(h)
    for i in da:
        w.writerow(i)  
import csv
s=0
with open('d.csv','r') as c:
    l=[]
    cr=csv.reader(c)
    for r in cr:
        l.append(r)
    for i in l:
        if i[1][0].lower()=='s' and len(i[1])<=20:
                print(i) 
                s+=1
if s==0:
    print("Not found")
