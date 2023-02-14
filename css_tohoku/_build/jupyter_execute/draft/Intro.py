#!/usr/bin/env python
# coding: utf-8

# ## Esstential Python Libraries

# ### NumPy
# **NumPy**は、プログラミング言語Pythonにおいて数値計算を効率的に行うための拡張モジュールである。効率的な数値計算を行うための型付きの多次元配列（numpy.ndarray）のサポートをPythonに加えるとともに、それらを操作するための大規模な高水準の数学関数ライブラリを提供する。
# 
# ### pandas
# 
# **pandas**とは、データ解析を容易にする機能を提供するPythonのデータ解析ライブラリです。
# Pandasの特徴には、データ操作のための高速で効率的なデータフレーム (DataFrame) という独自のデータ構造が提供されており、データの調整や変形など様々な処理が可能です。
# 
# ### matplotlib
# 
#  matplotlibは、グラフ描画ライブラリである。オブジェクト指向のAPIを提供しており、様々な種類のグラフを描画する能力を持つ。
# 
# ### scikit-learn
# 
# scikit-learnは機械学習ライブラリである。教師あり学習、教師なし学習に関するアルゴリズム(SVM、Random Forest、回帰、クラスタリングなど)が一通り利用出来る上、データセットが豊富に揃っている。
# 

# ## Python環境構築
# 
# ### Anaconda
# 
# Python の環境を構築するもう一つの方法として [Anaconda](https://www.anaconda.com/)を利用することもできます。
# Anaconda はデータサイエンス向けの環境を提供するプラットフォームです。科学技術計算などを中心とした、多くのモジュールやツールのコンパイル済みバイナリファイルを提供しており、簡単にPythonを利用する環境を構築・管理できます。
# 

# ### Anacondaのインストール
# 
# 下記の記事を参照してAnacondaをインストールします
# 
# - [Windows版Anacondaのインストール](https://www.python.jp/install/anaconda/windows/install.html)
# - [MacOS版Anacondaのインストール](https://www.python.jp/install/anaconda/macos/install.html)
# - [Linux版Anacondaのインストール](https://www.python.jp/install/anaconda/unix/install.html)

# ### Conda環境の作成
# Conda環境は、```conda create```コマンドでPython環境を作成します。
# つぎのコマンドは、```chss``` という名前で、```Python 3.10```の環境を作成します。
# ```
# (base) $ conda create --name chss python=3.10
# ```
# 作成した環境を確認します。
# ```
# (base) $ conda info -e
# ```

# In[1]:


get_ipython().system('conda info -e')


# 
