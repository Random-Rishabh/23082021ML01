Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> ##2
>>> 5**9
1953125
>>> 3//2
1
>>> 7//3
2
>>> 7/3
2.3333333333333335
>>> 6==6
True
>>> a=20;a+=30;a%=3;print(a)
2
>>> True*False
0
>>> True&False
False
>>> True and False
False
>>> ((6>3) and (7<4) or (18==3)) and (9>3)
False
>>> True is False
False
>>> False in 'False'
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    False in 'False'
TypeError: 'in <string>' requires string as left operand, not bool
>>> ((True==False)or(False>True))and(False<=True)
False

###############################......3......################################

s1="Nice to have it"
s2="here"
s1+s2              ##'Nice to have ithere'

###############################......4......################################

a=[1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
a[3][1][2][0]     ##'hello'

###############################......5......################################

a.insert(0,s1); a.append(s2)
a                ##['Nice to have it', 1, 2, [3, 4], [5, [100, 200, ['hello']], 23, 11], 1, 7, 'here']

###############################......6......################################

numbers = [386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 
953, 345, 399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 
687, 217, 815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 
742, 717, 958,743, 527]

for i in numbers:
	if i!=237:
		if i%2==0:
			print(i,end = ' ')
	else:
		break
##386 462 418 344 236 566 978 328 162 758 918

###############################......6......################################

color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])
color_list_1.difference(color_list_2)

###############################......8......################################

alphab='abcdefghijklmnopqrstuvwxyz'
z=input('enter the string')
i=True
for q in alPha:
	if q not in z:
		i=False
if i==False:
	print("it is not a pangram")
else:
	print("it is a pangram")

###############################......9......################################

n=int(input("enter a number"))
print((3*n)+(20*n)+(100*n))

###############################......10......################################

>>> inp=input("enter the string")
enter the string23 54 12#98 3 17
>>> f,n=inp.split(sep ="#",maxsplit=2)
>>> qw=list(f.split(sep=" "))
>>> qw
['23', '54', '12']
>>> qw=[int(i) for i in qw]
>>> qe=list(n.split(sep=" "))
>>> qe=[int(i) for i in qe]
>>> print(qw,qe)

###############################......11......################################
ll=[];u=True
u=True
while u==True:
	x=input("enter string");ll.append(x)
	u=bool(input("want to rnter more(write something to enter more or nothing to stop, and press enter)"))
print(ll.sort())

###############################......12......################################

d = {'Student': ['Rahul','Kishore', 'Vidhya', 'Raakhi'], 
'Marks': [57,87,67,79]}
max=0;
 for i in d['Marks']:
	if i>max:max=i
print(d['Student'][d['Marks'].index(max)])

###############################......13......################################

z=input('enter a string')
a,m=0,0
 for i in z:
	if i.isalpha()==True:
		a+=1
	if i.isdigit()==True:
		m+=1
print("LETTERS ",a,"\nDIGITS ",m)

###############################......14......################################

