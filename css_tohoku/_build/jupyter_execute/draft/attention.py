#!/usr/bin/env python
# coding: utf-8

# # Attention

# ## 8.1 Attention の仕組み

# ### 8.1.1 seq2seqの問題点
# seq2seqでは、「Encoder側の最後の隠れ状態$\mathbf{h}_{T-1} = (h_{0,0}^{(T-1)}, \cdots, h_{N-1,H-1}^{(T-1)})$」を「Decoder側の最初のLSTMレイヤ」に入力しました。

# In[1]:


from IPython.display import HTML

HTML("""
    <video alt="hydrangea" width="640" height="480" controls>
        <source src="https://lena-voita.github.io/resources/lectures/seq2seq/general/seq2seq_training_with_target.mp4">
    </video>
""")


# Encoderは無理やりに情報を固定長のベクトルへと押し込むので、時系列サイズ$T$が大きいと全ての単語の情報がDecoderに伝わらない可能性があります。
# 
# ![seq2seq_problem](https://lena-voita.github.io/resources/lectures/seq2seq/attention/bottleneck-min.png "seq2seq_problem")
# 

# ### 8.1.2 Encoderの改良

# **ポイント**: 入力する文章の長さ(単語の数)に応じてEncoderの長さを変化すべきです。
# 
# ![seq2seq_attention](https://camo.qiitausercontent.com/0672413a2ed55d707906253eaef08a4fe012896e/68747470733a2f2f71696974612d696d6167652d73746f72652e73332e61702d6e6f727468656173742d312e616d617a6f6e6177732e636f6d2f302f3230393730352f32353233333635302d313135352d653730382d613265662d3835616230626661346538362e706e67 "seq2seq_attention")

# ### 8.1.3 Decoderの改良

# Decoderの基本構造
# - Enocoder最後の隠れ状態ベクトル $\mathbf{h}$ は, Decoder最初のLSTMレイヤに渡すことにします。
# - **Attention**: 各時刻においてLSTMレイヤの隠れ状態とEncoderからの $\mathbf{hs}$ を受け取って、そして必要な情報だけに注意を向けさせ、その情報から時系列変化を行います。
# 
# 
# - **Attention_weight**
#  - Encoderの<strong>ベクトルhs0〜hs4</strong>とDecoderの<strong>ベクトルh</strong>の<strong>積</strong>を求め、それぞれ<strong>列方向(axis=2)</strong>で足した数値は、２つののベクトルの<strong>類似度が高いほど大きく</strong>なります。この数値にSoftmaxを通すと、ベクトルhs0〜hs4を<strong>どういう重み付けでアテンション(参照)すべき</strong>かを表す<strong>ベクトルa</strong>が得られます。</p>
# 
# 

# ![attention](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F209705%2F10f8f28c-f6da-dbf4-cf53-309b76b96662.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&w=1400&fit=max&s=85733fb2feb2f18afaac729b04b72b1f"attention")

# 
