#1 check given number is armstrong number or not 
'''num=eval(input('enter any three digit number:'))
def armstrong(n):
    s=0
    while n>0:
        digit=n%10
        s+=digit**3
        n//=10
    if num==s:
        print(num,'is a armstrong number')
    else:
        print(num,'is not a armstrong number')
armstrong(num)

'''

#2 print fibonacci series for below n number

'''num=eval(input('enter any number:'))
def fibonacci(n):
    t1=0
    t2=1
    for i in range(10000):
        temp=t1+t2
        t1=t2
        t2=temp
        if t1>=n:
            break
        print(t1)
fibonacci(num)
'''
#3 write a python function to print first 10 fibonacci series numbers
'''num=eval(input('enter any number:'))
def fibonacci(n):
    t1=0
    t2=1
    lst=[0]
    temp=0
    while temp<10000:
        temp=t1+t2
        t1=t2
        t2=temp
        lst.append(t1)
        if len(lst)==n:
            break

    for i in lst:
        print(i)

fibonacci(num)
'''

#4 write a python function to print the given three values in asc and desc

'''a=eval(input('enter first value:'))
b=eval(input('enter second value:'))
c=eval(input('enter third value:'))

def orderofvalues(x,y,z):
    if x>y and x>z:
          if y>z: 
                print('the desc order is ',x,y,z) 
                print('the asc order is',z,y,x) 
          else: 
                print('the desc order is ',x,z,y) 
                print('the asc order is ',y,z,x) 
    elif y>x and y>z: 
        if x>z: 
                print('the desc order is ',y,x,z) 
                print('the asc order is ',z,x,y) 
        else: 
                print('the desc order is ',y,z,x) 
                print('the asc order is',x,z,y) 
    elif z>x and z>y: 
        if x>y: 
                print('the desc order is ',z,x,y) 
                print('the asc order is ',y,x,z) 
        else: 
                print('the desc order is ',z,y,x) 
                print('the asc order is ',x,y,z) 
 
orderofvalues(a,b,c) 
  '''
# 5 Write a Python to check the marital status, gender and age 
 
'''marsta=input("Enter marital status(married or single): ").lower() 
gen=input("Enter your gender(male or female): ").lower() 
age=int(input("Enter your age: ")) 
 
 
if marsta=="married": 
    print("You are not allowed to marry again") 
elif marsta=="single": 
    if gen=="male": 
        if age>=21: 
            print("Congrates, You are eligible to marry") 
        else: 
            print("Sorry, You are not eligible to marry") 
    elif gen=="female": 
        if age>=18: 
            print("Congrates, You are eligible to marry") 
        else: 
            print("Sorry, You are not eligible to marry") 
    else: 
        print('You entered invalid gender') 
else: 
    print("You entered invalid marital status")
'''

#6 write a python function to remove vowels from given string
'''st=input('enter any string:')
v='AEIOUaeiou'
st=list(st)
for i in st:
    if i in v:
        st=st.replace(i,'')

    st=''.join(st)
print(st)
'''
#7 write a python function to copy a given string into new varaiable and count how many characters are copied
'''st=input('enter any string:')
def copystring(st):
    c=0
    st1=''
    for i in st:
        st1+=i
        c=c+1

    print(st1)
    print(c)
copystring(st)
'''
#8 write a python function to count no.of digits is a given number
'''num=input('enter any number:')
def countdigit(n):
    n1=len(n)
    print(n1)
countdigit(num)
'''
#9 write a python function to print power values based on two given base and exponent values
'''base=eval(input('enter base value:'))
exp=eval(input('enter exponent value:'))
def power(m,n):
    x=base**exp
    print(x)
power(base,exp)
'''
#10  write a python function to check whether user given string or number
'''x=input('enter either string or  number:')

def stringnumber(m):
    if m.isalpha()==True:
        print(x,'is a string value')
    elif m.isnumeric()==True:
        print(x,'is a number value')
    elif m.isalnum()==True:
        print(x,'is a alpha-numeric value')
    else:
        print(x,'is not a completer string or number or alpha-numeric value')


stringnumber(x)
'''

#11 write a python function to check whether the given character is vowel or consonant
'''char=input('enter any charcter:')
def vowel(ch):
    vowel='aeiouAEIOU'
    if ch in vowel:
        print(char,'is a vowel')
    else:
        print(char,'is a consonant')

vowel(char)
'''

#12 write a python function to print the following pattern
'''n=4
def pattern(n):
    for i in range(n):
        for j in range(n):
            print('*',end='')
        print('\n')

pattern(n)
'''

#13 write a python function to print the following pattern
'''n=4
def pattern(n):
    for i in range(n+1):
        for j in range(i):
            print('*',end='')
        print('\n')

pattern(n)
'''

#14 write a python function to print the following pattern
'''n=5
def pattern(n):
    k=0
    for i in range(1,n+1):
        for j in range(1,(n-i)+1):
            print(end=' ')
        while(k!=(2*i-1)):
            print('*',end='')
            k=k+1
        k=0
        print('\n')

pattern(n)
'''

#15  write a python function to print the following pattern

'''n=4
def pattern(n):
    m=8
    for i in range(n+1):
        for j in range(m):
            print(end='')
        m=m-2
        for k in range(i+1):
            print('*',end='')
        print()
pattern(n)
'''
#16 write a python function to print the following pattern

'''n=5
def pattern(n):
    for i in range(n+1):
        for j in range(1,(n-i)+1):
            print('*',end='')
        print()
pattern(n)
'''

            
            
            




        
        
