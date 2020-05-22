#!/usr/bin/env python
# coding: utf-8

# In[42]:


arr = [int(x) for x in input().split()]


# In[43]:


even_number_sum = 0
negative_count = 0
for i in arr:
    if(i % 2 == 0):
        even_number_sum = even_number_sum + i
    if(i < 0):
        negative_count = negative_count + 1
print(even_number_sum)
print(negative_count)
    


# In[44]:


print(arr)


# In[47]:


largest = -100000
smallest = 1000000
for x in arr:
    if(x > largest):
        largest = x
    if(x < smallest):
        smallest = x
print(largest)
print(smallest)

