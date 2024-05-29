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


# シーケンス型（sequence types）とは、データが順序付けられているデータ型のことを指します。Pythonなどのプログラミング言語における主なシーケンス型には以下のようなものがあります：
# 
# リスト（List）: 可変的で、異なるデータ型の要素を含むことができます。
# タプル（Tuple）: 不変的で、一度作成後にはその内容を変更することができません。
# 文字列（String）: 不変的で、文字の並びを表します。
# レンジ（Range）: 数値のシーケンスを生成するために使われます。

# In[1]:


# 定義された一年の平均日数
average_days_per_year = 365.2425

# 1日は24時間、1時間は60分、1分は60秒である
seconds_per_day = 24 * 60 * 60

# 一年の秒数を計算
seconds_per_year = average_days_per_year * seconds_per_day

# 一年の秒数を分と秒に変換
minutes_per_year = seconds_per_year // 60  # 整数分のみ取得
seconds_remaining = seconds_per_year % 60  # 残りの秒数

minutes_per_year, seconds_remaining


# In[ ]:


# Example 1: check if a string is palindrome or not

my_str = 'aIbohPhoBiA'

# make it suitable for caseless comparison
my_str = my_str.casefold()

# reverse the string
rev_str = reversed(my_str)

# check if the string is equal to its reverse
if list(my_str) == list(rev_str):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")


# In[ ]:


# Example 2: check if a string is a Palindrome.

string=str(input("Enter string:"))
if(string==string[::-1]):
    print("The string is a palindrome")
else:
    print("The string isn't a palindrome")

'''
>>Output/Runtime Test Cases
     
Case 1:
Enter string:madam
The string is a palindrome

Case 2:
Enter string:hello
The string isn't a palindrome
'''


# In[ ]:


if num > 1:
   # check for factors
   for i in range(2,num):
        if (num % i) == 0:
            print(num,"is not a prime number")
            print(i,"times",num//i,"is",num)
            break
   else:
        print(num,"is a prime number")
       
# if input number is less than
# or equal to 1, it is not prime
else:
    print(num,"is not a prime number")


# In[ ]:


# Example 1: display all the prime numbers within an interval

lower = 900
upper = 1000

print("Prime numbers between", lower, "and", upper, "are:")

for num in range(lower, upper + 1):
   # all prime numbers are greater than 1
   if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)
    


# In[ ]:


# Example 1: display the Fibonacci sequence up to n-th term

nterms = int(input("How many terms? "))

# first two terms
n1, n2 = 0, 1
count = 0

# check if the number of terms is valid
if nterms <= 0:
    print("Please enter a positive integer")
# if there is only one term, return n1
elif nterms == 1:
    print("Fibonacci sequence upto",nterms,":")
    print(n1)
# generate fibonacci sequence
else:
    print("Fibonacci sequence:")
    while count < nterms:
        print(n1)
        nth = n1 + n2
        # update values
        n1 = n2
        n2 = nth

