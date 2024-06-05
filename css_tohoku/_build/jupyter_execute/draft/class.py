#!/usr/bin/env python
# coding: utf-8

# # オブジェクトとクラス
# 
# ## 基本概念
# 
# 
# 今までさまざまな箇所で触れたように、Pythonに含まれるすべての要素がオブジェクトとして扱われます。そのゆえに、pythonは**オブジェクト指向プログラミング**の一種になります。
# 
# **オブジェクト**とは、データ（属性）とそれを操作する関数（メソッド）をカプセル化したものです。
# 
# 例えば、「customer」というオブジェクトで考えてみます。
# 
# - customerでは、「email」や「phone」などのプロファイルがあります。このようなcustomerが持つ特徴を「属性」といいます。
# - customerでは、「place order」や「cancel order」などの行動を行うことができます。このようなcustomerが取ることのできるアクションを「メソッド」といいます。
# 
# 各customer独自の属性とメソッドを持っていますが、「形式」は共通しています。
# 
# あるcustomerを定義するために必要される属性とメソッドを定義している「テンプレート」に相当するものは、「**クラス**」といいます。
# 
# 「テンプレート」に内容を記入することで、作成される一人一人のcustomerが「**インスタンス**」といいます。

# ![](./Figure/object_example.png)
# 

# 
# 
# - ```num=10```と書けば、値10の**整数型のオブジェクト**を作って、numという名前にオブジェクト参照を代入できます。整数型のオブジェクトは加算や乗算などのメソッドを持つため、```num+10```や```num*10```などの計算は可能です。
# 
# - ```"cat"```や```"dog"```などの文字列もオプジェットであり、メソッドを持っています。文字列のオプジェットに定義されるメソッドによる、```"cat"+"dog"```で文字列の結合のような文字列のオプジェット特有な操作が可能です。
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
# オプジェットを作成する際、なんらかの値を代入することは必要される場合が多いです。
# 
# その場合、```__init__```という特殊なメソッドで、クラスのインスタンス化時に自動的に初期設定を行います。これにより、同じクラスの異なるインスタンスが異なる値を持つことができます。
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

# オブジェクトにおける値は、属性としてオブジェクトとともに保存されますので、オプジェットの外から直接に読み書きできます。

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
# ```Personクラス```に```current_year```という属性を追加してください。```death```で没年を受け取って、```print_death()```メソッドを追加する。
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


class Person:
    def __init__(self, name, birth, current_year=2023):
        self.name = name
        self.birth = birth
        self.current_year = current_year

    def say_hello(self):
        print("Hello, my name is", self.name)
    
    def print_birth(self):
        print("{} was born in {}".format(self.name,self.birth))
    
    def age(self):
        return self.current_year - self.birth


# In[12]:


class Student(Person):
    pass # 何もしない


# クラスは他のクラスを継承したものかどうかは、```issubclass()```を使えば調べられます。

# In[13]:


issubclass(Student, Person)


# 次に、継承を使用し、新しいクラスを作成してみよう。

# In[14]:


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

# In[15]:


john = Student("John", 2000, "S12345")


# In[16]:


john.name


# In[17]:


john.birth


# In[18]:


john.number


# さらに、```Student```クラスには```say_hello```メソッドなど親クラスである```Person```クラスで定義されたメソッドが追加されて、```super().say_hello()```という形でを呼び出されます。

# In[19]:


john.say_hello()


# In[20]:


john.introduce()


# ````{tab-set}
# ```{tab-item} 実習問題
# - ```Student```クラスが```Person```クラスを継承する際、```current_year```という属性も継承してくだい。
# 
# - ```Student```クラスに```print_age()```というメソッドを追加してくだい。```print_age()```は、親クラスで定義された```age()```メソッドで年齢を計算し、```{name} is {age} years old```という形でプリントしてください。例えば、名前は```sato```, 年齢は```23```の場合、```sato is 23 years old```が表示されるようにしてください。
# ```
# 
# ````

# ## 集約
# 
# Pythonにおけるクラスの集約（aggregation）とは、あるクラスが他のクラスのインスタンスをメンバーとして持つことを指します。つまり、1つのクラスが他のクラスを部品として利用し、それらのクラスの機能やデータを組み合わせて利用することができるということです。
# 
# クラスの集約は、関連性のあるオブジェクトを独立して定義し、それらを組み合わせてより複雑な構造を作成する場合に便利です。

# In[21]:


class Address:
    def __init__(self, state, city, street):
        self.state = state
        self.city = city
        self.street = street

    def get_full_address(self):
        return f"{self.state} {self.city} {self.street}"


# In[22]:


class Person:
    def __init__(self, name, birth, current_year=2023,address=None):
        self.name = name
        self.birth = birth
        self.current_year = current_year
        self.address = address

    def say_hello(self):
        print("Hello, my name is", self.name)
    
    def print_birth(self):
        print("{} was born in {}".format(self.name,self.birth))
    
    def age(self):
        return self.current_year - self.birth
    
    def get_person_info(self):
        address_info = self.address.get_full_address()
        return f"Name: {self.name}, Age: {self.age()}, Address: {address_info}"


# In[23]:


# Addressのインスタンスを作成
address = Address("宮城県", "仙台市", "青葉区川内27番1号")

# Personのインスタンスを作成し、Addressのインスタンスを渡す
sato = Person(name="佐藤", birth=2000, address=address)


# In[24]:


sato.get_person_info()


# ````{tab-set}
# ```{tab-item} 実習問題
# 1. Majorというクラスを作成し、専門分野に関する情報を保持する。
# 
# 2. Majorクラスには専攻名（major）、所属学部（department）、入学年（duration）が含まれている。
# 
# 3. StudentクラスがPersonクラスを継承する。その際、 
#  - Majorのインスタンスを渡す
#  - 入学年（duration）と現在の年(current_year)で学年を計算するメソッドを定義する
# 
# 4. Studentクラスをインスタンス化して、学年を計算してください。
# ```
# ````

# ## 特殊メソッド

# - ```num=1+9```のようなコードを実行する際、値1と値9を持つ整数オブジェクトは、```+```が数学の足し算の意味で使われています
# 
# - ```name='Karl'+'Marx'```のようなコードを実行する際、```+```が文字列の結合の意味で使われています。
# 
# なぜPythonがどの使い方にすべきことを知るといえば、**特殊メソッド**で演算子の機能を定義しているわけです。

# 特殊メソッドは、クラスの振る舞いや組み込みの言語機能をカスタマイズするために使用されます。
# 
# メソッド名の前後に2つのアンダースコア（ダブルアンダースコア）が付いていることが特徴です。
# 
# 既に紹介した```__init()__```は、初期化ための特殊メソッドとして知られており、オブジェクトが作成される際に自動的に呼び出されます。オブジェクトの初期化やインスタンス変数の設定など、初期化に必要な処理を実行します。

# ```{margin}
# 特殊メソッドはPythonの言語機能と密接に関連しており、それらを正しく動作させるためには予約された名前が必要です。
# 
# アンダースコアによって、これらの特殊メソッドが明示的に区別され、特殊メソッドと一般的なメソッドや変数名との間で名前の衝突を回避することができます。
# ```

# 次のコードは、```equal()```という通常のメソッドを定義します。
# 
# このメソッドにより、文字列を小文字へ変換してから比較します。

# In[25]:


class Word:
    def __init__(self, text):
        self.text = text

    def equal(self,word2):
        return self.text.lower() == word2.text.lower()


# In[26]:


sendai=Word("Sendai")
sendai2=Word("sendai")
tokyo=Word("Tokyo")


# In[27]:


sendai.equal(tokyo)


# In[28]:


sendai.equal(sendai2)


# In[29]:


sendai == sendai2


# ここで、組み込み型と同じように、```==```を使いたいときは、```equal()```メソッドを```__eq__```という特殊メソッドに変更します。

# In[30]:


class Word:
    def __init__(self, text):
        self.text = text

    def __eq__(self,word2):
        return self.text.lower() == word2.text.lower()


# In[31]:


sendai=Word("Sendai")
sendai2=Word("sendai")
tokyo=Word("Tokyo")


# In[32]:


sendai == sendai2


# In[33]:


sendai == tokyo


# | メソッド名              | 説明                                                                            |
# |----------------------|---------------------------------------------------------------------------------|
# | `__eq__(self, other)`  | `==`         |
# | `__ne__(self, other)`  | `!=`        |
# | `__lt__(self, other)`  | `<`          |
# | `__le__(self, other)`  | `<=`        |
# | `__gt__(self, other)`  | `>`          |
# | `__ge__(self, other)`  | `>=`          |
# 
# 

# | メソッド名             | 説明                                                                                        |
# |----------------------|-----------------------------------------------------------------------------------------|
# | `__add__(self, other)`   | `+`                      |
# | `__sub__(self, other)`   | `-`                       |
# | `__mul__(self, other)`   | `*`                  |
# | `__truediv__(self, other)` |`/`                |
# | `__floordiv__(self, other)` | `//`                  |
# | `__mod__(self, other)`   | `%`                      |
# | `__pow__(self, other)`   | `**`                          |

# | メソッド名             | 説明                                                                                        |
# |----------------------|-----------------------------------------------------------------------------------------|
# | `__str__(self)`   | オブジェクトの文字列表現を返す。```str()```                      |
# | `__repr__(self)`   | オブジェクトの公式な表現を返すために使用されます。```repr()```                       |
# | `__len__(self)`   | オブジェクトの長さ（要素数）を返すために使用されます。```len()```                 |
# 

# In[34]:


class Word:
    def __init__(self, text):
        self.text = text
    def __eq__(self,word2):
        return self.text.lower() == word2.text.lower()
    def __repr__(self):
        return "The word is {}".format(self.text)
    def __str__(self):
        return self.text.upper()


# In[35]:


sendai=Word("Sendai")


# In[36]:


sendai


# In[37]:


print(sendai)


# ````{tab-set}
# ```{tab-item} 実習問題
# クラスPersonに二人の年齢は等しいか、異なるか、より小さいか、より大きいか、を判断する演算を特殊メソッドで定義してください。
# ```
# ````
