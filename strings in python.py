s='sanjana'
print(s)

s1="sanjana deepakbhai may"
print(s1)

a="be st"
f=a[2]
print(f)
b=a[0]
print(b)
c=a[1]
print(c)
d=a[-2]
print(d)
e=a[-1]
print(e)#indexing

#[start:end:step]# slicing
s="pdeucollege"
a=s[0:5] #end-1
print(a)
b=s[1:]#end(start exclude)
print(b)
c=s[:7] #end-1
print(c)
d=s[-2:]#end(start include)
print(d)
e=s[:-5]#beginning to end-1
print(e)
f=s[1:7:2]#start to end-1 with step
print(f)

a=int('0')
print(a)#type conversion

#orperators in string
s1='papa'
s2='best'
s3=s1+s2#concantation
print(s3)
s4='btu'+'3'#no error as 3 is in string here 
print(s4)

p1='hi'
p2=p1*3#repetation(*)
print(p2)
p3=p1*0
print(p3)

x1='namarata'
x2='nama'
print(x2 in x1)#membership(in)

#built in function:
a='siddhu'
#b=len(a) print(b)
      #OR
print(len(a))
print(min(a))
print(max(a))
print(type(a))
print(id(a))

#string methods
b=" degree"
print(b.upper())
print(b.lower())
print(b.capitalize())
print(b.title())
print(b.swapcase())
print(b.isalpha())
print(b.isdigit())
print(b.isalnum())
print(b.islower())
print(b.isupper())
print(b.startswith('d'))
print(b.endswith('i'))
print(b.count('e'))
print(b.find('r'))
print(b.find('g',1,2))
print(b.replace('g','k'))
print(b.strip())#or lstrip() or rstrip
sname, fname, surname = input('Enter your full name :').split()
print(sname,fname, surname)
#sname, fname, surname = input('Enter your full name with comma seperation:').split(',')
print("_".join("boss"))


#built in function for conversion of string to number and vice versa:
print(str(4))
print(int('9'))
print(float('9'))
print(complex('9'))
print(chr(98))
print(ord('N'))


def printstr(str1):

for ch in str1:# print the string character by character in one line.
    print(ch, end=' ')
print()
i= 0  # print the string character by character in different lines.
while i < len(str1):
    print(str1[i])
    i = i + 1

str1 = "pandit deendayal energy university"
printstr(str1)



























