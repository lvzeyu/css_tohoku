#!/usr/bin/env python
# coding: utf-8

# # オブジェクトとクラス
# 
# 今までさまざまな箇所で触れたように、Pythonに含まれるすべての要素がオブジェクトとして扱われます。
# 
# オブジェクトは、**データ**と**メソッド**を持っています。
# 
# 例えば、```num=10```と書けば、値10の**整数型のオブジェクト**を作って、numという名前にオブジェクト参照を代入できます。整数型のオブジェクトは加算や乗算などのメソッドを持つため、```num+10```や```num*10```などの計算は可能です。
# 
# もちろん、```"cat"```や```"dog"```などの文字列もオプジェットであり、メソッドを持っています。文字列のオプジェットに定義されるメソッドによる、```"cat"+"dog"```で文字列の結合のような文字列のオプジェット特有な操作が可能です。
# 

# Pythonのオブジェクトは**クラス**に基づいて作成されます。クラスはオブジェクトの設計図であり、オブジェクトが持つデータとメソッドを定義します。
# 
# Pythonには、文字列、リスト、辞書などの標準データ型を作るための組み込みクラスがあります。
# 
# 新しいオブジェクトを作成する時、オブジェクトの内容と機能を規定するクラスを作る必要があります。

# ## ```class```によるクラスの定義

# 一般にクラス定義は、以下のような形をしています。
# 
# ```
# class クラス名:
#     def __init__(self):
#         実行文
#     def メソッド名(self, 引数, ...):
#         実行文
#     def メソッド名(self, 引数, ...):
#         実行文
# ```
# 
# ### 初期化
# 
# オプジェットを作成する際値を代入する場合は多いです。その場合。```__init__```という特殊なメソッドで、クラスのインスタンス化時に自動的に初期設定を行います。
# 
# ### メソッド
# 
# ここで示したように、**メソッド**は、クラスの中の関数のことです。
# 
# メソッド定義は関数定義と同じ形をしていますが、その最初の引数には慣例として```self```という名前を付けます。 この引数には、メソッドが呼び出されたオブジェクト自身が渡されます。メソッド内で自身の属性や他のメソッドにアクセスするために使用されます。

# In[1]:


class Person:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print("Hello,", self.name)


# In[2]:


marx=Person("Marx")


# 上記の例では、
# - Personというクラスを定義する
# - ```Person("Marx")```でオブジェクトのインスタンスを生成する
# - ```self```として新しい作ったオブジェクト、```name```としてもう一つの引数```"Marx"```を渡して、オブジェクトの```__init()__```メソッドを呼び出す
# - ```name```の値をオブジェクトに格納する
# - 新しいオブジェクトを返す、```Marx```という名前を与える

# オブジェクトにおける値は、属性としてオブジェクトとともに保存されますので、直接に読み書きできます。

# In[3]:


marx.name


# オブジェクトのメソッドを呼び出します。

# In[4]:


marx.say_hello()


# - ここで注意してほしいのは、```Personクラス```内部では、```name```属性には```self.name```という形でアクセスできます。

# 異なる値を渡せば、```Personクラス```から新しいオブジェクトを作成できます。

# In[5]:


webber=Person("Webber")


# In[6]:


webber.name


# In[7]:


webber.say_hello()


# ### 属性とメソッドの追加
# 
# 同じような形式で、属性とメソッドの追加しましょう。
# 
# 例えば、```Personクラス```に```birth```属性と```print_birth()```メソッドを追加するなら

# In[8]:


class Person:
    def __init__(self, name, birth):
        self.name = name
        self.birth = birth

    def say_hello(self):
        print("Hello, my name is", self.name)
    
    def print_birth(self):
        print("{} was born in {}".format(self.name,self.birth))


# In[9]:


sato=Person("Sato", 2000)


# In[10]:


sato.print_birth()


# ````{tab-set}
# ```{tab-item} 実習問題1
# ```Personクラス```に```current_year```という属性を追加してください。　で没年を受け取って、```print_death()```メソッドを追加する。
# ```
# 
# ```{tab-item} 実習問題2
# ```Personクラス```に```age()```年齢を計算するメソッドを追加してください。
# ```
# 
# ```{tab-item} 実習問題3
# ```Personクラス```をインスタント化にしてくだい。その際、```current_year```の値として2023を受け取って、年齢を計算してください。
# ```
# 
# ````

# ## 親クラスからの継承

# 継承は、既存のクラスをもとにして、変更部分だけを与えることにより、 新たなクラスを定義する機能です。
# 
# 元のクラスは親クラスまたはスーパークラス、基底クラス、新しいクラスは子またはサブクラスと呼ばれます。
# 
# 以下の例では、```Person```クラスをもとにして```Student```クラスを定義しています。

# In[11]:


class Student(Person):
    pass # 何もしない


# クラスは他のクラスを継承したものかどうかは、```issubclass()```を使えば調べられます。

# In[12]:


issubclass(Student, Person)


# 次に、継承を使用し、新しいクラスを作成してみよう。

# In[13]:


class Student(Person):
    def __init__(self, name, birth, number):
        super().__init__(name, birth)
        self.number = number

    def introduce(self):
        super().say_hello()
        print("I am a student.")


# ```Student```クラスが```Person```クラスを継承する際、```__init__```メソッドでは```super()```を使用することにより、```Person```クラスの属性```name```と```birth```を継承できます。
# 
# - ```super()```が親クラスの```Person```の定義を取り出す
# - ```super().__init__()```メソッド呼び出しは、```Person.__init__()```メソッドを呼び出す
# - ```self.number```は```Person```クラスに含まれていなく、```Student```クラスに新しい属性を追加する

# さらに、```Student```クラスには```say_hello```メソッドなど親クラスである```Person```クラスで定義されたメソッドが追加されて、```super().say_hello()```という形でを呼び出されます。

# In[14]:


john = Student("John", 2000, "S12345")


# In[15]:


john.name


# In[16]:


john.birth


# In[17]:


john.number


# さらに、```Student```クラスには```say_hello```メソッドなど親クラスである```Person```クラスで定義されたメソッドが追加されて、```super().say_hello()```という形でを呼び出されます。

# In[18]:


john.say_hello()


# In[19]:


john.introduce()


# ````{tab-set}
# ```{tab-item} 実習問題1
# ```Student```クラスが```Person```クラスを継承する際、```current_year```という属性も継承してくだい。
# 
# ```{tab-item} 実習問題2
# ```Student```クラスに```print_age()```というメソッドを追加してくだい。```print_age()```は、親クラスで定義された```age()```メソッドで年齢を計算し、```{name} is {age} years old```という形でプリントしてください。例えば、名前は```sato```, 年齢は```23```の場合、```sato is 23 years old```が表示されるようにしてください。
# ```
# 
# ````

# In[ ]:




