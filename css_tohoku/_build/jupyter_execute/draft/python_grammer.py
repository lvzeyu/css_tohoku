#!/usr/bin/env python
# coding: utf-8

# # Pythonの基本構文
# 
# ## 改行
# 
# Python では、改行が文の区切りとなります。
# 

# In[1]:


print("Hello")
print("World")


# または、セミコロン(```;```)で区切ることもできます。

# In[2]:


a = 5; b = 3; c = a + b
print(c)


# 文を数行に分けて記述したい場合は、行末にバックスラッシュ(```\```)を書きます。

# In[3]:


total = 123       + 456       + 789
print(total)


# ## コメント(```#```)
# 
# ハッシュ(```#```)から行末まではコメントとみなされます。
# 
# コメントはプログラムの実行には影響せず、プログラムのコードを読む人に向けたメモや説明のために使われます。
# 

# In[4]:


print("Hello")      # Helloと表示します


# ## インデント
# 
# Python ではインデント(行頭の空白文字の数)が重要な意味を持ち、同じ数の空白やタブ文字でインデントされた文がブロックとみなされます。
# 
# インデントは通常4個の空白文字を使用します。
# 
# - 同じブロックのコードは同じ量のインデントが必要です：あるブロック（例えば、関数の本体、ループの内部、条件文の内部など）内のすべての行は同じレベルのインデントでなければなりません。
# - ブロックが終了すると、インデントは元に戻ります：ブロックの最後の行に到達すると、次の行はそのブロックを開始する前のインデントレベルに戻ります。

# In[5]:


for i in range(5):
    print(i)  # ループの内部でインデントされています
    if i == 3:
        print("Found three!")  # 条件文の内部でさらにインデントされています

print("Loop finished")  # ループの外で、インデントは元に戻ります


# ## 変数

# ### 変数の命名
# 
# ```{margin}
# Pythonにおいて**すべての数、文字列、データ構造、関数、クラス、モジュールがオブジェクト**です。初心者にとってやや理解しにくいかもしれませんが、ここではさしあたり、オブジェクトのイメージを簡単に説明します。
# ```
# 
# Pythonで変数を定義できます。変数とは、プログラムで使いたいメモリ上の値に名前を付けたものです。値を保存したり参照したりするために使用されます。
# 
# Pythonで変数の作成は、いくつかのルールがあります。
# 
# - 大文字と小文字を区別する：```chss```,```Chss```, ```CHSS```はすべて異なる名前です。
# - 先頭で数字は使えないです。例えば、```1a```は無効な変数名です。
# - Pythonの予約語を避けます。

# ### 予約語の一覧を表示
# ```{note}
# 強制ではないですが、可読性を向上するために、できるだけ推奨される命名規則にしたがった方が良いです。
# <table class="table2">
#     <thead>
# <tr>
# <th style="text-align: center">対象</th>
# <th style="text-align: center">ルール</th>
# <th style="text-align: center">例</th>
# </tr>
# </thead>
# <tbody>
# <tr>
# <td style="text-align: center">パッケージ</td>
# <td style="text-align: center">全小文字 なるべく短くアンダースコア非推奨</td>
# <td style="text-align: center">tqdm, requests ...</td>
# </tr>
# <tr>
# <td style="text-align: center">モジュール</td>
# <td style="text-align: center">全小文字 なるべく短くアンダースコア可</td>
# <td style="text-align: center">sys, os,...</td>
# </tr>
# <tr>
# <td style="text-align: center">クラス</td>
# <td style="text-align: center">最初大文字 + 大文字区切り</td>
# <td style="text-align: center">MyFavoriteClass</td>
# </tr>
# <tr>
# <td style="text-align: center">例外</td>
# <td style="text-align: center">最初大文字 + 大文字区切り</td>
# <td style="text-align: center">MyFuckingError</td>
# </tr>
# <tr>
# <td style="text-align: center">型変数</td>
# <td style="text-align: center">最初大文字 + 大文字区切り</td>
# <td style="text-align: center">MyFavoriteType</td>
# </tr>
# <tr>
# <td style="text-align: center">メソッド</td>
# <td style="text-align: center">全小文字 + アンダースコア区切り</td>
# <td style="text-align: center">my_favorite_method</td>
# </tr>
# <tr>
# <td style="text-align: center">関数</td>
# <td style="text-align: center">全小文字 + アンダースコア区切り</td>
# <td style="text-align: center">my_favorite_funcion</td>
# </tr>
# <tr>
# <td style="text-align: center">変数</td>
# <td style="text-align: center">全小文字 + アンダースコア区切り</td>
# <td style="text-align: center">my_favorite_instance</td>
# </tr>
# <tr>
# <td style="text-align: center">定数</td>
# <td style="text-align: center">
# <strong>全大文字</strong> + アンダースコア区切り</td>
# <td style="text-align: center">MY_FAVORITE_CONST</td>
# </tr>
# </tbody>
# </table>
# ```

# In[6]:


help("keywords")


# ### 代入
# ```=```を使って変数に値を代入する。

# In[7]:


a=5
print(a)
print(a+5)


# `````{admonition} Advanced
# :class: important
# 多くのプログラミング言語では、変数自体が型を持ち、メモリ位置が固定されているが、Pythonの場合、**変数はただの名前です**。
# ```{figure} ./Figure/immutable.png
# ---
# scale: 50%
# align: left
# ---
# ```
# つまり、代入は値をコピーするわけではない、**データを入れてあるオブジェクトに名前を付けるだけです**。名前はものの**参照手段**であり、もの自体ではないです。
# 
# 変数の代入は、メモリ内のどこかにあるオブジェクトに長いヒモで繋がるというイメージです。そのため、```C```や```JAVA```のような静的言語では変数の型を明確的に指定しなければないが、Pythonでは型を指定する必要はありません。
# 
# ```{figure} ./Figure/immutable2.png
# ---
# scale: 40%
# align: left
# ---
# ```
# 
# ```{figure} ./Figure/immutable3.png
# ---
# scale: 40%
# align: right
# ---
# ```
# `````

# In[8]:


#新たに生成したように見えるbは同じ値を指しているので、変数も値そのものもIDは同じになります。
a=5
b=5
print("a:{},b:{},5:{}".format(id(a),id(b),id(5)))


# In[9]:


#変数の型が異なるなら、変数IDも異なっています。
a='5'
b=5
print("a:{},'5':{},b:{},5:{}".format(id(a),id('5'),id(b),id(5)))

