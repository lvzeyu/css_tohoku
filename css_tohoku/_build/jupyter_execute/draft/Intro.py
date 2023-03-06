#!/usr/bin/env python
# coding: utf-8

# # 授業の概要
# 
# Pythonは世界中でよく使われているプログラミング言語です。特に、科学計算とデータ分析のコミュニティの発展に伴う、Pythonはデータサイエンス、機械学習などの領域において、最も重要な言語の一つと変わっていきました。
# 
# この授業は、プログラミング言語Pythonを用いて計算社会科学的なデータ操作・処理・分析用プログラムを書くための基本的な技術を習得することを目的とします。その以外、プログラミングとデータ分析のために必要な知識と技術も学びます。
# 
# ## 授業の資料について
# 
# この授業の資料は、[Jupyter Notebook](https://jupyter-notebook.readthedocs.io/en/stable/)形式で作成されたソースファイルを[Jupyter Book](https://jupyterbook.org/en/stable/intro.html)を用いて変換することで作成されたコンテンツになっている。
# 
# 
# - 授業の資料はこちらのリンクで閲覧できます。
# - `.ipynb`形式のソースファイルの管理と共有には、GitHubと呼ばれる環境を利用していて、ソースファイルは[こちら](https://github.com/lvzeyu/css_tohoku)からも閲覧できる。
# - [Google Colaboratory](https://colab.research.google.com/)というサービスを利用してGoogleのクラウド環境上でJupyter Nootebookを編集・実行することができます (手持ちのPCの動作に不安がある方は、Google Colaboratoryを利用してください)。
# ```{note}
# Google Colaboratory上でノートブックを開くには、ロケットの形をしたボタンにマウスオーバーして”Colab”から開く。
# ```

# # Python

# ## Pythonとは？

# Pythonはデータ解析・機械学習のためのライブラリが充実しており、データ解析や機械学習の分野で最もよく使われている言語である。

# ### NumPy
# [**NumPy**](https://numpy.org/doc/)は、プログラミング言語Pythonにおいて数値計算を効率的に行うための拡張モジュールである。効率的な数値計算を行うための型付きの多次元配列（numpy.ndarray）のサポートをPythonに加えるとともに、それらを操作するための大規模な高水準の数学関数ライブラリを提供する。
# 
# ### pandas
# 
# [**pandas**](https://pandas.pydata.org/docs/)とは、データ解析を容易にする機能を提供するPythonのデータ解析ライブラリです。
# Pandasの特徴は、データ操作のための高速で効率的なデータフレーム (DataFrame) という高いレベルのデータ構造データを提供しています。構造化されるデータ形式で、データの調整や変形など様々な処理が可能です。
# 
# ### matplotlib
# 
#  [**matplotlib**](https://matplotlib.org/stable/index.html)は、グラフ描画ライブラリである。オブジェクト指向のAPIを提供しており、様々な種類のグラフを描画する能力を持つ。Pythonで使える可視化ためのライブライは他にもありますが、Matplotlibは最も広く使われているため、他のライブライとうまく連携しやすくなっています。
# 
# ### scikit-learn
# 
# [**scikit-learn**](https://scikit-learn.org/stable/)は機械学習ライブラリである。教師あり学習、教師なし学習に関するアルゴリズム(SVM、Random Forest、回帰、クラスタリングなど)の効率的な実装を提供しています。
# 

# # Jupyter
# 
# Jupyter Notebookとは、ブラウザの強力な表示機能を活用したインターフェイスです。Pythonコードの実行だけでなく、Markdownテキスト・数式・図などを含んだドキュメント作成の機能も備えています。
# 
# ## Jupyterの基本
# - Jupyterにはコマンドモードとエディットモードがあります。セルをダブルクリックするか、選択して```enter```を押すと、そのセルのエディットモードになります。エディットモードで```esc```を押すか、別のセルをクリックするとコマンドモードに戻ります。
# - jupyterはセルを基本的な要素としています。セルにはいくつか種類がありますが、CodeとMarkdownの２種類だけ覚えてください。
# - [ショートカット](https://qiita.com/zawawahoge/items/baa2a5318df079c5f7e5)はいろいろありますが、最低限次だけは覚えましょう。
# 
# ```{コマンドモード}
# shift+enterを押す: コードを実行し、下のセルに移動する.
# Mを押す: マークダウンセルにする
# Yを押す: コードセルにする
# Dを二回押す: セルを削除する
# Oを押す: セルの出力結果の表示・非表示
# Aを押す: 上にセルを追加する
# Bを押す: 下にセルを追加する  	
# ```
# ## Markdown
# 
# Markdown（マークダウン）は、文書を記述するための言語のひとつです。基本的なMarkdown記法を覚えておきましょう。
# 
# ### 見出し
# ```
# # 見出し1
# ## 見出し2
# ### 見出し3
# #### 見出し4
# ##### 見出し5
# ###### 見出し6
# ```
# 
# ### 箇条書きリスト
# ```
# - リスト1
#     - ネスト リスト1_1
#         - ネスト リスト1_1_1
#         - ネスト リスト1_1_2
#     - ネスト リスト1_2
# - リスト2
# - リスト3
# ```

# - リスト1
#     - ネスト リスト1_1
#         - ネスト リスト1_1_1
#         - ネスト リスト1_1_2
#     - ネスト リスト1_2
# - リスト2
# - リスト3

# ### 番号付きリスト
# ```
# 1. 番号付きリスト1
#     1. 番号付きリスト1_1
#     1. 番号付きリスト1_2
# 1. 番号付きリスト2
# 1. 番号付きリスト3
# ```

# 1. 番号付きリスト1
#     1. 番号付きリスト1_1
#     1. 番号付きリスト1_2
# 1. 番号付きリスト2
# 1. 番号付きリスト3

# ### 引用
# ```
# >社会学（しゃかいがく、仏: sociologie、英:Sociology）は、社会現象の実態や、現象の起こる原因に関するメカニズム（因果関係）を体験・統計・データなどを用いて分析することで解明する学問である。
# ```

# >社会学（しゃかいがく、仏: sociologie、英:Sociology）は、社会現象の実態や、現象の起こる原因に関するメカニズム（因果関係）を体験・統計・データなどを用いて分析することで解明する学問である
# 

# ## Python環境
# 
# ### Anaconda
# 
# 数あるPython の環境を構築する方法の中で、 [Anaconda](https://www.anaconda.com/)を利用することをお勧めします。
# Anaconda はデータサイエンス向けの環境を提供するプラットフォームです。科学技術計算などを中心とした、多くのモジュールやツールのコンパイル済みバイナリファイルを提供しており、簡単にPythonを利用する環境を構築・管理できます。Windows, Linux, macOS向けのパッケージが提供されています。
# 

# #### Anacondaのインストール
# 
# 下記の記事を参照してAnacondaをインストールします
# 
# 
# - [Windows版Anacondaのインストール](https://www.python.jp/install/anaconda/windows/install.html)
# - [MacOS版Anacondaのインストール](https://www.python.jp/install/anaconda/macos/install.html)
# - [Linux版Anacondaのインストール](https://www.python.jp/install/anaconda/unix/install.html)

# #### Conda環境の作成
# - Conda環境は、```conda create```コマンドでPython環境を作成します。つぎのコマンドは、```chss``` という名前で、```Python 3.10```の環境を作成します。
# ```
# conda create --name chss python=3.10
# ```
# - 作成した環境を確認します。
# ```
# conda info -e
# ```
# - 作成した環境を有効にする。
# ```
# conda activate chss
# ```

# #### Pythonコードの実行
# - ターミナルでpythonを呼び出します
# ```
# python
# ```
# - 定番なコードを実行しましょう

# In[1]:


print("Hello world")


# # GitHub

# 

# 
