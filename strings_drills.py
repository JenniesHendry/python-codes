#!/usr/bin/env python
# coding: utf-8

# In[1]:


input_string = 'the sky is blue'
reversed_string = ' '.join(input_string.split()[::-1])
print(reversed_string)


# In[1]:


text = "Never odd or even"

text = text.replace(" ", "").lower()

print(text == text[::-1])


# In[2]:


sentence = input("Enter a sentence: ")
char = input("Enter a character to count: ")

count = sentence.lower().count(char.lower())

print("Character appears", count, "times")


# In[3]:


s1 = "waterbottle"
s2 = "erbottlewat"

print(len(s1) == len(s2) and s2 in (s1 + s1))


# In[4]:


name = "  john   smith  "

tidy_name = " ".join(name.split()).title()

print(tidy_name)


# In[5]:


email = "john.smith@gmail.com"

name, domain = email.split("@")

masked_email = name[0] + "***@" + domain

print(masked_email)


# In[7]:


text = "Hello World"

vowels = (text.lower().count('a') +
    text.lower().count('e') +
    text.lower().count('i') +
    text.lower().count('o') +
    text.lower().count('u'))

print("Number of vowels:", vowels)


# In[8]:


item = "Coffee"
price = 3.5
receipt = f"{item:.<20}{price:6.2f}"

print(receipt)
print(len(receipt))


# In[11]:


print("Python strings are immutable, which means their contents cannot be changed after they are created. Once a string is assigned a value, any modification creates a new string instead of changing the original one. Immutability makes strings safer to use because their values cannot be accidentally modified. It also allows Python to optimize memory usage, support string hashing, and use strings reliably as dictionary keys and set elements.However, immutability can affect performance when concatenating strings inside a loop. Each concatenation may create a new string and copy the existing contents into it. Repeated concatenation can therefore cause unnecessary memory allocation and copying, making the process inefficient. Using `join()` with a list of strings is generally more efficient.")


# In[ ]:




