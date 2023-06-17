#!/usr/bin/env python
# coding: utf-8

# # NumPy

# 計算社会科学の研究は、テキスト、画像、ビデオや数値測定結果など幅広いデータセットとソースを扱っています。
# 
# 形式に違いがあるにも関わらず、基本的に全てのデータは数値の配列として扱うのに適しています。
# 
# - テキストデータは文字のシーケンスであり、それぞれの文字には数値の表現があります（通常はUnicode）。テキスト処理や自然言語処理のために、テキストデータは数値の配列として表現されることがあります。一般的な手法には、文字を数値にエンコードする方法（例：ASCII、UTF-8）、単語や文字の出現頻度を数える方法、単語の埋め込み（Word2Vec、GloVe）などがあります。
# - 画像は、各ピクセルに対して数値の輝度や色情報が割り当てられています。カラー画像の場合、各ピクセルはRGB（赤、緑、青）の値で表され、グレースケール画像の場合は単一の輝度値で表されます。
# 
# ![](https://nbviewer.org/github/fastai/numerical-linear-algebra/blob/master/nbs/images/digit.gif)
# 
# どのようなデータであっても、それらを分析可能にする最初のステップは、数値の配列に変換することです。
# 
# このため、数値配列の効率的な格納と操作は、データ分析にとって欠かせない要素です。
# 
# ```NumPy```は、多次元配列や行列演算を効率的に処理する機能を提供し、科学技術計算やデータ解析に広く利用されています。

# In[1]:


import numpy as np
print(np.__version__)


# ## NumPy配列の作成

# ### Pythonリストから作る配列

# ```np.array```を使って、PythonリストからNumPy配列（```ndarray```）を作成します。

# ```{margin}
# NumPy配列とPythonの組み込みリストと似ていますが、NumPy配列はより効率的な格納とデータ操作を提供しています。
# ```

# In[2]:


np.array([1, 2, 3, 4, 5, 6])


# Pythonリストとは異なり、NumPy配列の要素は全て同じ型という制約がります。作成する際、型が一致しない場合、可能であればNumPyは自動的に調整してくれます。

# In[3]:


np.array([1, 2, 3.14, 4, 5, 6]) # upcasting: all elements are converted to float


# ```dtype```キーワードで配列のデータ型を明示的に設定できます。

# In[4]:


np.array([1, 2, 3, 4, 5, 6],dtype='float32') # specify data type


# ### 配列の構築

# ```NumPy```の組み込み関数で配列を作成できます。

# In[5]:


np.zeros(10, dtype=int) # create an array of 10 zeros


# In[6]:


np.ones((3, 5), dtype=float) # create a 3x5 array of floating-point ones


# In[7]:


np.full((3, 5), 3.14) # create a 3x5 array filled with 3.14


# In[8]:


np.arange(0, 20, 2) # create an array filled with a linear sequence


# In[9]:


np.linspace(0, 1, 5) # create an array of five values evenly spaced between 0 and 1


# In[10]:


np.random.random((3, 3)) # create a 3x3 array of uniformly distributed random values between 0 and 1


# In[11]:


np.random.normal(0, 1, (3, 3)) # create a 3x3 array of normally distributed random values with mean 0 and standard deviation 1


# In[12]:


np.random.randint(0, 10, (3, 3)) # create a 3x3 array of random integers in the interval [0, 10)


# In[13]:


np.eye(3) # create a 3x3 identity matrix


# ```{note}
# 配列作成方法の一覧は、[公式チュートリアル](https://numpy.org/doc/stable/reference/routines.array-creation.html)を参照してください。
# ```

# ## NumPy配列の属性

# In[14]:


import numpy as np
np.random.seed(0) # seed for reproducibility
x1 = np.random.randint(10, size=6) # one-dimensional array
x2 = np.random.randint(10, size=(3, 4)) # two-dimensional array
x3 = np.random.randint(10, size=(3, 4, 5)) # three-dimensional array


# NumPy配列には、ndim(次元数)、shape(各次元のサイズ)、size(配列の合計サイズ)、dtype(配列のデータ型)などの属性を持ちます。

# In[15]:


print("x3 ndim: ", x3.ndim) # number of dimensions
print("x3 shape:", x3.shape) # the size of each dimension
print("x3 size: ", x3.size) # total size of the array
print("dtype:", x3.dtype) # data type of the array


# ## 配列のインデクス

# 1次元配列では、Pythonリストと同様に、$i$番目($0$から)の値にアクセスできます。

# In[16]:


x1


# In[17]:


x1[1]


# 多次元配列では、カンマで区切ったインデクスで要素にアクセスします。

# In[18]:


x2


# In[19]:


x2[1,1]


# In[20]:


x2[1,-1]


# インデクスを指定し、要素の値を変更するもできます。

# In[21]:


x2[1,-1]=12


# In[22]:


x2


# 
