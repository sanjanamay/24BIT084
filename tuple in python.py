t1=(18,9,3,'namarata',"hirva")#tuple may or maynot be of similar objects 
print(t1)
print(t1[0])
print(t1[1:4])#accessing tuple

#names[0]='harsita'immutable
#num[0:2]=[20,30] not possile

a1=(11) #take as int value not tupe1
print(a1)
a2=(11,)#take a2 tuple(print single element in tuple)
print(a2)

b1=(11)*5
print(b1)#not a tuple
b2=(11,)*5
print(b2)#repetation in tuple

tp1=(99,100,101)
tp2=tp1+(102,103,104)#concatenated
print(tp2)

tp3=tp1+tp2#merge of two string
print(tp3)

t=tuple('parmar')#conversion of string/set/list into tuple
print(t)

num1=(15,7,88)
num2=num1
print(num1 is num2)#aliasing
print(num1,num2)

ele1=(99,100,101)
ele2=()
ele2=ele2+ele1
print(ele1 is ele2)#cloning
print(ele1,ele2)

tpl=(1,2,3,4)
print(3 in tpl)#searching

id1=(11,22,33,44,55)
id2=(11,22,33,44,55)
id3=id1
print(id1 is id2, id1 is not id2,id1 is id3)#identity

co1=(1,2,3,4)
co2=(1,2,4,5)
print(co1>co2)#comparision

emp=()
if not emp:
    print("empty tuple")
print(bool(emp))#emptiness



#BULIT IN FUNCTION ON TUPLE
dig=(1,2,3,4,5,6,7,8,9,10)
print( "length=",len(dig))#len
print( "maximum=",max(dig))#max
print( "minimum=",min(dig))#min
print( "sum=",sum(dig))#min
n=(9,6,7,3,00)
#del(n[3]) print(n)#delete
e=[3,6,9,8]
print(any(e))#any
print(all(e))#all

#sorted and reversed function in tupel return a list
v=(9,6,7,3,00,100,88,67)
v1=reversed(v)#reversed {CAN'T GET REVERSED OBJECT IN OUTPUT}
print(v1)
v2=sorted(v) #sorted
print(v2)
v3 = sorted(v, reverse = True)#{WHY THIS GIVE OUTPUT IN TUPEL NOT IN LIST}
print(v)

#TUPEL METHODS
c=(1,1,1,12,44,55,3,66,55,7,999,00,4,0,00)
i1=c.count(0)
print(i1)
c.count(55)
print(c.count(55))#count

i2=c.index(44)
print(i2)
i3=c.index(00)
print(i3)#index

#LOOPS IN TUPEL
num=(10,20,30,40,50)
for i in num:
  print (i) #using for loop on element

i=0
for i in range(len(num)):
       print(num[i])#can be also as: print("num[i]",i)
       i=i+1# using for loop on index


i = 0
while i < len(num): #using while loop
   print(num[i])
   i = i + 1
    
for index, a in enumerate(num):
          print (index, a)#using enumerate() to keep track of index


#list varities
a = (1,3,5,7,9)
b = (2,4,6,8,10)
c = (a,b)
print(c)

a=(1,2,3,4)
b=(6,7,8,9,a)#embdded a tupel into another
print(a)
print(b)
b=(6,7,8,9,*a)#unpack list a in b
print(b)

t=(11,12,[13,14,15],16,17)#a list inside tuple
print(t)
#t[0]=20 error index cannot be 0,1,3,4 as tuple is immutable
t[2][1]=20
print(t)

l=[11,12,(13,14,15),16,17]#a tuple inside loop
print(t)





































