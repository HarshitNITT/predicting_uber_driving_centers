
# coding: utf-8

# In[140]:


import pandas as pd
data=pd.read_csv("./dataset/uber-raw-data-jul14.csv")
print type(data)
data.shape
# print data
data=data.dropna()
# data.isna()
# data['all_text'] = data['title'].astype(str) + data['author']+data['text']

# corpus=data['all_text'].values.tolist()
# data.timeStamp = pd.to_datetime(data.Date/Time)
# data['Date/Time']=data['Date/Time'].to_datetime.date()
data['Date/Time'] = pd.to_datetime(data['Date/Time'])
data['Date/Time'] = data['Date/Time'].dt.date
data
# print corpus[:6]
# vectorizer = CountVectorizer()
# X = vectorizer.fit_transform(corpus)


# In[141]:


from sklearn import preprocessing
le = preprocessing.LabelEncoder()
le.fit(data['Date/Time'].tolist())


# In[142]:


data['Date/Time']=pd.DataFrame(le.transform(data['Date/Time'].tolist()))
data


# In[143]:


from sklearn.cluster import AgglomerativeClustering

# 
X=data[['Date/Time','Lat','Lon']]
X_test=X[:10000]
# X_train=X[:3000]-X_test

# X_train, X_test, y_train, y_test = train_test_split(X_int.tolist(), Y, test_size=0.25, random_state=42)
clustering = AgglomerativeClustering(n_clusters=8).fit(X_test)
clustering.labels_


# In[144]:


from sklearn.neighbors import KNeighborsClassifier
KN = KNeighborsClassifier(n_neighbors=250)
KN.fit(X_test,clustering.labels_)

labels2 = KN.predict(X[:20000])


# In[145]:


# data['labels']=labels2


# In[146]:



# data=pd.DataFrame(labels2,columns=['label'])


# In[147]:


# df=df.reset_index()
data=data.reset_index()
data


# In[148]:


print len(labels2)


# In[164]:


print df
import matplotlib.pyplot as plt

fig,ax = plt.subplots(12,figsize=(10,40))
df=pd.DataFrame(labels2,columns=['label'])
dm=data[0:20000]
dm['label']=df['label']
print dm
print df
print dm['Date/Time']
scatter = ax[0].scatter(dm['Date/Time'],df['label'])
ax[0].set_title('Uber Driving centers')
ax[0].set_xlabel('Days')
ax[0].set_ylabel('Cluster')
colors = ['red','blue', 'green','black','orange','yellow','#00B7EB','purple']
scatter = ax[1].scatter(dm['Lat'],df['label'])
# plt.yticks(np.arange(dm['Lon'].min(), dm['Lon'].max(), 0.25))
scatter = ax[2].scatter(dm['Lat'],dm['Lon'],c=df['label'].apply((lambda x: colors[x])))
for i in range(0,8):
    scatter = ax[3+i].scatter(dm[dm['label']==(i)]['Lat'],dm[dm['label']==(i)]['Lon'],c=colors[i])
    ax[3+i].set_xlabel('Latitude')
    ax[3+i].set_ylabel('Longitude')
plt.show()


# In[48]:





# In[ ]:





# In[ ]:





# In[ ]:




