#!/usr/bin/env python
# coding: utf-8

# # scikit-learn
# 
# scikit-learnには、データの読み込みと変形、様々な機械学習アルゴリズムの効率的な実装、モデル選択や評価の仕組みを統一されるAPIで提供されています。
# 
# この一貫性により、ある種類のモデルでscikit-learnの基本的な使い方と構文を理解したなら、新しいモデルやアルゴリズムへの切り替えは簡単です。

# ## 機械学習
# 
# 機械学習は、コンピュータが大量のデータを学習することで、データの中に潜むパターンと規則性を抽出する技術です。ここで、「学習」は、観察されたデータをモデルに適合させるための調整可能な「パラメータ」を与えるために行われます。
# 
# 最も基本的なレベルにおいて、機械学習は「教師あり学習」と「教師なし学習」の二つに分類できます。
# 
# - 教師あり学習（Supervised Learning）：教師あり学習では、入力データ（特徴量）とそれに対応する正解ラベル（目標値）のペアを使用してモデルを訓練します。モデルは、入力データと正解ラベルの間の関係やパターンを学習し、未知の入力データに対して正しい予測や分類を行うことが期待されます。
# 教師あり学習の代表的なタスクには、分類（クラスの予測）や回帰（数値の予測）があります。例えば、手書き数字の画像を入力として与え、それぞれの画像がどの数字に対応するのかを予測する手法や、住宅価格を予測する回帰モデルなどがあります。
# 
# - 教師なし学習（Unsupervised Learning）：教師なし学習では、正解ラベルを使わずに入力データのみを使用してモデルを訓練します。モデルはデータ内のパターンや関連性を自動的に発見し、データをクラスタリング（類似したデータのグループ化）や次元削減データの特徴量を圧縮)などの方法で解析します。例えば、顧客セグメンテーションにおいて、似た行動パターンを持つ顧客をグループ化するために教師なし学習を使用することができます。
# 
# 機械学習は、基本的に以下の手順で構成されます。
# 
# - データセットの構築
# - 性能指標の選択
# - 学習アルゴリズムの実装
# - モデル性能の評価
# 

# ## scikit-learnのデータ表現

# In[1]:


from sklearn import datasets
iris= datasets.load_iris()


# ### 特徴行列
# 
# データの情報が数値配列はまた行列と考えることができます。これを「特徴行列」と呼びます。
# 
# 一般的には、特徴行列は、$「nサンプル,m特徴」$をもつ配列で格納されます。
# 
# アイリスデータセットを例にして考えてみましよう。
# - データの各行は、観測された一つのサンプルを表します。
# - データの各列は、各サンプルの特徴を表す量的情報を持ちます。

# In[2]:


iris.data


# ### 目的配列
# 
# 特徴行列に対して、サンプルの長さを持つラベルや目的配列も扱います。
# 
# アイリスデータセットの場合、アイリスの種類を表す数値ラベルが目的配列と見なされます。

# In[3]:


iris.target


# In[4]:


import pandas as pd
iris_df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
# Add the target variable to the DataFrame
iris_df['target'] = iris.target
iris_df.head()


# ## scikit-learnのAPI
# 
# scikit-learnは、各機械学習アルゴリズムと幅広い機械学習アプリケーションに一貫したインタフェースを提供するAPIを通じて実装されています。
# 
# scikit-learnでは、以下の手順でデータからモデルの学習を行います。
# 
# - 適切なモデルを選択し、Estimatorクラスをインポートします。
# - モデルのハイパーパラメータの選択とインスタンス化
# - データの準備
#   - 教師あり学習では、特徴量・ラベルデータをモデル学習用の訓練データとモデル評価用のテストデータに分ける
#   - 教師なし学習では、特徴量データを準備
# - インスタンスの```fit()```メソッドを呼び出し、学習を行う
# - モデルの評価
#   - 教師あり学習では、```predict()``` メソッドを用いてテストデータの特徴量データからラベルデータを予測しその精度の評価を行う
#   - 教師なし学習では、```transform()``` または ```predict()``` メソッドを用いて特徴量データのクラスタリングや次元削減などを行う

# ### 教師あり学習・分類の例
# 
# アイリスデータセットを用いて花の4つの特徴から3つの花の種類を分類するタスクを考えてみましょう。
# 
# #### モデルのクラスの選択
# 
# scikit-learnでは、全てのモデルはPythonクラスとして実装されており、ここでは分類を行うモデルの1つであるロジスティック回帰 ([```LogisticRegression```](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html)) クラスをインポートしています。

# In[5]:


from sklearn.linear_model import LogisticRegression


# #### モデルのハイパーパラメータの選択
# 
# モデルのクラスに応じて、ハイパーパラメータでモデルを調整することは可能です。

# In[6]:


model=LogisticRegression(solver='lbfgs',  multi_class='auto')


# ### データの準備
# 
# 教師あり学習では、特徴量(特徴行列)・ラベルデータ(目的行列)をモデル学習用の訓練データとモデル評価用のテストデータに分ける必要があります。
# 
# - 基本的には、特徴量のサンプルとラベルのサンプルを同じ長さに保つ必要があります。ここでは、アイリスデータセットは既に正しい形式で整形されました。
# - ```train_test_split()``` でデータセットを訓練データとテストデータに分割できます。ここでは、```train_test_split()``` 関数の ```test_size``` 引数にデータセットの$30%$をテストデータとすることを指定しています。また、```stratify``` 引数にラベルデータを指定することで、訓練データとテストデータ、それぞれでラベルの分布が同じになるようにしています。

# In[7]:


from sklearn.model_selection import train_test_split
from sklearn import datasets

iris= datasets.load_iris()
X = iris.data # 特徴量データ
y = iris.target # ラベルデータ

assert len(X) == len(y)

# 訓練データとテストデータに分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1, stratify=y)


# ### データをモデルに当てはめる
# 
# ```fit()```メソッドは、モデルに依存する計算を内部で実行し、計算の結果は、ユーザが調べられるようにモデルの[属性](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html)に格納されます。

# In[8]:


model.fit(X_train, y_train) # モデルを訓練データに適合


# In[9]:


model.classes_


# ### モデルで未知のラベルを予測する
# 
# モデルが訓練できたら、教師データに含まれていなかった新しいデータに対してラベルを予測し、評価を行うことは可能です。
# 
# ```accuracy_score()``` はモデルの予測精度を評価するための関数です。

# In[10]:


y_predicted=model.predict(X_test) # テストデータでラベルを予測


# In[11]:


from sklearn.metrics import accuracy_score
accuracy_score(y_test, y_predicted) # 予測精度（accuracy）の評価


# ### 教師あり学習・回帰の例
# 
# 以下では、アイリスデータセットを用いて花の特徴の1つ、petal_length、からもう1つの特徴、petal_width、を回帰する手続きを示しています。
# 
# この時、petal_length は特徴量、petal_width は連続値のラベルとなっています。
# 
# 散布図を用いて petal_length と petal_width の関係を可視化してみると、関係があるといえそうでしょうか。

# In[12]:


import proplot as pplt
fig, ax = pplt.subplots()

iris= datasets.load_iris()
X = iris.data # 特徴量データ


# Extract petal length and petal width
petal_length = X[:, 2]
petal_width = X[:, 3]

# Create a scatter plot using proplot

ax.scatter(petal_length, petal_width)
# Set plot labels and title
ax.set_xlabel('Petal Length (cm)')
ax.set_ylabel('Petal Width (cm)')


# 
# ここで、回帰を行うモデルの1つである線形回帰 ([```LinearRegression```](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html)) を実装します。
# 
# ```mean_squared_error()``` は平均二乗誤差によりモデルの予測精度を評価するための関数です。
# 
# 

