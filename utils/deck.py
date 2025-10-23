import random
def create_card(rank:str, suite:str) ->dict:
    cards_value = {2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9, 10:10, "j":11, "q":12, "k":13,"a": 14}
    current_card_value = cards_value[int(rank)]
    card_info = {"rank": rank, "suite": suite, "value": current_card_value}
    return card_info


def compare_cards(p1_card:dict, p2_card:dict) -> str:
    if p1_card["value"] > p2_card["value"]:
        return "p1"
    elif p2_card["value"] > p1_card["value"]:
        return "p2"
    return "war"


def create_deck() -> list[dict]:
    cards_list = []
    card_dict = {}
    for rank in range(2, 15):
        value = rank
        for suite in ["H", "C", "D", "S"]:
            card_dict["value"] = value
            if rank == 11:
                rank = "j"
            elif rank == 12:
                rank = "q"
            elif rank == 13:
                rank = "k"
            elif rank == 14:
                rank = "a"
            card_dict["rank"] = rank
            card_dict["suite"] = suite
            cards_list.append(card_dict)
            card_dict = {}
    return cards_list

def shuffle(deck:list[dict]) -> list[dict]:
    times = 0
    while times < 1000:
        index1 = random.randint(0, 51)
        index2 = random.randint(0, 51)
        if index1 == index2:
            continue
        deck[index1], deck[index2] = deck[index2], deck[index1]
        times += 1
    return deck



