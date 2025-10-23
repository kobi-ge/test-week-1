from utils.deck import *
def create_player(name:str = "AI") -> dict:
    player_dict = {"name": name, "hand": [], "won_pile": []}
    return player_dict

def init_game() -> dict:
    p1 = create_player("kobi")
    p2 = create_player()
    deck = shuffle(create_deck())
    p1_half = []
    p2_half = []
    for card in range(len(deck)):
        if card < 26:
            p1_half.append(deck[card])
        else:
            p2_half.append(deck[card])
    p1["hand"] = p1_half
    p2["hand"] = p2_half
    game_dict = {"deck": deck, "player_1": p1, "player_2": p2}
    return game_dict

def play_round(p1:dict, p2:dict):
    top_card_p1 = p1["hand"].pop(0)
    top_card_p2 = p2["hand"].pop(0)
    higher = compare_cards(p1, p2)
    round_winner = None
    if higher == "p1":
        round_winner = p1
    elif higher == "p2":
        round_winner = p2
    else:
        round_winner = None
    if round_winner:
        round_winner["hand"].append(top_card_p1)
        round_winner["hand"].append(top_card_p1)
