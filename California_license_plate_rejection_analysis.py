#!/usr/bin/env python
# coding: utf-8

# In[71]:


import numpy as np
import pandas as pd

get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns


# In[72]:


from plotly import __version__
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot

print(__version__) # requires version >= 1.9.0


# In[73]:


# For Notebooks
init_notebook_mode(connected=True)


# In[172]:


df = pd.read_csv('applicationsUP1.csv')


# In[173]:


df.head(5)


# In[76]:


sns.set_style('whitegrid')


# In[77]:


df[df['status']=='Y'].head()


# In[82]:


s = df['review_reason_code'].value_counts()
w = df['review_reason_code'].value_counts()
new = pd.DataFrame({'review_reason_code':s.index, 'Count':s.values})
s


# In[146]:


plt.figure(figsize=(13,7))
sns.countplot(x='review_reason_code',data=df,hue='status',linewidth=2,order=df['review_reason_code'].value_counts().index,
              palette='viridis')
plt.title('California License Plates')
plt.xlabel('Rejection reasons')
plt.ylabel('Rejection count')
plt.legend(loc='upper right',bbox_to_anchor=(1.08,1.0))


# In[176]:


df1 = (df.groupby(['review_reason_code','status'])
         .apply(lambda x: (x['status']=='Y').value_counts()).reset_index(name='count'))


# In[177]:


df2=pd.DataFrame(df1)
df2


# In[156]:


import plotly.express as px


# In[157]:


#tickers = ['Sexual Connotations used','Vulgar term used','Swear word or term considered profane','negative connotation to a specific group',
#          'Misrepresents a law enforcement entity','Deleted from regular series license plates','Foreign or slang word or term']


# In[174]:


dfn = pd.read_csv('applicationsUP2.csv')


# In[178]:


df1n= (dfn.groupby(['review_reason_code','status'])
         .apply(lambda x: (x['status']=='Y').value_counts()).reset_index(name='count'))


# In[179]:


df2n=pd.DataFrame(df1n)
df2n


# In[194]:


x="review_reason_code"
y="count"
fig = px.bar(df2n, x="review_reason_code", y="count", color='status', barmode='group',
             height=600, width=900,title='California License Plate rejection',labels={x: 'Rejection reasons',y: 'Review count(Y/N)'})
fig.show()

