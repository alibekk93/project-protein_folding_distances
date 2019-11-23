#!/usr/bin/env python
# coding: utf-8

# # Full matrix creator

# ## 0. Libraries

# In[22]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import seaborn as sns
import math
import sys


# ## 1. Load data

# In[2]:


##### Format:
##### AA
##### Amino Acid sequence
##### SS
##### Secondary Structure sequence


# In[21]:


# species = sys.argv[1]
# orders = str(sys.argv[2])

species = 'Tthermophilus'
orders = '3'

file_path = 'C:/Users/alibe/Desktop/Project/training_files/XXX/06_XXX_YYY_ZZZ'
file_path = file_path.replace('XXX', species).replace('ZZZ', orders)
path = file_path + '.trHMM'
training_file_1 = open(path.replace('YYY', species))
training_file_2 = open(path.replace('YYY', 'Ecoli'))


# In[13]:


lines_1 = training_file_1.read().splitlines()
AA_seq_1 = lines_1[1]
SS_seq_1 = lines_1[3]

lines_2 = training_file_2.read().splitlines()
AA_seq_2 = lines_2[1]
SS_seq_2 = lines_2[3]


# In[14]:


AA_list = ['*','A','C','D','E','F','G','H','I','K','L','M','N','P','Q','R','S','T','V','W','X','Y']

if file_path[-1] == '8':
    SS_list = ['*','B','C','E','G','H','I','S','T']
elif file_path[-1] == '3':
    SS_list = ['*','C','E','H']


# In[15]:


count_matrix_1 = np.zeros((len(SS_list), len(AA_list)))
count_matrix_2 = np.zeros((len(SS_list), len(AA_list)))


# ## 3. Fill matrices

# In[16]:


for i in range(len(AA_seq_1)):
    for j in range(len(AA_list)):
        if AA_seq_1[i] == AA_list[j]:
            for k in range(len(SS_list)):
                if SS_seq_1[i] == SS_list[k]:
                    count_matrix_1[k,j] += 1
    print('\r1st order: {:%}'.format(i / (len(AA_seq_1) - 1)), end = '')


# In[17]:


for i in range(len(AA_seq_2)):
    for j in range(len(AA_list)):
        if AA_seq_2[i] == AA_list[j]:
            for k in range(len(SS_list)):
                if SS_seq_2[i] == SS_list[k]:
                    count_matrix_2[k,j] += 1
    print('\r1st order: {:%}'.format(i / (len(AA_seq_2) - 1)), end = '')


# In[18]:


count_matrix_1 = pd.DataFrame(count_matrix_1, index=SS_list, columns=AA_list)
count_matrix_2 = pd.DataFrame(count_matrix_2, index=SS_list, columns=AA_list)


# ## 4. Save as CSV

# In[19]:


matrix_path_1 = file_path.replace('06', '09').replace('XXX', species).replace('YYY', species) + '_overall' + '.csv'
count_matrix_1.to_csv(matrix_path_1)


# In[20]:


matrix_path_2 = file_path.replace('06', '09').replace('XXX', species).replace('YYY', 'Ecoli') + '_overall' + '.csv'
count_matrix_2.to_csv(matrix_path_2)


# In[ ]:




