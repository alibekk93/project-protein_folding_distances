#!/usr/bin/env python
# coding: utf-8

# # Data processing to create a table from ss file

# ## 0. Libraries

# In[1]:


import pandas as pd
import numpy as np
import sys


# ## 1. Import data

# In[2]:

path = sys.argv[1]
path_to_csv = sys.argv[2]
d_raw = open(path, 'r')


# In[3]:


d_lines = d_raw.readlines()


# ## 2. Create empty matrix

# In[4]:


n_seqs = 0
for line in d_lines:
    if line.count('>') >= 1:
        n_seqs += 1
n_seqs = int(n_seqs / 2)


# In[5]:


d_matrix = np.zeros((n_seqs, 4))


# In[6]:


d_processed = pd.DataFrame(d_matrix, columns = ['Name', 'AA', 'Name2', 'SS'])


# In[ ]:


n_lines = int(sys.argv[3])


# ## 3. Fill in matrix

# In[29]:


name_q = 0
q = 1
string_output = []
for i in range(n_lines):   #n_seqs
    x = list(d_lines[i].strip('\n'))   # line into single characters
    if x[0] == '>' and q % 2 != 0:
        # AA sequence name
        if len(string_output) != 0:
            d_processed['SS'][name_q] = ''.join(string_output)   # paste formed SS sequence as string into database
            name_q += 1   # iterate line of output database
            string_output = []
            print('\r{:%}'.format(i / n_lines), end = '')
        name = x[1:7]   # take sequence name
        d_processed['Name'][name_q] = ''.join(name)   # paste as string into database
        q += 1   # iterate AA / SS
    elif x[0] == '>' and q % 2 == 0:
        # SS sequence name
        if len(string_output) != 0:
            d_processed['AA'][name_q] = ''.join(string_output)   # paste formed AA sequence as string into database
            string_output = []
        name = x[1:7]   # take sequence name
        d_processed['Name2'][name_q] = ''.join(name)   # paste as string into database
        q += 1   # iterate AA / SS
    elif x[0] != '>' and q % 2 == 0:
        # AA sequence
        string_output += x   # add sequence string from line i
    elif x[0] != '>' and q % 2 != 0:
        # SS sequence
        string_output += x   # add sequence string from line i


# ## 4. Save table as .csv

# In[8]:


d_processed.to_csv(path_to_csv, index = False)


# In[ ]:




