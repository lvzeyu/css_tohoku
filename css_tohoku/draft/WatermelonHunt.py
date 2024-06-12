import random
import math
import argparse

class WatermelonHunt:
    def __init__(self, board_size=5, player_num=2):
        self.board_size = board_size
        self.player_num = player_num
        self.suika_pos = (random.randrange(0, self.board_size), random.randrange(0, self.board_size))
        self.player_positions = [(random.randrange(0, self.board_size), random.randrange(0, self.board_size)) for _ in range(self.player_num)]
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
                distance = self.calc_distance(self.suika_pos, self.player_positions[i])
                print(f"プレイヤー {i + 1} のスイカまでの距離: {distance}")
                self.move_player(i)
                if self.winner is not None:
                    break
        
        print(f"プレイヤー {self.winner} がスイカを見つけました！")

#if __name__ == "__main__":
#    # ゲームを開始する
#    game = WatermelonHunt(board_size=5, player_num=3)
#    game.play_game()


#if __name__ == "__main__":
#    # 引数を処理する
#    parser = argparse.ArgumentParser(description="スイカ狩りゲーム")
#    parser.add_argument("--board_size", type=int, default=5, help="ボードのサイズ")
#    parser.add_argument("--player_num", type=int, default=2, help="プレイヤーの人数")
#    args = parser.parse_args()

    # ゲームを開始する
#    game = WatermelonHunt(board_size=args.board_size, player_num=args.player_num)
#    game.play_game()


#ゲームを開始する
game = WatermelonHunt(board_size=5, player_num=3)
game.play_game()
