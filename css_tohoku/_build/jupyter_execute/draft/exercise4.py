#!/usr/bin/env python
# coding: utf-8

# # 練習課題
# 
# ## 課題1
# 以下の指示に従って、```Sphere```というクラスを作成しなさい。
# 
# - インスタンス化時に```radius```という値を受け取る
# - ```surface_area```というメソッドで表面積を計算する
# 
# $$ S = 4 \pi r^2 \$$
# 
# - ```volume```というメソッドで体積を計算する
# 
# $$ V = \frac{4}{3} \pi r^3 \$$
# 

# In[1]:


class Sphere():
    pass


# In[2]:


s = Sphere(1)


# In[ ]:


s.surface_area()


# In[ ]:


s.volume()


# ## 課題2
# 
# 「スイカ割りゲーム」のプログラムをクラスの形に整理してください。

# In[1]:


import random
import math

BOARD_SIZE = 5  # ボードサイズを定義

def generate_position(board_size):
    # スイカとプレイヤーの初期位置をランダムに生成
    return (random.randrange(0, board_size), random.randrange(0, board_size))

def determine_move(player_pos, target_pos):
    # スイカに向かってプレイヤーを移動させる方向を決定
    current_x, current_y = player_pos
    target_x, target_y = target_pos

    move_x = 1 if current_x < target_x else -1 if current_x > target_x else 0
    move_y = 1 if current_y < target_y else -1 if current_y > target_y else 0

    return (move_x, move_y)

def move_player(player_pos, move_x, move_y):
    # プレイヤーの位置を更新
    new_x = player_pos[0] + move_x
    new_y = player_pos[1] + move_y
    return (new_x, new_y)

def play_game(board_size):
    suika_pos = generate_position(board_size)
    player_pos = generate_position(board_size)

    while suika_pos != player_pos:
        move_x, move_y = determine_move(player_pos, suika_pos)
        player_pos = move_player(player_pos, move_x, move_y)
        print("プレイヤーが移動しました:", player_pos)

    print("スイカを見つけました！")

# ゲームを開始
play_game(BOARD_SIZE)


# - 属性
#     - ```board_size```
#     - ```suika_pos```
#     - ```player_pos```
# - メソッド
#     - ```calc_distance```: 二点間のユークリッド距離を計算
#     - ```move_player```: プレイヤーをスイカに向かって一歩移動させます。プレイヤーの位置を更新します。
#     - ```play_game```: ゲームのループを実行します。プレイヤーがスイカの位置に到達するまで、プレイヤーを移動させます。

# In[2]:


class WatermelonHunt:
    pass


# In[3]:


import random
import math

class WatermelonHunt:
    def __init__(self, board_size=5):
        self.board_size = board_size
        self.suika_pos = (random.randrange(0, self.board_size), random.randrange(0, self.board_size))
        self.player_pos = (random.randrange(0, self.board_size), random.randrange(0, self.board_size))
    
    def calc_distance(self, pos1, pos2):
        diff_x = pos1[0] - pos2[0]
        diff_y = pos1[1] - pos2[1]
        return math.sqrt(diff_x**2 + diff_y**2)

    def move_player(self):
        current_x, current_y = self.player_pos
        target_x, target_y = self.suika_pos

        if current_x < target_x:
            current_x += 1
        elif current_x > target_x:
            current_x -= 1

        if current_y < target_y:
            current_y += 1
        elif current_y > target_y:
            current_y -= 1

        self.player_pos = (current_x, current_y)
        print("プレイヤーが移動しました:", self.player_pos)
    
    def play_game(self):
        while self.suika_pos != self.player_pos:
            distance = self.calc_distance(self.suika_pos, self.player_pos)
            print("スイカまでの距離:", distance)
            self.move_player()
        
        print("スイカを見つけました！")


# In[7]:


game = WatermelonHunt(board_size=10)
game.play_game()


# ## 課題3
# 
# ```verbose```という属性を追加する。
# 
# verboseがTrueの場合、プレイヤーの移動やスイカまでの距離などの情報(```print(...)```)が出力されます。逆にverboseがFalseの場合、これらの情報は出力されません。

# In[ ]:


import random
import math

class WatermelonHunt:
    def __init__(self, board_size=5, verbose=True):
        self.board_size = board_size
        self.suika_pos = (random.randrange(0, self.board_size), random.randrange(0, self.board_size))
        self.player_pos = (random.randrange(0, self.board_size), random.randrange(0, self.board_size))
        self.verbose = verbose
    pass


# ## 課題4
# 
# クラスに移動数をカウントするメソッドを追加する。
# 
# そのメソッドは、指定された回数のゲームをプレイし、それぞれのゲームでの移動回数の平均を計算します。これにより、ボードのサイズに応じてプレイヤーがスイカに到達するまでに必要な平均移動回数を推定することができます。

# In[ ]:





# ## 課題5
# 
# 複数のプレイヤーが参加し、最初にスイカに到達したプレイヤーが勝つゲームを想定します。
# 
# ```player_num```という属性を追加し、プレイヤーの数を制御します。
# 
# 各プレイヤーはそれぞれ独立してスイカに向かって移動し、ゲームの進行は各ターンで全プレイヤーが一度ずつ移動する。あるプレイヤーがスイカに到達したら、ゲームは終了します。
# 

# 

# In[8]:


import random
import math

class WatermelonHunt:
    def __init__(self, board_size=5, player_num=2):
        self.board_size = board_size
        self.suika_pos = (random.randrange(0, self.board_size), random.randrange(0, self.board_size))
        self.player_positions = [(random.randrange(0, self.board_size), random.randrange(0, self.board_size)) for _ in range(self.player_num)]
        self.player_num = player_num
        self.winner = None

    def calc_distance(self, pos1, pos2):
        diff_x = pos1[0] - pos2[0]
        diff_y = pos1[1] - pos2[1]
        return math.sqrt(diff_x**2 + diff_y**2)

    def move_player(self, player_index):
        current_x, current_y = self.player_positions[player_index]
        target_x, target_y = self.suika_pos

        if current_x < target_x:
            current_x += 1
        elif current_x > target_x:
            current_x -= 1

        if current_y < target_y:
            current_y += 1
        elif current_y > target_y:
            current_y -= 1

        self.player_positions[player_index] = (current_x, current_y)
        print(f"プレイヤー {player_index + 1} が移動しました: {self.player_positions[player_index]}")
        
        if self.player_positions[player_index] == self.suika_pos:
            self.winner = player_index + 1

    def play_game(self):
        while self.winner is None:
            for i in range(self.player_num):
                pass
        
        print(f"プレイヤー {self.winner} がスイカを見つけました！")


# In[ ]:




