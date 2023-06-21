#!/usr/bin/env python
# coding: utf-8

# # 標本分布と近似

# 推測統計(inferential statistics)では、母集団に確率モデルを想定し、その確率分布に従う確率変数の実現値としてデータを捉えます。
# 
# $X_1,...,X_n$がランダムサンプルとは、$X_1,...,X_n$がお互いに独立に分布していて、各$X_i$が同一の確率分布$F$に従うことを意味する。これを、$X_1,...,X_n$はお互いに独立に同一分布に従う(independently and identically distributed)といいます。
# 
# $$X_1,...,X_n,\  i,i,d, \sim F$$
# 
# 推測統計はでは、このように、データ$x_1,...,x_n$を確率変数$X_1,...,X_n$の一つの実現値と捉えることによって、推定、検定、予測などの推測に関して信頼性を見積もることを可能にしています。

# 母集団の平均$\mu$や分散$\sigma ^2$を母平均(population mean),母分散(population variance)といいます。
# 
# 母数は標本$X_1,...,X_n$に基づいて推定されます。
# $$ 
# \bar{X}=\frac{1}{n}\sum_{i=1}^n X_i,\ S^2=\frac{1}{n}\sum_{i=1}^n (X_i-\bar{X})^2
# $$

# はそれぞれ標本平均と標本分散と呼ばれます。実際には$\mu$は$\bar{X}$の実現値$\bar{x}=\frac{\sum_{i=1}^n x_i}{n}$で推定されることになるが、信頼区間や推定誤差などその推定値の信頼性を与えるためには、確率変数$\bar{X}$の確率分布を求める必要があります。
# 
# 一般に、$\bar{X}$, $S^2$のように、標本$X_1,...,X_n$に基づいて関数で母数を含んでいないもの$t(X_1,...,X_n)$を統計量といい、その確率分布を標本分布(sampling distribution)といいます。
# 
# 平均$\mu$, 分散$\sigma ^2$の確率分布を母集団とするランダムサンプルで、
# $\bar{X}$の平均は、
# $$
# E[\bar{X}]=\frac{1}{n}\sum_{i=1}^n E[X_i] = \frac{1}{n}\sum_{i=1}^n \mu = \mu
# $$
# $S^2$の期待値については、まず、
# \begin{align*}
# &\sum_{i=1}^n(X_i-\bar{X})^2\\
# &= \sum_{i=1}^n (X_i - \mu + \mu - \bar{X})^2\\
# &= \sum_{i=1}^n(X_i - \mu)^2 + 2 \sum_{i=1}^n (X_i - \mu)(\mu - \overline{X}) + \sum_{i=1}^n(\mu - \overline{X})^2 \\
# &= \sum_{i=1}^n (X_i - \mu)^2 -n (\overline{X}-\mu)^2 
# \end{align*}
# より、標本分散の期待値は
# \begin{align*}
# &E[S^2] = E[\frac{1}{n} \sum_{i=1}^n (X_i - \mu)^2 -n (\overline{X}-\mu)^2] \\
# &= \sigma ^2 -n(\frac{\sigma ^2}{n})\\
# &= \frac{n-1}{n} \sigma ^2
# \end{align*}
# 
# 母分散を得るためには、
# \begin{align*}
# E(\frac{n}{n-1}S^2)=\sigma ^2
# \end{align*}
# ここで、$E(\frac{n}{n-1}S^2)$が母分散$\sigma ^2$の不偏推定量を示しています。母分散に対する不偏分散$u^2$は次式で表される。
# 
# $$
# u^2=\frac{n}{n-1}S^2=\frac{1}{n-1} \sum_{i=1}^n(X_i-\bar{X})^2
# $$
# 
# 標本平均の推定誤差は$n$とともに小さくなることを示しています。

# 
