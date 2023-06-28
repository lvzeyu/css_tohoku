#!/usr/bin/env python
# coding: utf-8

# # pandas
# 
# pandas はデータ分析によく用いられるパッケージであり、データの操作や解析、可視化などを行うための機能を提供します。

# In[1]:


import pandas as pd


# ## pandasのデータ構造
# 
# pandasには```Series```と```DataFrame```の２つの種類のオブジェクト型があります。
# 
# ### Series
# 
# ```Series```は一次元の配列ようなオブジェクトです。```Series```には値とそれに関連付けられたインデックスというデータラベルの配列が含まれます。

# In[2]:


obj=pd.Series([1,2,3,4,5])
obj


# In[3]:


obj.values


# In[4]:


obj.index


# ```Series```から一つの値や複数の値を参照する時にインデックスのラベルを使って指定することができます。

# In[5]:


obj[0]


# In[6]:


obj[[0,3]]


# 条件指定によるフィルタリング、スカラー値の掛け算、数学的な関数の適用など```NumPy```の関数と似ているような操作が可能です。
# 
# そこで、インデックスと値の関連が常に保持されます。

# In[7]:


obj[obj>3]


# In[8]:


obj*2


# 辞書形式のデータから```Series```を作成することも可能です。

# In[9]:


population_dict = {
    '東京': 13929286,
    '横浜': 3723392,
    '大阪': 2691004,
    '名古屋': 2390411,
    '札幌': 1952356,
    '神戸': 1538316,
    '京都': 1474570,
    '福岡': 1532591,
    '広島': 1196564,
    '仙台': 1098330
}

# 辞書からSeriesを作成
population_series = pd.Series(population_dict)

population_series


# In[10]:


population_series[["東京","仙台"]]


# ### DataFrame
# 
# データフレームはテーブル形式のデータ構造になって、行と列の両方のインデックスを持っています。
# 
# ![](./Figure/dataframe.svg)
# 

# データフレームを作成する方法はたくさんありますが、最も一般的な方法は、同じ長さを持つリスト型のバリューを持った辞書から作成します。

# In[11]:


data_dict = {
    'City': ['東京', '横浜', '大阪', '名古屋', '札幌', '神戸', '京都', '福岡', '広島', '仙台'],
    'Population': [13929286, 3723392, 2691004, 2390411, 1952356, 1538316, 1474570, 1532591, 1196564, 1098330],
    'Income': [754, 602, 615, 530, 535, 535, 490, 477, 457, 444]
}

# 辞書からDataFrameを作成
df = pd.DataFrame(data_dict)


# 作成されたデータフレームは、```Serise```と同じように自動的にインデックスが代入されます。

# In[12]:


df


# ## データの読み書き
# 
# pandasの特徴は、テーブル形式のデータをデータフレームオブジェクトとして読み込む[関数](https://pandas.pydata.org/docs/reference/io.html)がたくさんあることです。
# 
# 例えば、CSV ファイルを読み込むための```pd.read_csv()``という関数が用意されています。 こちらを使って CSV ファイルを読み込みます。

# In[13]:


df=pd.read_csv("./Data/titanic.csv")


# In[14]:


df


# データフレームをファイルに書き出せます。

# In[15]:


#df.to_csv("./Data/titanic.csv")


# ## 統計量の算出
# 
# データフレームには、中のデータに対し統計量を計算するための[メソッド](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.mean.html)も用意されています。

# In[16]:


df["age"].mean()


# In[17]:


df["age"].var()


# In[18]:


df["age"].sum()


# In[19]:


# 頻度
df["age"].value_counts()


# ## インデックス参照、選択、フィルタリング

# In[20]:


df["sex"]


# In[21]:


df[["sex","age"]]


# In[22]:


df[:5]


# In[23]:


df[df["age"]>70]


# ```loc```と```iloc```を使うことで、データフレームから行や列の一部分を選択することができます。
# - 軸ラベルを使うときは```loc```
# - 整数のインデックス位置による参照を使うときは```iloc```

# In[24]:


df.loc[96,['name','age']]


# In[25]:


df.iloc[96,[1,3]]


# 条件を指定して選択した要素に対し、値の書き換えを行うことができます。

# In[26]:


df.loc[df["age"]<1, ['age']] = 1


# ````{tab-set}
# ```{tab-item} 実習問題
# 年齢が30-50歳の男性のデータを取り出し、Name, Age, Sexを示してください。
# ```
# ````

# ## ソート
# 
# pandasは、データを一定の基準でソートする機能を提供しています。
# 
# 行や列のインデックスをソートするためには、```sort_index()```メソッドを使います。

# In[27]:


df.sort_index(ascending=False)


# In[28]:


df.sort_index(axis=1)


# 値によってソートするためには、```sort_values()```メソッドを使います。
# 
# デフォルトでは、欠損値が末尾にソートされます。

# In[29]:


df.sort_values(by="age")


# ```sort_values()```に複数なソートキーを指定することもできます。

# In[30]:


df.sort_values(by=["age","embarked"])


# ## マッピング

# - ```map()```メソッドは、Seriesオブジェクト内の各要素に対して、指定した辞書や関数を適用して新しい値を返す方法です。

# In[31]:


male={"male":0,
      "female":1}
df["male"]=df["sex"].map(male)
df


# In[32]:


def male_dummay(sex):
    if sex=="male":
        return 1
    elif sex=="female":
        return 0
    else:
        return sex
    
df["male"]=df["sex"].map(male_dummay)
df


# - ```apply()```メソッドは、DataFrameオブジェクトの列に対して関数を適用する方法です。

# In[33]:


def male_dummay(sex):
    if sex=="male":
        return 1
    elif sex=="female":
        return 0
    else:
        return sex
    
df["male"]=df["sex"].apply(male_dummay)
df


# ````{tab-set}
# ```{tab-item} 実習問題1
# ラムダ関数を適用する形で男性ダミー変数を作成しよう。
# ```
# 
# ```{tab-item} 実習問題2
# Cabin変数によって、頭文字で新しいカテゴリ変数を作成しよう。例えば、C105の場合はCに変更します。
# ```
# 
# ````

# ## 欠損値の取扱い
# 欠損値を含むデータの場合、一部の行の値が欠損している列に ```NaN``` (Not a Number)、```None```、```NaT``` (Not a Time) などが含まれる場合があります。 
# ### 欠損値を削除する

# In[34]:


# df[df.notnull()]
df.dropna()


# 行ではなく列を削除する場合は、```axis=1```を指定します。

# In[35]:


df.dropna(axis=1)


# 特定の列に基づく欠損値を削除することも可能です。

# In[36]:


df.dropna(subset=["age"])


# ### 欠損値の穴埋め
# 
# 欠損値への対策としては、欠損値を特定の値で補完するという方法が考えられます。
# 
# ```fillna```メソッドに何らかの値を引数として与えて呼び出すと、その値で欠損値を置き換えることができます。

# In[37]:


df.fillna(0)


# 平均を使った欠損値の補完する方法がよく用いられます。

# In[38]:


mean_age = df["age"].mean() # まずは、補完に使用する平均値の計算を行います
df["age"].fillna(mean_age,inplace=True) # inplace=Trueで元のデータを変更
df


# In[ ]:





# ## データのグループ化

# 
