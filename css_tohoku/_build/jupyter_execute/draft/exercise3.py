#!/usr/bin/env python
# coding: utf-8

# # 練習課題
# 
# ## 課題1
# 
# 「スイカ割りゲーム」のプログラムを作成する。
# 
# - スイカとプレイヤーの初期位置をランダムに設定
# - プレイヤーがスイカの位置に到達するまでに移動を続けて、移動する度にプレイヤーとスイカの距離を計算する
# - スイカに向かってプレイヤーを移動させる方向を決定する

# In[1]:


import random
import math

BOARD_SIZE = 5  # ボードサイズを定義

def calc_distance(pos1, pos2):
    # 二点間のユークリッド距離を計算
    diff_x = pos1[0] - pos2[0]
    diff_y = pos1[1] - pos2[1]
    return math.sqrt(diff_x**2 + diff_y**2)

# スイカとプレイヤーの初期位置をランダムに設定
suika_pos = (random.randrange(0, BOARD_SIZE), random.randrange(0, BOARD_SIZE))
player_pos = (random.randrange(0, BOARD_SIZE), random.randrange(0, BOARD_SIZE))

# プレイヤーがスイカの位置に到達するまで処理を続ける
while (suika_pos != player_pos):
    # スイカまでの距離を表示
    distance = calc_distance(suika_pos, player_pos)
    print("スイカまでの距離:", distance)

    # スイカに向かってプレイヤーを移動させる方向を決定
    current_x, current_y = player_pos
    target_x, target_y = suika_pos

    if current_x < target_x:
        current_x += 1
    elif current_x > target_x:
        current_x -= 1

    if current_y < target_y:
        current_y += 1
    elif current_y > target_y:
        current_y -= 1

    # プレイヤーの位置を更新
    player_pos = (current_x, current_y)
    print("プレイヤーが移動しました:", player_pos)

print("スイカを見つけました！")


# このプログラムを関数で分割して、再作成してください。
# 
# - 初期位置の作成の関数```generate_position()```
# - 移動先を決める関数
# - 移動処理の関数```move_player()```
# - ゲームの主なループを実行する関数```play_game()```

# In[ ]:





# ## 課題2
# 
# 複数のプレイヤーが参加し、最初にスイカに到達したプレイヤーが勝つゲームを想定してください。
# 
# 各プレイヤーはそれぞれ独立してスイカに向かって移動し、ゲームの進行は各ターンで全プレイヤーが一度ずつ移動する。
# 
# あるプレイヤーがスイカに到達したら、ゲームは終了します。
# 
# このようなシナリオを実装してください。
# 

# In[ ]:





# 
