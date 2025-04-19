#accessing elements in list
num=[33,5,8,7]
names=['dhaval','nirali','namarata','siddharth']
num=[10]*5 #repetation
names[0]='harsita'#mutable
num[0:2]=[20,30]#mutable
print(num)
print(names)
print(names[0])
print (num[1:4])

lst1=[99,100,101]
lst2=lst1+[102,103,104]#concatenated
print(lst2)

lst3=lst1+lst2#merge of two string
print(lst3)

l=list('parmar')#conversion of string/set/tuple into list
print(l)

num1=[15,7,88]
num2=num1
print(num1 is num2)#aliasing
print(num1,num2)

ele1=[99,100,101]
ele2=[]
ele2=ele2+ele1
print(ele1 is ele2)#cloning
print(ele1,ele2)

lst=[1,2,3,4]
print(3 in lst)#searching

id1=[11,22,33,44,55]
id2=[11,22,33,44,55]
id3=id1
print(id1 is id2, id1 is not id2,id1 is id3)#identity

co1=[1,2,3,4]
co2=[1,2,4,5]
print(co1>co2)#comparision

emp=[]
if not emp:
    print("empty list")
print(bool(emp))#emptiness


dig1=[10,20,30,40,50]
for i in dig1:
    print(i)#using for loop on element


i=0
for i in range(len(dig1)):
       print(dig1[i]) #can be also as: print("num[i]",i)
       i=i+1# using for loop on index

i=0
while i<len(dig1):
    print(dig1[i])
    i=i+1#use of while loop

for index,i in enumerate(dig1):
                 print(index,i)# enumarate

animal=['cat','dog','cow']                 ,
for index,i in enumerate(animal):
                 print(index,i)# enumarate
                 

#use of built in function                  
dig=[1,2,3,4,5,6,7,8,9]
print( "length=",len(dig))#len
print( "maximum=",max(dig))#max
print( "minimum=",min(dig))#min
print( "sum=",sum(dig))#min

n=[9,6,7,3,0]
del(n[3])
print(n)#delete
p=[5,7,8,4,6,7,88,9]
del(p[2:5])
print(p)#delete

d=[5,66,88,9,1,1000]
d.sort()#sort
print(d)
d.reverse()#reverse
print(d)

e=[3,6,9,8]
print(any(e))#any
print(all(e))#all


#methods in list
k=[10,11,13,14]
k.append(15)
print(k)#to append 15 at end

l=[10,10,20,30]
l[1]=60
l.append([20,30])#append
print(l)
type(l[1])

l=[1,2,3,4]
l.extend([20,40])#extend
print(l)

l=[4,5,6,7,8,9,0]
l.remove(8)#remove
print(l)
l.pop()
print(l)#pop
l.pop(4)
print(l)#pop

b=[3,2,5,8,9]
b.insert(3,10)
print(b)#insert

c=[1,1,1,12,44,55,3,66,55,7,999,00,4,0,00]
i1=c.count(0)
print(i1)
c.count(55)
print(c.count(55))#count

i2=c.index(44)
print(i2)
i3=c.index(00)
print(i3)#index


#list varities
a=[[1,2],[3,4],[4,5]]
print(len(a))#nested list
print(len(a[1]))
print(len(a[2]))

a=[1,2,3,4]
b=[6,7,8,9,a]
print(a)
print(b)
b=[6,7,8,9,*a]#unpack list a in b
print(b)





































