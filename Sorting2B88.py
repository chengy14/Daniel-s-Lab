#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd


# In[4]:


#Panda read csv
df=pd.read_csv('2b88Foldx_original.csv')


# In[5]:


#check if it read properly and delete null raw
df=df.dropna()


# In[6]:


#compartment sorting
Position6=df.loc[0:9,:]
sort6=Position6.sort_values(by=['Total Energy'] )
Position9=df.loc[10:19,:]
sort9=Position9.sort_values(by=['Total Energy'] )
Position10=df.loc[20:30,:]
sort10=Position10.sort_values(by=['Total Energy'] )
Position11=df.loc[31:40,:]
sort11=Position11.sort_values(by=['Total Energy'] )
Position13=df.loc[41:50,:]
sort13=Position13.sort_values(by=['Total Energy'] )
Position14=df.loc[51:60,:]
sort14=Position14.sort_values(by=['Total Energy'] )
Position15=df.loc[61:70,:]
sort15=Position15.sort_values(by=['Total Energy'] )
Position17=df.loc[71:80,:]
sort17=Position17.sort_values(by=['Total Energy'] )
Position18=df.loc[81:90,:]
sort18=Position18.sort_values(by=['Total Energy'] )
Position24=df.loc[91:100,:]
sort24=Position24.sort_values(by=['Total Energy'] )
Position25=df.loc[101:110,:]
sort25=Position25.sort_values(by=['Total Energy'] )
Position27=df.loc[111:120,:]
sort27=Position27.sort_values(by=['Total Energy'] )
Position28=df.loc[121:130,:]
sort28=Position28.sort_values(by=['Total Energy'] )
Position31=df.loc[131:140,:]
sort31=Position31.sort_values(by=['Total Energy'] )
Position32=df.loc[141:150,:]
sort32=Position32.sort_values(by=['Total Energy'] )
Position35=df.loc[151:160,:]
sort35=Position35.sort_values(by=['Total Energy'] )
Position36=df.loc[161:171,:]
sort36=Position36.sort_values(by=['Total Energy'] )


# In[7]:


#sorting result
df_sort=sort6.append(sort9).append(sort10).append(sort11).append(sort13).append(sort14).append(sort15).append(sort17).append(sort18).append(sort24).append(sort25).append(sort27).append(sort28).append(sort31).append(sort32).append(sort35).append(sort36)


# In[8]:


#save files
df_sort.to_csv('2b88Foldx_sorting.csv')


# In[9]:


df_sort.to_excel('2b88Foldx_sorting.xlsx')





