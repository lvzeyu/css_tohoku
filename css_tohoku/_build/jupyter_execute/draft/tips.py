#!/usr/bin/env python
# coding: utf-8

# # Tips

# ## VSCode

# ### 作業リポジトリを指定する
# 
# gitリポジトリ内で複数のgitリポジトリの履歴を管理することができますが、場合による混乱になることもありますので、作業リポジトリを指定して、VSCodeを使う方がいいです。

# - メニュー　→　ファイル　→ 新しいウィンドウ
# - 新しいウィンドウで、左側のツールバー　→　エクスプローラー　→ フォルダーを開く
# - 子ディレクトリを選択

# ## Git/GitHub
# 

# ### 指定するリポジトリから```git pull```をする方法
# 

# ```git pull <original_repository>```という形で、指定するリポジトリから```git pull```をすることができます。
# 
# ```https://github.com/lvzeyu/chss_2023_assignment```から最新の状況を同期する操作を例として説明します。

# - ```cd ~/chss_2023_assignment```
# - ```git remote -v```でgitリポジトリに関連付けられたリモートリポジトリの一覧とそのURLを表示する
# - ```origin/upstream  git@github.com:lvzeyu/chss_2023_assignment.git```というリモートリポジトリが表示されることを確認
# - ```git branch <branch_name>```で自分のブランチを作成・移動
# - ```git pull origin main```または ```git pull upstream main```でローカルリポジトリブランチをリポジトリの最新状態に更新します。
# 

# ````{tab-set}
# 
# ```{tab-item} ターミナル操作
# 
# - ```cd ~/chss_2023_assignment```
# - ```git remote -v```でgitリポジトリに関連付けられたリモートリポジトリの一覧とそのURLを表示する
# - ```origin/upstream  git@github.com:lvzeyu/chss_2023_assignment.git```というリモートリポジトリが表示されることを確認
# - ```git branch <branch_name>```で自分のブランチを作成・移動
# - ```git pull origin main```または ```git pull upstream main```でローカルリポジトリブランチをリポジトリの最新状態に更新します。
# ```
# 
# ```{tab-item} VSCode操作
# -「ソース管理」→「...」をクリックします。
# - 「プル、プッシュ」→ 「指定元からプル」
# - リモートリポジトリのブランチを指定してください。基本的には```origin main```または```upstream main```であるはずです。
# 
# ```

# 
