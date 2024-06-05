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