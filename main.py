import game_logic.game as g


if __name__ == "__main__":
    def main():
            game_info = g.init_game()
            while len(game_info["player_1"]["hand"]) > 0 and len(game_info["player_2"]["hand"]) > 0:
                g.play_round(game_info["player_1"], game_info["player_2"])

            if game_info["player_1"]["won_pile"] > game_info["player_2"]["won_pile"]:
                winner = f'the winner is: {game_info["player_1"]["name"]}'
            elif game_info["player_2"]["won_pile"] > game_info["player_1"]["won_pile"]:
                winner = f'the winner is: {game_info["player_2"]["name"]}'
            else:
                winner = "the game ended with a draw"

            print(winner, game_info["player_1"]["won_pile"], game_info["player_2"]["won_pile"])


