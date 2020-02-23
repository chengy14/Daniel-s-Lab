#!/usr/bin/env python
# coding: utf-8

# In[28]:


import pandas as pd


# In[29]:


df=pd.read_csv('2b88Foldx.csv')


# In[30]:


df.head()


# In[55]:


Position6=df.loc[0:9,:]
sort6=Position6.sort_values(by=['Total Energy'] )


# In[56]:


Position9=df.loc[10:19,:]
sort9=Position9.sort_values(by=['Total Energy'] )


# In[57]:


Position10=df.loc[20:29,:]
sort10=Position10.sort_values(by=['Total Energy'] )


# In[69]:


Position11=df.loc[30:39,:]
sort11=Position11.sort_values(by=['Total Energy'] )
Position13=df.loc[40:49,:]
sort13=Position11.sort_values(by=['Total Energy'] )
Position14=df.loc[50:59,:]
sort14=Position11.sort_values(by=['Total Energy'] )
Position15=df.loc[60:69,:]
sort15=Position11.sort_values(by=['Total Energy'] )
Position17=df.loc[70:79,:]
sort17=Position11.sort_values(by=['Total Energy'] )
Position18=df.loc[80:89,:]
sort18=Position11.sort_values(by=['Total Energy'] )
Position24=df.loc[90:109,:]
sort24=Position11.sort_values(by=['Total Energy'] )
Position25=df.loc[110:119,:]
sort25=Position11.sort_values(by=['Total Energy'] )
Position27=df.loc[120:129,:]
sort27=Position11.sort_values(by=['Total Energy'] )
Position28=df.loc[130:139,:]
sort28=Position11.sort_values(by=['Total Energy'] )
Position31=df.loc[140:149,:]
sort31=Position11.sort_values(by=['Total Energy'] )
Position32=df.loc[150:159,:]
sort32=Position11.sort_values(by=['Total Energy'] )

Position35=df.loc[160:169,:]
sort35=Position11.sort_values(by=['Total Energy'] )
Position36=df.loc[170:179,:]
sort36=Position11.sort_values(by=['Total Energy'] )


# In[70]:


df_sort=sort6.append(sort9).append(sort10).append(sort11).append(sort13).append(sort14).append(sort15).append(sort17).append(sort18).append(sort24).append(sort25).append(sort27).append(sort28).append(sort32).append(sort35).append(sort36)


# In[76]:


df_sort.to_csv('2b88Foldx_sorting.csv')


# In[78]:


df_sort.to_excel('2b88Foldx.xlsx')


# In[ ]:




