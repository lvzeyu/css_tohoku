#!/usr/bin/env python
# coding: utf-8

# # 授業の概要
# 
# Pythonは世界中でよく使われているプログラミング言語です。特に、科学計算とデータ分析のコミュニティの発展に伴う、Pythonはデータサイエンス、機械学習、深層学習などの領域において、最も重要な言語の一つと変わっていきました。
# 
# この授業は、プログラミング言語Pythonを用いて計算社会科学的なデータ操作・処理・分析用プログラムを書くための基本的な技術を習得することを目的とします。その以外、プログラミングとデータ分析のために必要な知識と技術も学びます。
# 

# ## 授業の内容

# ### Python

# Pythonはデータ解析・機械学習のためのライブラリが充実しており、データ解析や機械学習の分野で最もよく使われている言語である。

# #### NumPy
# [**NumPy**](https://numpy.org/doc/)は、プログラミング言語Pythonにおいて数値計算を効率的に行うための拡張モジュールである。効率的な数値計算を行うための型付きの多次元配列（numpy.ndarray）のサポートをPythonに加えるとともに、それらを操作するための大規模な高水準の数学関数ライブラリを提供する。

# - 配列を作成するための関数は多く備えています

# In[1]:


import numpy as np


# In[2]:


a = np.zeros((2,2)) # すべて0の配列を作成
print(a)


# In[3]:


b = np.random.normal(
    loc   = 0,      # 平均
    scale = 1,      # 標準偏差
    size  = (2,2),# 出力配列のサイズ
) # 正規分布に従う乱数の配列を作成
print(b)


# In[4]:


arr1 = np.arange(4).reshape((2, 2))
print(arr1)


# In[5]:


arr2 = np.arange(6).reshape((2, 3))
print(arr2)


# - 行列の操作と演算を行うにはNumPyを使うと便利です

# In[6]:


arr1.reshape((1, 4))


# In[7]:


# 転置
arr1.T


# In[8]:


# 逆行列
np.linalg.inv(arr1)


# In[9]:


# 内積
np.dot(arr1, arr2)


# #### pandas
# 
# [**pandas**](https://pandas.pydata.org/docs/)とは、データ解析を容易にする機能を提供するPythonのデータ解析ライブラリです。
# Pandasの特徴は、データ操作のための高速で効率的なデータフレーム (DataFrame) という高いレベルのデータ構造データを提供しています。構造化されるデータ形式で、データの調整や変形など様々な処理が可能です。

# In[10]:


import pandas as pd
data = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')
data


# In[11]:


# 頻度を計算する
data["species"].value_counts()


# In[12]:


# 統計量を計算する
data["sepal_width"].describe()


# In[13]:


# データフレームの変形
data.melt(id_vars=["species"], 
        var_name="features", 
        value_name="values")


# 
# #### matplotlib
# 
#  [**matplotlib**](https://matplotlib.org/stable/index.html)は、グラフ描画ライブラリである。オブジェクト指向のAPIを提供しており、様々な種類のグラフを描画する能力を持つ。Pythonで使える可視化ためのライブライは他にもありますが、Matplotlibは最も広く使われているため、他のライブライとうまく連携しやすくなっています。

# In[14]:


import matplotlib.pyplot as plt
plt.rcParams['xtick.direction'] = "out"
plt.rcParams['ytick.direction'] = "in"

normal = np.random.normal(0, 1, 2000)
plt.hist(normal, bins=50, density=True, alpha=0.6, color='b')
plt.show()


# #### scikit-learn
# 
# [**scikit-learn**](https://scikit-learn.org/stable/)は機械学習ライブラリである。教師あり学習、教師なし学習に関する[アルゴリズム](https://scikit-learn.org/stable/modules/classes.html)(SVM、Random Forest、回帰、クラスタリングなど)の効率的な実装を提供しています。

# #### 学習の到達目標
# 
# - データ構造、制御構造、オブジェクト指向などプログラミング言語の基礎概念について学ぶとともに、ある程度自由にPythonを用いて計算やデータ処理を実装できるようになることを目指す
# - データ処理とデータ分析に必要なPythonライブラリの使い方を習得することを目指す
# - Python環境の構築、パッケージ管理、コード管理に関する知識を習得し、Pythonを用いて再生可能なデータ解析を行えるようにことを目指す
# 

# ### GitとGitHub

# [Git](https://git-scm.com/)は「**パージョン管理システム(Version Control System)**」と呼ばれるものの一つです。
# 
# パージョン管理システムとは、一つのファイル、または複数のファイルの集合に対して、時間とともに加えられた変更を記録するシステムで、後から特定のバージョンを呼び出すことができるようにするためのものです。
# 
# ファイルの「パージョン(変更履歴)」を記録して、いつでも過去の状況に戻したり、過去の変更履歴を比較したり、またはどのタイミングで問題が起こっていたかを確認したり、様々なことができるプログラム開発やファイル管理を補助するシステムです。
# 
# [**GitHub**](https://github.com/)などの**リモートリポジトリ**と組み合わせることで、クラウドでデータと進捗を管理したり、他のメンバーとコードと情報を共有したり、個人のプロジェクトだけでなく、共同開発するときも強力なツールとなります。

# ![](./Figure/remote.png)

# #### 学習の到達目標
# 
# - Gitを用いてプロジェクトを管理するスキルを把握するを目指す
# - GitHubを用いて共同作業を進めるスキルを把握することを目指す

# # 授業設計と成績評価
# 
# - 授業中実践的なプログラミング操作が多いので、必ずPCをご持参ください。また、インターネットとの接続が必要される操作もありますので、PCのインターネット接続も事前に設定してください。
# - 授業後課題提出を求める場合があります。基本的には授業の理解度を確認するためのプログラミング課題と想定しています。
# - グループワークの形で実践的なデータ解析プロジェクトに取り組んで、最終の授業で発表します。
#     - 基本的にはpythonを使ってくだい。
#     - グループワークの管理は<ins>GitとGitHub</ins>を使ってください。
#     - グループ内の責任分担は自由ですが、<ins>全てのメンバーが一部のプログラミング作業を分担する</ins>ことが望ましい。
#     - これからの授業で説明しますが、GitとGitHubによるプロジェクトを管理すると、<ins>各メンバーの作業履歴を確認できます</ins>ので、グループ全体の成果だけでなく、各メンバーの貢献度も加味して成績を評価します。
# - 成績評価の分配は以下の通りです
#     - 出席: $30\%$
#     - 授業後の課題: $30\%$
#     - グループワーク: $40\%$
# ```{margin}
# GitHub　Issueの使い方についてはこれからの授業で説明します。
# ```
# - 授業の内容に関して不明点あるいはご要望があれば、随時メールでご連絡ください。また、プログラミングや操作の質問については、Google ClassroomまたはGitHub Issueでも受け付けます。
# - 授業のオフィスアワーは、できれば二日前アポイントを取ってくだい。

# # 授業の資料
# 
# この授業の資料は、[Jupyter Notebook](https://jupyter-notebook.readthedocs.io/en/stable/)形式で作成されたソースファイルを[Jupyter Book](https://jupyterbook.org/en/stable/intro.html)を用いて変換することで作成されたコンテンツになっている。
# 
# 
# - 授業の資料はこちらの[リンク](https://lvzeyu.github.io/css_tohoku/)から閲覧できます。
# - `.ipynb`形式のソースファイルの管理と共有には、GitHubと呼ばれる環境を利用していて、ソースファイルは[こちら](https://github.com/lvzeyu/css_tohoku)からも閲覧できる。
# - [Google Colaboratory](https://colab.research.google.com/)というサービスを利用してGoogleのクラウド環境上でJupyter Nootebookを編集・実行することができます (手持ちのPCの動作に不安がある方は、Google Colaboratoryを利用してください)。
# ```{note}
# Google Colaboratory上でノートブックを開くには、ロケットの形をしたボタンにマウスオーバーして”Colab”から開く。
# ```
# ![](./Figure/intro1.png)

# # 次回の授業までに
# 
# - [**GitHub**](https://github.com/)アカウントを作ってください。
# - [公式サイト](https://git-scm.com/downloads)からGitをインストールしてください。
# 

# 
