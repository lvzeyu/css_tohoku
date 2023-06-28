#!/usr/bin/env python
# coding: utf-8

# In[1]:


<details><summary>Answer</summary>

The two heads are getting the same input data so they will be calculating the same gradients and will end up learning the same thing. We have two options:

A. Feed the two networks different data. This would essentially mean training the two networks independently or restructuring our data so that batch sizes of treated and control units can be split equally after input.

B. Somehow ensure that each head only receives error gradients for the correct treatment group. This will require writing a custom loss function.

Let's go with B.
</details>


# In[ ]:




