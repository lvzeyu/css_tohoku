#!/usr/bin/env python
# coding: utf-8

# In[ ]:





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
# - [Windows版Anacondaのインストール](https://www.python.jp/install/anaconda/windows/install.html)
# - [MacOS版Anacondaのインストール](https://www.python.jp/install/anaconda/macos/install.html)
# - [Linux版Anacondaのインストール](https://www.python.jp/install/anaconda/unix/install.html)
# 
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

# 
