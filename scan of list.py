#scan the list
l=[]
n=int(input())
for i in range(n):
    no=int(input("enter element"))
    l.append(no)
print(l)  


l=[]
n=input("enter all elements").split(',')
print(n)#in string form


Lint=[]
lstr=(input("enter element")).split(',') #take ele i.e string
for ele in lstr:
    Lint.append(int(ele)) #typecast into int and then append
print(Lint)


Lint=[]
lstr=(input("enter element")).split(',')
print(lstr)#take ele i.e string
for ele in lstr:
    n=int(ele)
    Lint.append(n) #typecast into int and then append
print(Lint)

#for 2D into 1D
for ele in l:
    if (type(ele)=="list"):
      lnew.extend(ele)
    else:
        lnew.append(ele)