# In[13]:


from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

iris = load_iris()
X = iris.data[:, 2:3]  # Petal length as input feature
y = iris.data[:, 3]  # Petal width as target variable


# 訓練データとテストデータに分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)

model=LinearRegression() # 線形回帰モデル
model.fit(X_train,y_train) # モデルを訓練データに適合
y_predicted=model.predict(X_test) # テストデータで予測
mean_squared_error(y_test,y_predicted) # 予測精度（平均二乗誤差）の評価


# 線形回帰モデルにより学習された petal_length と petal_width の関係を表す回帰式を可視化しています。学習された回帰式が実際のデータに適合していることがわかります。

# In[98]:


# Create a scatter plot with regression line using proplot
fig, ax = pplt.subplots()
ax.scatter(X_test, y_test, label='Actual')
ax.plot(X_test, y_predicted, c='red', label='Regression Line')

# Set plot labels and title
ax.set_xlabel('Petal Length (cm)')
ax.set_ylabel('Petal Width (cm)')

# Add legend
ax.legend()

# Show the plot
plt.show()


# ````{tab-set}
# ```{tab-item} 実習問題
# [Perceptron](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Perceptron.html#sklearn.linear_model.Perceptron)で花の種類を分類するモデルを実装しなさい。
# ```
# ````

# ### 教師なし学習・クラスタリングの例
# 
# 教師なし学習の例として、アイリスデータセットをクラスタリングすることを考えましょう。
# 
# クラスタリングは、データセット内の類似した特徴を持つデータポイントをグループ化する手法です。クラスタリングの目的は、データ内の潜在的な構造やパターンを明らかにすることや、データをより理解しやすくすることです。

# ここでは、 [KMeans](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html)でアイリスデータセットをクラスタリングする手続きを示しています。
# 
# - ```KMeans``` クラスをインポートします
# - 特徴量データを用意します
# - 引数 ```n_clusters``` にハイパーパラメータとしてクラスタ数を指定して、 ```KMeans``` クラスのインスタンスを作成しています。
# - ```fit()``` メソッドによりモデルをデータに適合させます
# - ```predict()``` メソッドを用いて各データが所属するクラスタの情報 (```y_km```) を取得しています。

# In[136]:


from sklearn.cluster import KMeans

# アイリスデータセットの読み込み
iris = load_iris()
X = iris.data

# PCAモデルのインスタンス化とデータの変換
model = KMeans(n_clusters=3) #引数 n_clusters にハイパーパラメータとしてクラスタ数
model.fit(X) # モデルをデータに適合
y_km=model.predict(X) # クラスタを予測


# 学習された各花データのクラスタ情報を元のデータセットのデータフレームに列として追加し、クラスタごとに異なる色でデータセットを可視化しています。

# In[137]:


df = pd.DataFrame(data=X, columns=iris.feature_names)
df['cluster'] = y_km

# クラスタごとに色分けしてプロット
fig, ax = pplt.subplots()
ax.scatter(df['sepal length (cm)'], df['sepal width (cm)'], c=df['cluster'], cmap='viridis')

# Set plot labels and title
ax.set_xlabel('sepal length (cm)')
ax.set_ylabel('sepal width (cm)')

# Show the plot
plt.show()


# ````{tab-set}
# ```{tab-item} 実習問題1
# ガウス混合モデル(GMM)でアイリスデータセットのクラスタリングを実装しなさい。
# ```
# ```{tab-item} 実習問題2
# クラスタリングの結果と真のラベルと比較して、精度を計算しなさい。
# 
# 注意：クラスタリングでは真のラベルを利用するのではなく、クラスタリング結果のラベルを使用して精度を計算します。クラスタリング結果のラベルは、真のクラスラベルとは異なる順序やラベル付けを持つ場合があります。
# ```
# ````

# In[ ]:




