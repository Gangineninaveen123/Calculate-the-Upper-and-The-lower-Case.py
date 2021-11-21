#!/usr/bin/env python
# coding: utf-8

# In[1]:


def my_func(args):
    upper=0
    lower=0
    
    for i in args :
        if i.isupper()==True:
            upper+=1
          
        elif i.islower()==True:
            lower+=1
        else:
            pass
    print('No. of Upper case characters : ',upper)
    print('No. of Lower case Characters : ',lower)
    


my_func('The quick Brow Fox')
            


# In[ ]:




