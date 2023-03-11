#!/usr/bin/env python
# coding: utf-8

# # GitとGitHub
# 
# ## 紹介
# 
# [Git](https://git-scm.com/)は「**パージョン管理システム(Version Control System)**」と呼ばれるものの一つです。
# 
# パージョン管理システムは、バージョン管理とは、一つのファイルやファイルの集合に対して時間とともに加えられていく変更を記録するシステムで、後で特定バージョンを呼び出すことができるようにするためのものです。
# 
# ファイルの「パージョン(変更履歴)」を記録して、いつでも過去の状況に戻したり、過去の変更履歴を比較したり、どのタイミングで問題が起こっているかといった様々なことができるようになって、プログラム開発やファイル管理を補助するシステムです。
# 
# ```{margin}
# 様々な方法でGitを使うことができます。この授業はコマンドラインツールとVSCodeでGitを使うことにします。コマンドラインツールを利用しますので、Macの場合はターミナル、Windowsの場合はコマンド・プロンプトやPowerShellを起動する方法を調べてください。
# ```
# 
# パージョン管理システムはたくさんの種類がありますが、現在最も利用されているのはGitです。さらに、[**GitHub**](https://github.com/)などの**リモートリポジトリ**と組み合わせることで、クラウドでデータを管理したり、プロジェクトを共同開発するとき強力なツールとなります。
# 
# ![](./Figure/remote.png)

# ## インストール
# 
# ### Git
# 
# #### Gitインストール
# 
# [公式サイト](https://git-scm.com/downloads)からGitをインストールする。
# 
# #### GitHubの初期設定
# - GitHubアカウントを作成します。
# - ターミナルを開きます。
# - 次の git コマンドでユーザー情報を設定する。
# ```
# git config --global user.name "First-name Family-name"
# git config --global user.email "username@example.com"
# ```
# - 次の git コマンドでSSHキーを生成する。
# ```
# cd ~/.ssh
# ssh-keygen -t rsa
# ```
# - 任意のパスフレーズを入力してEnter（2回）。パスフレーズが不要であれば空欄のままEnterでよい。
# - SSH Keyを格納するディレクトリに移動します。```ls```でファイルを確認します。```id_rsa.pub```というファイルがあるはずです。
# - ```cat id_rsa.pub```でSSHキーを開く、```ssh-rsa XXX```を全てコピーします。
# - Githubのページの右上で、プロフィール画像をクリックし、続いてSettings→Access→New SSH key→Add SSH keyをクリックしてください。
# - キーを ```Key``` フィールドに貼り付けます。
# - ```Add SSH key```をクリックしてください。
# - ターミナルで```ssh -T git@github.com```を実行します。もしGitHubと連携できましたら、以下の内容が表示されます。
# ```
# Hi USERNAME! You've successfully authenticated, but GitHub does not provide shell access.
# ```
# ### VSCodeのインストール
# 
# [公式サイト](https://code.visualstudio.com/)からVSCodeをインストールする。
# 
# ```{note}
# VSCodeは強力なコードエディターであり、様々なプログラミング言語に機能を提供する幅広い拡張機能を備えた軽量の汎用統合開発環境 (IDE) です。VSCodeでより簡単的に・効率的にGitを操作できます。また、VSCodeでは便利な機能が豊富に搭載されている[Python拡張機能](https://learn.microsoft.com/ja-jp/training/modules/python-install-vscode/5-exercise-install-python-extension?pivots=linux)もたくさんあります。
# ```

# ## Gitの基本操作

# 
# Git プロジェクトを取得するには、大きく二通りの方法があります。 
# - 既存のプロジェクトやディレクトリを Git にインポートする方法。
# - 既存の Git リポジトリを別のサーバーからクローンする方法です。
# 
# まず、既存のプロジェクトやディレクトリを Git にインポートし、ファイルをコミットと履歴の管理を説明します。
# 
# #### 既存のディレクトリでのリポジトリの初期化
# 
# ```{margin}
# 空のディレクトリではなくすでに存在するファイルのバージョン管理を始めたい場合は、まずそのファイルを監視対象に追加する。例えば、すでに存在する```myfile.txt```を以下のコマンドで追加します。```git add myfile.txt```
# ```
# ````{tab-set}
# 
# ```{tab-item} ターミナル操作
# 
# - ディレクトリを作ろう ```mkdir test``` → ```cd test```
# - **リポジトリの初期化** ```git init```
# ```
# 
# ```{tab-item} VSCode操作
# 
# - 「ファイル」→「フォルダーを開く』→　ディレクトリを選択。VSCode左側の『エクスプローラー』に、開いたフォルダ名が表示されます。
# -  サイドバーの「ソース管理」(Source Control)を表示して，「リポジトリの初期化」(Initialize Rspository)をクリックします。
# 
# ![](./Figure/git_init.png)
# 
# ```
# ````

# #### コミット(commit)
# 
# リポジトリを作成すると、そこに対するファイルの変更履歴を登録することができます。その操作をコミット(commit)といいます。
# 
# コミットを実行すると、リポジトリの内では、前回コミットした時の状態から現在の状態までの差分を記録したリビジョンと呼ばれるものが作成されます。
# 
# ![](./Figure/commit1.png)
# 
# - Gitの管理下に置かれた、みなさんが実際に作業をしているディレクトリのことをワークツリーと呼びます。
# - Gitではリポジトリとワークツリーの間にはインデックスというものが存在しています。インデックスとは、リポジトリにコミットする準備をするための場所のことです。
# - コミットでファイルの状態を記録するためには、まずインデックスにファイルを登録し、そして変更をコミットするプロセスになります。

# ````{tab-set}
# 
# ```{tab-item} ターミナル操作
# 
# - ディレクトリで任意のファイルを作る。例えば、```echo This is some text > myfile.txt```
# - ```git status```でステータスを確認すると、```myfile.txt```は```Untracked file```であり、つまり、また追跡対象になっていないです。
# ![](./Figure/commit_example1.png)
# - ```git add myfile.txt```で```myfile.txt```を追跡対象に追加し、再び```git status```でステータスを確認すると、```Changes to be committed```、すなわち、コミット待ちと表示されています。
# ![](./Figure/commit_example2.png)
# - コミットをするには```git commit```というコマンドを使います。コミットをする際、コミットの内容を説明するメッセージを記入する必要があります。```-m``` というオプションを付加して、その後メッセージを入れましょう。例えば、```git commit -m "myfileを作成ました"```
# ![](./Figure/commit_example3.png)
# 
# ```
# 
# ```{tab-item} VSCode操作
# 
# - ファイルを作成すると、VSCodeが自動的に変更を検出し、ソース管理サイドバーで数字が表示されます。
# ![](./Figure/commit_example4.png)
# - ソース管理に更新ファイルの一覧が表示されます。```+```アイコンでステージング操作を行います。
# - ステージングした状態からコミットメッセージを入力して、```コミット(Commit)```アイコンでコミットが完了します。
# ![](./Figure/commit_example5.png)
# ```
# ````

# ```{note}
# コミットを特定するためには、```3be9fa78156da4febd9b9cea28b71c15d8f95c4d```のような形のハッシュを使います。
# ```

# 
