#!/usr/bin/env python
# coding: utf-8

# # Pythonの基礎

# ## オブジェクト
# 
# Pythonにおいて**すべての数、文字列、データ構造、関数、クラス、モジュールがオブジェクト**です。初心者にとってやや理解しにくいかもしれませんが、ここではさしあたり、オブジェクトのイメージを簡単に説明します。

# # 変数
# 
# ## 変数の命名
# 
# Pythonで変数を定義できます。変数とは、プログラムで使いたいメモリ上の値に名前を付けたものです。
# Pythonで変数の作成は、いくつかのルールがあります。
# 
# - 大文字と小文字を区別する：```chss```,```Chss```, ```CHSS```はすべて異なる名前です。
# - 先頭で数字は使えないです。例えば、```1a```は無効な変数名です。
# - Pythonの予約語を避けます。

# In[1]:


# 予約語の一覧を表示
help("keywords")


# ```{note}
# 強制ではないですが、可読性を向上するために、できるだけ推奨される変数の命名規則にしたがった方が良いです。
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

# ## 代入

# ```=```を使って変数に値を代入する。

# In[2]:


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

# In[3]:


#新たに生成したように見えるbは同じ値を指しているので、変数も値そのものもIDは同じになります。
a=5
b=5
print("a:{},b:{},5:{}".format(id(a),id(b),id(5)))


# # データ型
# 
# ## 数値

# ### ブール値
# 
# Pythonでは、bool型の値は```True```と```False```の2種類です。**条件式**や**論理演算**でよく使われます。
# 
# 組込み関数```bool()``` は、オブジェクトや演算式等を真理値判定に基づいて、任意のPythonデータ型を```bool```に変換できます。

# ```{note}
# **関数**の詳細については今後の授業で学びますので、さしあたり今は、関数に引数を渡すと、その値に応じた何らかの処理結果を返すということを知っておけば良いです。
# ```

# - $0$ではない数値は```True```と見されます。

# In[4]:


bool(10)


# - $0$は```False```と見されます。

# In[5]:


bool(0)


# ### 整数
# 整数は、小数点以下がなく数値です。

# In[6]:


123


# In[7]:


-123


# 大きな数値のセパレータとしてアンダースコア(```_```)を使えます。

# ```{margin}
# 整数の先頭に$0b$,$0o$,$0x$がつくのは、通常の10進数以外の基数であることを指します。
# ```

# In[8]:


1_000_000


# Pythonでは数値の計算もできます。数学演算子は表のように定義されています。
# 
# 演算の優先順位は通常の数学と同様に定義されています。通常の数学と同様に、()を使えば、演算の順番を決めることもできます。
# <table class="table2">
#     <thead>
#         <tr><th>演算子</th><th>演算</th><th>例</th></tr>
#     </thead>
#     <tbody>  
#         <tr><td>+</td><td>加算</td><td>a + b</td></tr>
#         <tr><td>-</td><td>減算</td><td>a - b</td></tr>
#         <tr><td>*</td><td>乗算</td><td>a * b</td></tr> 
#         <tr><td>/</td><td>除算</td><td>a / b</td></tr> 
#         <tr><td>%</td><td>剰余</td><td>a % b</td></tr>
#         <tr><td>//</td><td>切り捨て除算</td><td>a // b</td></tr>
#         <tr><td>**</td><td>べき乗</td><td>a ** b</td></tr>
#     </tbody>
# </table>
# 
# 少し馴染みのない演算子のは、
# - 演算子 ```//``` は小数部を切り捨てた整数値（商）を返します。
# - 演算子 ```%```は整数除算の余り（剰余）を返します。

# In[9]:


13//5


# In[10]:


13%5


# ### 浮動小数点数
# 
# Pythonでは、整数と小数点のある数（実数）は浮動小数点数といいます。
# 
# ここで注意する必要があるのは、整数と実数が数学的に同じ数を表す場合でも、コンピュータの中で異なる形式で記憶されますので、表示は異なります。 

# In[11]:


5.


# In[12]:


5.0


# 浮動小数点数は文字```e```の後ろに$10$進の桁数を入れて指定することもできます。

# In[13]:


5e2


# ここで注意する必要があるのは、整数と実数が数学的に同じ数を表す場合でも、コンピュータの中で異なる形式で記憶されますので、表示は異なります。 
# ```{margin}
# プログラムの中で扱う変数には様々な"型"(```type```)があります。変数の型は```type()```という関数を使うことで調べることができる。
# ```

# In[14]:


print(type(5.0))
print(type(5))


# 浮動小数点数も算術演算子を使えます。
# 
# また、整数と実数が混ざって計算も可能です。ただ、その場合、結果は実数になります。

# In[15]:


2+5.0


# ```int()```関数で、浮動小数点数を整数に変換できます。

# In[16]:


int(98.5)


# ```float()```関数で、整数を浮動小数点数に変換できます。

# In[17]:


float(98)


# ````{tab-set}
# ```{tab-item} 練習問題1
# 一日は何秒だを計算してみよう。
# ```
# 
# ```{tab-item} 練習問題2
# $1$年$365$日といいますが、厳密的に言えば、$1$年を$366$日とする閏年を$400$年間に$97$回設けることによって、$1$年の平均日数を$365.2425$日とする。
# 
# 今度は一年は何分何秒かを計算しよう。一年$=()$分$()$秒で回答してください。
# ```
# ````

# In[ ]:





# ### 文字列
# 
# 文字列は数値とは異なるデータ型の一つで、文字通り文字を扱います。
# 
# #### 作成
# 
# 文字列は、**シーケンス**型という広義の型に属しています。シーケンス型とは順番のある要素の集まりを指します。インデックスで要素を指定して取り出すことができます。インデックスは$R$などとは違い、$1$ではなく、$0$から始まります。例えば、
# - ```0:3```とすると、$0$から$2$までの要素を取り出します。
# - ```1:```とすると$1$以降のすべての要素を取り出します。

# 文字列は、 クォートで文字を囲んで作ります。

# In[18]:


text="Hello!"
print(text)


# In[19]:


text='Hello!'
print(text)


# In[20]:


'"ダブル" クォートを埋め込むことができます'


# In[21]:


"'シングル' クォートを埋め込むことができます"


# In[22]:


'''三つのシングルクォート'''


# In[23]:


text='Hello!'


# 特定の文字の前にバックスラッシュをつけると、その文字を特殊な意味として扱うことができます。もっともよく使われるのは改行を意味する```\n```です。
# 
# ```{margin}
# Pythonには、小数の特殊なタイプの文字列があり、それらは最初クォートの前に文字を付けて示す。例えば、先頭が```r```の*raw文字列*では、 文字内の```\n``` は改行を表すエスケープシーケンスをエスケープシーケンスとして解釈されないようにする。特に説明しない限り、ここで取り上げるのは普通のUnicode文字列です。
# ```

# In[24]:


print("Hello\nWorld")


# #### $+$による連結

# In[25]:


"Hello"+"World"


# #### $*$による繰り返し

# In[26]:


"Hello"*3


# 
