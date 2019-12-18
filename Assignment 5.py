#!/usr/bin/env python
# coding: utf-8

# In[9]:


a = int (input("Enter a positive number: "))
b = 1
for x in range(1,a+1):
    b = b*x
print ("Factorial of the number is: ")
print (b)


# In[17]:


a = input("Enter a string: ")
u = 0
l = 0
for x in a:
    if x.isupper():
        u = u + 1
    else:
        l = l + 1
print ("Number of upper case letters: ")        
print (u)
print ("Number of lower case letters: ")
print (l)


# In[18]:


l1 = [2, 32, 45, 15, 17, 18, 29, 66, 12]
for x in l1:
    if x%2 == 0:
        print (x)


# In[23]:


a = input("Enter a word: ")
a = a.casefold()
b = reversed(a)
if list(a) == list(b):
    print ("Given word is a palindrome")
else:
    print ("Given word is not a palindrome")


# In[35]:


num = int (input ("Enter a number: "))
if num > 1:
    
    
    for i in range(2,num):
        if (num % i) == 0:
            print(num,"is not a prime number")
            break
    else:
        print(num,"is a prime number")
else:
    print(num,"is not a prime number")


# In[39]:


a = input ("Enter elements from shopping list: ")
x = a.split(' ')
print ("List of items: ")
print (x)

