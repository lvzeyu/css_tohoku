#!/usr/bin/env python
# coding: utf-8

# In[1]:


<details><summary>Answer</summary>

The two heads are getting the same input data so they will be calculating the same gradients and will end up learning the same thing. We have two options:

A. Feed the two networks different data. This would essentially mean training the two networks independently or restructuring our data so that batch sizes of treated and control units can be split equally after input.

B. Somehow ensure that each head only receives error gradients for the correct treatment group. This will require writing a custom loss function.

Let's go with B.
</details>


# In[1]:


import pandas as pd
from sklearn.datasets import load_iris
from sklearn.mixture import GaussianMixture
from sklearn.metrics import accuracy_score

# アイリスデータセットの読み込み
iris = load_iris()
X = iris.data
y_true = iris.target

# GMMモデルのインスタンス化と学習
gmm = GaussianMixture(n_components=3, random_state=42)  # クラスタ数を3に設定
gmm.fit(X)

# クラスタリング結果のラベルを取得
y_pred = gmm.predict(X)

df_clustering = pd.DataFrame({'cluster': y_pred, 'target': y_true})
df_clustering["cluster"]=df_clustering["cluster"].map({0:2, 1:0, 2:1}) # クラスタ番号を元のラベルに対応させる

# クラスタリングの精度を計算
accuracy = accuracy_score(df_clustering["cluster"], df_clustering["target"])

# 結果の表示
print(f"クラスタリングの精度: {accuracy}")


# In[ ]:




