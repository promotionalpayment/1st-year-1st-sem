#!/usr/bin/env python
# coding: utf-8

# # PROGRAM 1A
# 
# ## Program to print the user given values
# 

# In[9]:


num =int(input("enter the integer value:"))
pi = float(input("enter the value of pi:"))
name = str(input("enter your name:"))
compval =complex(input("enter complex value :"))
boolean = bool(input("enter boolean value:"))
nonetype = None
#print the values of the variables
print("\n entered integer variable=", num)
print("\n entered pi value is=", pi)
print("\n entered name is=", name)
print("\n entered complex value is=", compval)
print("\n entered boolean value is=", boolean)
print("\n none type is:", nonetype)


# # BILL AMOUNT ------>PROGRAM 1 B

# ## to read and calculate the bill amt 

# In[49]:


name = str(input("enter the name of the item sold:"))
qty = float(input("enter the quantity of the item sold:"))
price = float(input("enter the price of the item sold:"))
disc = int(input("enter the discount percentage on the item sold:"))
tax = float(input("enter the tax percentage on the item sold:"))
grossamt = qty*price
discountamt =(disc/100)*grossamt
discountedprice=grossamt-discountamt
taxamt = discountedprice*(tax/100)
finalprice = taxamt+discountedprice
#here lies the bill

print("\n")
print("\n")
print("       ********************BILL***********************")
print("      ----Here lies the information of your purchase-----")
print("\n")
print("\tYou have purchased:",qty," ",name,"For  $",qty," each")
print("\t\t\t\t\t------------------")
print("\tYou have recieved a discount of  ",disc,"%")
print("\t\t\t\t\t------------------")
print("\tYour tax percentage is:        \t",tax,"%")
print("\t\t\t\t\t------------------")
print("\tYour price before discount is:\t$",grossamt) 
print("\t\t\t\t\t------------------")
print("\tYour discount amount is:      \t-$",discountamt)
print("\t\t\t\t\t------------------")
print("\tYour price after discount is:  \t$",discountedprice)
print("\t\t\t\t\t------------------")
print("\t\t\tTax:           \t+$",taxamt,)
print("\t\t\t\t\t------------------")
print("\t\tYour Subtotal is:  \t$",finalprice)
print("\n")
print("\n")
print("  ********************THANK YOU FOR YOUR PURCHASE********************")
print("  ***************Your purchase is of great value to us***************")
print("-------------------------------------------------------------------------")


# # PROGRAM 2A
# ## Develop a program to calc the roots of a quad eq

# In[56]:


import math
a=float(input("enter the value of coefficient a:" ))
b=float(input("enter the value of coefficient b:" ))
c=float(input("enter the value of constant c:" ))
disc=b*b-4*a*c
#program to calculate quadratic equation with real and distinct roots
if a==0:
    print("this is not a quadratic equation")
else:
    if disc>0:
        root1=(-b+math.sqrt(disc))/(2*a)
        root2=(-b-math.sqrt(disc))/(2*a)
        print("the equation has real and distinct roots")
        print("root 1=",root1," And"," root 2=",root2)
#calcs the root for an equation with real and equal roots
    elif disc==0:
        0
        root=-b/(2*a)
        print("the equation has real and equal roots")
        print("root =",root)
#for equations where roots are imaginary
    else:
        root=-b/(2*a)
        imgpart=math.sqrt(abs(disc))
        print("this equation has real and complex roots:",root,"+j",imgpart,)


    


# # PROGRAM 2B

# ## TO DEVELOP A PROGRAM TO CALCULATE THE SUM OF SQUARES OF EVEN NUMBERS UPTO N 

# In[4]:


n=int(input("enter the upper limit of the range:"))
s=0
#using loop to go through the entire range of numbers
for i in range(1,n+1):
    #to check if the number is even
    if(i%2==0):
        sqr=i*i
        term=sqr 
    else:
        term=0
    #calculating the sum of the squares of even number
    s=s+term
print("the sum of squares from 1 to ",n,"is=",s)    


# # PROGRAM 3A

# ## to develop a program to use the lambda function within an ordinary function 

# In[25]:


#defining a function
def add(x,y):
    #using lambda function to add two numbers
    return(lambda a,b:a+b)(x,y)
num1=int(input("enter one number:"))
num2=int(input("enter another number:"))
#calling the defined function
sum=add(num1,num2)
print("the answer is=",sum)


# # PROGRAM 3B

# ## TO DEVELOP A PROGRAM WHERE A SUB FUNCTION IS DEFINED IN ONE MODULE AND CALLED BY CODE IN ANOTHER MODULE(in 3 ways)

# In[36]:


import a
sum=a.add(1,2)
subtract=a.sub(3,2)
multiply=a.mult(3,2)
divide=a.div(36,6)
print("the sum is=",sum)
print("the answer is=",subtract)
print("the product is=",multiply)
print("the answer is=",divide)


# In[1]:


from a import add,sub,mult,div
sum=add(1,2)
subtract=sub(3,2)
multiply=mult(3,2)
divide=div(36,6)
print("the sum is=",sum)
print("the answer is=",subtract)
print("the product is=",multiply)
print("the answer is=",divide)


# In[2]:


from a import *
sum=add(1,2)
subtract=sub(3,2)
multiply=mult(3,2)
divide=div(36,6)
print("the sum is=",sum)
print("the answer is=",subtract)
print("the product is=",multiply)
print("the answer is=",divide)


# # PROGRAM 4A

# ## TO DEVELOP A PROGRAM TO ENCRYPT A PHRASE/ WORD THAT IS GIVEN BY THE USER AND DISPLAY THE ENCRYPTED WORD/PHRASE

# In[6]:


passcode=str(input("enter your password for encryption:"))
t=len(passcode)
print(t)


# In[9]:


passcode=str(input("enter your character for conversion:"))
t=ord(passcode)
print(t)
g=t+2
r=chr(g)
print(r)


# In[10]:


ord('A')


# In[24]:


#encrypt ypur password (with end)
passcode=input("enter your password for encryption:")
t=len(passcode)
i=0
for i in range(0,t):
    g=passcode[i]
    encrypt=ord(g)+5
    decrypt=chr(encrypt)
    print(decrypt,end='')
    
    


# In[27]:


#encrypt ypur password (without end)
passcode=input("enter your password for encryption:")
t=len(passcode)
i=0
for i in range(0,t):
    g=passcode[i]
    encrypt=ord(g)+5
    decrypt=chr(encrypt)
    print(decrypt)


# In[26]:


#decrypt your password
passcode=input("enter your encrypted password:")
t=len(passcode)
i=0
for i in range(0,t):
    g=passcode[i]
    encrypt=ord(g)-5
    decrypt=chr(encrypt)
    print(decrypt,end='')


# In[29]:


#without end
passcode=input("enter your password for encryption:")
t=len(passcode)
i=0
s=''
for i in range(0,t):
    g=passcode[i]
    encrypt=ord(g)+5
    decrypt=chr(encrypt)
    s=s+decrypt
print(s)    
    


# # PROGRAM 4B

# ## To develop  a program to accept a username and PAN and validate it using the isx() function.

# In[23]:


username=input("enter your username: ")
if username.isalpha()==False:
    print("Invalid Username")
else:
    print("Valid username")
    PAN=input("Enter your PAN:")
    if len(PAN)==10 and PAN[0:5].isalpha()==True and PAN[5:9].isdigit()==True and PAN[9].isalpha()==True:
        print("valid pan")
    else:
        print("Invalid pan")


# # PROGRAM 5A

# ## To develop a program to that reads a file line by line. Each line read  from the files is copied to another line with line number specified at the begining of the line.

# In[24]:


file1=open("C:/Users/DSUCSC006/KAILASNATHR(B13)/file1.txt","r")
file2=open("file2.txt","w")
i=1
for line in file1:
    file2.write(str(i)+":"+line)
    i+=1
file1.close()  
file2.close()
print("The lines should be copied by now.")    


# In[ ]:




