#!/usr/bin/env python
# coding: utf-8

# In[176]:


import pandas as pd
import numpy as np


# In[177]:


df = pd.read_csv("laptop_data.csv")
df.head()


# In[178]:


df.shape


# In[179]:


df.info()


# In[180]:


df.isnull().sum()


# In[181]:


df.duplicated().sum()


# In[182]:


df.drop(columns=["Unnamed: 0"],inplace=True)


# In[183]:


df.head()


# In[184]:


df['Ram']=df['Ram'].str.replace('GB','')
df['Weight']=df['Weight'].str.replace('kg','')


# In[185]:


df.head()


# In[186]:


df['Ram']=df['Ram'].astype('int32')
df['Weight']=df['Weight'].astype('float32')


# In[187]:


df.info()


# In[188]:


import seaborn as sns
import matplotlib.pyplot as plt


# In[189]:


sns.distplot(df["Price"])


# In[190]:


df['Company'].value_counts().plot(kind='bar')


# In[191]:


sns.barplot(x=df['Company'],y=df['Price'])
plt.xticks(rotation='vertical')
plt.show()


# In[192]:


df['TypeName'].value_counts().plot(kind='bar')


# In[193]:


sns.barplot(x=df['TypeName'],y=df['Price'])
plt.xticks(rotation='vertical')
plt.show()


# In[194]:


sns.distplot(df["Inches"])


# In[195]:


sns.scatterplot(x=df['Inches'],y=df['Price'],alpha=0.4)
plt.show()


# In[196]:


df['ScreenResolution'].value_counts()


# In[197]:


df['Touchscreen']=df['ScreenResolution'].apply(lambda x:1 if 'Touchscreen' in x else 0)


# In[198]:


df.sample(5)


# In[199]:


df['Touchscreen'].value_counts().plot(kind='bar')


# In[200]:


sns.barplot(x=df['Touchscreen'],y=df['Price'])


# In[201]:


df['Ips']=df['ScreenResolution'].apply(lambda x:1 if 'IPS' in x else 0)


# In[202]:


df.head()


# In[203]:


df['Ips'].value_counts().plot(kind='bar')


# In[204]:


sns.barplot(x=df['Ips'],y=df['Price'])


# In[205]:


new = df['ScreenResolution'].str.split('x',n=1,expand=True)


# In[206]:


df['X_res'] = new[0]
df['Y_res'] = new[1]


# In[207]:


df.head()


# In[208]:


df['X_res'].str.replace(',','').str.findall(r'(\d+.?\d+)').apply(lambda x:x[0])


# In[209]:


df['X_res']=df['X_res'].str.replace(',','').str.findall(r'(\d+.?\d+)').apply(lambda x:x[0])


# In[210]:


df.head()


# In[ ]:





# In[212]:


df.head()


# In[213]:


df.info()


# In[214]:


df['X_res']=df['X_res'].astype('int32')
df['Y_res']=df['Y_res'].astype('int32')


# In[215]:


df.info()


# In[216]:


df.select_dtypes(include='number').corr()['Price']


# In[217]:


df['ppi']=np.sqrt((df['X_res']**2)+(df['Y_res']**2))/df['Inches'].astype('float')


# In[218]:


df.head()


# In[219]:


df.select_dtypes(include='number').corr()['Price']


# In[220]:


df.drop(columns=["ScreenResolution"],inplace=True)


# In[221]:


df.head()


# In[222]:


df.drop(columns=["Inches","X_res","Y_res"],inplace=True)


# In[223]:


df.head()


# In[224]:


df['Cpu'].value_counts()


# In[225]:


df['Cpu Name']=df['Cpu'].apply(lambda x:" ".join(x.split()[0:3]))


# In[226]:


df.head()


# In[227]:


def fetch_processor(text):
       if text == 'Intel Core i7' or text == 'Intel Core i5' or text == "Intel Core i3":
           return text
       else:
           if text.split()[0] == 'Intel': 
               return 'Other Intel Processor'
           else:
               return 'AMd Processor'


# In[228]:


df['Cpu brand'] = df['Cpu Name'].apply(fetch_processor)


# In[229]:


df.head()


# In[230]:


df['Cpu brand'].value_counts().plot(kind='bar')
plt.xticks(rotation=20)
plt.show()


# In[231]:


sns.barplot(x=df['Cpu brand'],y=df['Price'])
plt.xticks(rotation=20)
plt.show()


# In[232]:


df.drop(columns=['Cpu','Cpu Name'],inplace=True)


# In[233]:


df.head()


# In[234]:


df['Ram'].value_counts().plot(kind='bar')


# In[235]:


sns.barplot(x=df['Ram'],y=df['Price'])
plt.xticks(rotation=20)
plt.show()


# In[236]:


df['Memory'].value_counts()


# In[237]:


df['Memory'] = df['Memory'].astype(str).replace('\.0', '', regex=True)
df["Memory"] = df["Memory"].str.replace('GB', '')
df["Memory"] = df["Memory"].str.replace('TB', '000')

new = df["Memory"].str.split("+", n=1, expand=True)
df["first"] = new[0].str.strip()
df["second"] = new[1]

df["Layer1HDD"] = df["first"].apply(lambda x: 1 if "HDD" in x else 0)
df["Layer1SSD"] = df["first"].apply(lambda x: 1 if "SSD" in x else 0)
df["Layer1Hybrid"] = df["first"].apply(lambda x: 1 if "Hybrid" in x else 0)
df["Layer1Flash_Storage"] = df["first"].apply(lambda x: 1 if "Flash Storage" in x else 0)

df['first'] = df['first'].str.extract('(\d+)')  
df['first'] = df['first'].fillna(0).astype(int) 

df["second"] = df["second"].fillna("0")  

df["Layer2HDD"] = df["second"].apply(lambda x: 1 if isinstance(x, str) and "HDD" in x else 0)
df["Layer2SSD"] = df["second"].apply(lambda x: 1 if isinstance(x, str) and "SSD" in x else 0)
df["Layer2Hybrid"] = df["second"].apply(lambda x: 1 if isinstance(x, str) and "Hybrid" in x else 0)
df["Layer2Flash_Storage"] = df["second"].apply(lambda x: 1 if isinstance(x, str) and "Flash Storage" in x else 0)

df['second'] = df['second'].str.extract('(\d+)')  # Extract only numeric values
df['second'] = df['second'].fillna(0).astype(int)  # Convert to integer safely

df["HDD"] = (df["first"] * df["Layer1HDD"] + df["second"] * df["Layer2HDD"])
df["SSD"] = (df["first"] * df["Layer1SSD"] + df["second"] * df["Layer2SSD"])
df["Hybrid"] = (df["first"] * df["Layer1Hybrid"] + df["second"] * df["Layer2Hybrid"])
df["Flash_Storage"] = (df["first"] * df["Layer1Flash_Storage"] + df["second"] * df["Layer2Flash_Storage"])

df.drop(columns=['first', 'second', 'Layer1HDD', 'Layer1SSD', 'Layer1Hybrid',
                 'Layer1Flash_Storage', 'Layer2HDD', 'Layer2SSD', 'Layer2Hybrid',
                 'Layer2Flash_Storage'], inplace=True)





# In[241]:


df.sample()


# In[242]:


df.drop(columns=['Memory'],inplace=True)


# In[243]:


df.head()


# In[245]:


df.select_dtypes(include='number').corr()['Price']


# In[246]:


df.drop(columns=['Hybrid','Flash_Storage'],inplace=True)


# In[247]:


df.head()


# In[248]:


df['Gpu'].value_counts()


# In[249]:


df['Gpu brand'] = df['Gpu'].apply(lambda x:x.split()[0])


# In[250]:


df.head()


# In[251]:


df['Gpu brand'].value_counts()


# In[252]:


df = df[df['Gpu brand'] != 'ARM']


# In[253]:


df['Gpu brand'].value_counts()


# In[254]:


sns.barplot(x=df['Gpu brand'],y=df['Price'],estimator=np.median)
plt.xticks(rotation='vertical')
plt.show()


# In[255]:


df.drop(columns=['Gpu'],inplace=True)


# In[256]:


df.head()


# In[257]:


df['OpSys'].value_counts()


# In[258]:


sns.barplot(x=df['OpSys'],y=df['Price'])
plt.xticks(rotation='vertical')
plt.show()


# In[259]:


def cat_os(inp):
    if inp == 'Windows 10' or inp == 'Windows 7' or inp == 'Windows 10 S':
        return 'Windows'
    elif inp == 'macOS' or inp == 'Mac OS X':
        return 'Mac'
    else:
        return 'Others/No OS/Linux'


# In[260]:


df['os'] = df['OpSys'].apply(cat_os)


# In[261]:


df.head()


# In[262]:


df.drop(columns=['OpSys'],inplace=True)


# In[263]:


sns.barplot(x=df['os'],y=df['Price'])
plt.xticks(rotation='vertical')
plt.show()


# In[265]:


sns.distplot(df['Weight'])


# In[266]:


sns.scatterplot(x=df['Weight'],y=df['Price'])


# In[267]:


df.select_dtypes(include='number').corr()['Price']


# In[269]:


sns.heatmap(df.select_dtypes(include='number').corr())


# In[270]:


sns.distplot(np.log(df['Price']))


# In[276]:


X = df.drop(columns=['Price'])
y = np.log(df['Price'])


# In[305]:


from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.15,random_state=2)


# In[306]:


from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.metrics import r2_score,mean_absolute_error


# In[307]:


from sklearn.ensemble import RandomForestRegressor


# In[413]:


col_transformer = ColumnTransformer(
    transformers=[
        ('onehot', OneHotEncoder(sparse_output=False, drop='first'), [0, 1, 7, 10, 11])
    ], 
    remainder='passthrough'
)

rf_regressor = RandomForestRegressor(
    n_estimators=74,      
    random_state=5,         
    max_samples=0.8,        
    max_features=1,    
    max_depth=19,           
)

pipe = Pipeline([
    ('preprocessor', col_transformer),
    ('regressor', rf_regressor)
])


pipe.fit(X_train, y_train)

y_pred = pipe.predict(X_test)

print('R2 Score:',r2_score(y_test, y_pred))
print('MAE:', mean_absolute_error(y_test, y_pred))


# In[414]:


import pickle


# In[415]:


pickle.dump(df,open('df.pkl','wb'))
pickle.dump(pipe,open('pipe.pkl','wb'))


# In[ ]:




