#!/usr/bin/env python
# coding: utf-8

# # Create .trHMM from BLAST results

# ## 0. Libraries

# In[2]:


import pandas as pd
import sys


# ## 1. Import data + filter

# In[ ]:


# species = sys.argv[1]

species = 'Bsubtilis'

file_path = 'C:/Users/alibe/Desktop/Project/training_files/XXX/04_XXX_BLAST'
path = file_path + '.csv'
BLAST_results = pd.read_csv(path, index_col = False)


# In[4]:


SS_data = pd.read_csv('C:/Users/alibe/Desktop/SS_data_processed.csv', index_col = False)


# In[5]:


BLAST_results_filtered = BLAST_results[BLAST_results['%Match'] >= 95]
BLAST_results_filtered = BLAST_results_filtered[BLAST_results_filtered['MatchLen'] >= 100]
BLAST_results_filtered = BLAST_results_filtered[BLAST_results_filtered['BitScore'] >= 200]


# In[6]:


BLAST_results_filtered.reset_index().to_csv(file_path.replace('04', '05') + '_results_filtered' + '.csv')


# In[7]:


BLAST_results_filtered = BLAST_results_filtered.reset_index()


# ## 2. Create lists

# In[8]:


DB_list = []
multiplier_list = []


# In[9]:


for i in range(len(BLAST_results_filtered)):
    DB_id = BLAST_results_filtered.DB_Seq.iloc[i]
    multiplier = int((len(DB_id) + 1) / 7)
    multiplier_list.append(multiplier)
    DB_list.append(DB_id.split('_'))


# In[10]:


Q_list = list(BLAST_results_filtered.Query)
QS_list = list(BLAST_results_filtered.QueryStart.astype(int))
QE_list = list(BLAST_results_filtered.QueryEnd.astype(int))
DBS_list = list(BLAST_results_filtered.DB_SeqStart.astype(int))
DBE_list = list(BLAST_results_filtered.DB_SeqEnd.astype(int))


# ## 3. Create lines for Query

# In[11]:


Q_AA = []
Q_SS = []


# In[12]:


for i in range(len(Q_list)):
    AA = SS_data.loc[SS_data['Name'] == Q_list[i], 'AA'].iloc[0]
    SS = SS_data.loc[SS_data['Name'] == Q_list[i], 'SS'].iloc[0]
    # cutting out non-matching parts
    AA = AA[QS_list[i] - 1 : QE_list[i]]
    SS = SS[QS_list[i] - 1 : QE_list[i]]
    # multiplication
    Q_AA.append(('*' + AA) * int(multiplier_list[i]))
    Q_SS.append(('*' + SS) * int(multiplier_list[i]))
    print('\rQ:{:%}'.format(i / (len(Q_list) - 1)), end = '')


# In[13]:


Q_AA_line = ''.join(Q_AA)
Q_8_SS_line = ''.join(Q_SS)
Q_3_SS_line = Q_8_SS_line.replace('S', 'C').replace('T', 'C').replace('B', 'E').replace('I', 'H').replace('G', 'H')


# ## 4. Create lines for DB

# In[14]:


DB_AA = []
DB_SS = []


# In[15]:


for i in range(len(DB_list)):
    for j in DB_list[i]:
        AA = SS_data.loc[SS_data['Name'] == j, 'AA'].iloc[0]
        SS = SS_data.loc[SS_data['Name'] == j, 'SS'].iloc[0]
        # cutting out non-matching parts
        AA = AA[DBS_list[i] - 1 : DBE_list[i]]
        SS = SS[DBS_list[i] - 1 : DBE_list[i]]
        # appending
        DB_AA.append('*' + AA)
        DB_SS.append('*' + SS)
    print('\rDB:{:%}'.format(i / (len(DB_list) - 1)), end = '')


# In[16]:


DB_AA_line = ''.join(DB_AA)
DB_8_SS_line = ''.join(DB_SS)
DB_3_SS_line = DB_8_SS_line.replace('S', 'C').replace('T', 'C').replace('B', 'E').replace('I', 'H').replace('G', 'H')


# ## 4. Create .trHMMs from lists

# In[17]:


Q_8_output_path = file_path.replace('BLAST', 'Ecoli').replace('04', '06') + '_8' + '.trHMM'
DB_8_output_path = file_path.replace('BLAST', species).replace('04', '06') + '_8' + '.trHMM'


# In[18]:


Q_3_output_path = file_path.replace('BLAST', 'Ecoli').replace('04', '06') + '_3' + '.trHMM'
DB_3_output_path = file_path.replace('BLAST', species).replace('04', '06') + '_3' + '.trHMM'


# In[19]:


Q_8_trHMM = open(Q_8_output_path, 'w')
Q_8_trHMM.write('>AA')
Q_8_trHMM.write('\n')
Q_8_trHMM.write(Q_AA_line)
Q_8_trHMM.write('\n')
Q_8_trHMM.write('>SS')
Q_8_trHMM.write('\n')
Q_8_trHMM.write(Q_8_SS_line)
Q_8_trHMM.close()


# In[20]:


DB_8_trHMM = open(DB_8_output_path, 'w')
DB_8_trHMM.write('>AA')
DB_8_trHMM.write('\n')
DB_8_trHMM.write(DB_AA_line)
DB_8_trHMM.write('\n')
DB_8_trHMM.write('>SS')
DB_8_trHMM.write('\n')
DB_8_trHMM.write(DB_8_SS_line)
DB_8_trHMM.close()


# In[21]:


Q_3_trHMM = open(Q_3_output_path, 'w')
Q_3_trHMM.write('>AA')
Q_3_trHMM.write('\n')
Q_3_trHMM.write(Q_AA_line)
Q_3_trHMM.write('\n')
Q_3_trHMM.write('>SS')
Q_3_trHMM.write('\n')
Q_3_trHMM.write(Q_3_SS_line)
Q_3_trHMM.close()


# In[22]:


DB_3_trHMM = open(DB_3_output_path, 'w')
DB_3_trHMM.write('>AA')
DB_3_trHMM.write('\n')
DB_3_trHMM.write(DB_AA_line)
DB_3_trHMM.write('\n')
DB_3_trHMM.write('>SS')
DB_3_trHMM.write('\n')
DB_3_trHMM.write(DB_3_SS_line)
DB_3_trHMM.close()


# In[ ]:




