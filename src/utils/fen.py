def precompute_fen_template():
    piece_types = ["p", "n", "b", "r", "q", "k", "P", "N", "B", "R", "Q", "K", "empty"]
    positions = [f"{col}{row}" for row in range(1, 9) for col in "abcdefgh"]
    board_template = {f"{piece}_{pos}": 0 for piece in piece_types for pos in positions}
    other_features = {
        "Turn_w": 0,
        "Turn_b": 0,
        "Castling_K": 0,
        "Castling_Q": 0,
        "Castling_k": 0,
        "Castling_q": 0,
        "Castling_None": 0,
        "En_Passant_None": 0,
        **{
            f"En_Passant_{sq}": 0
            for sq in [
                "a3",
                "b3",
                "c3",
                "d3",
                "e3",
                "f3",
                "g3",
                "h3",
                "a6",
                "b6",
                "c6",
                "d6",
                "e6",
                "f6",
                "g6",
                "h6",
            ]
        },
        # "Halfmove_Clock": 0,
        # "Fullmove_Number": 0,
    }

    return {**board_template, **other_features}


def fen_to_one_hot_optimized(fen: str) -> dict[str, int]:
    board_fen, turn, castling, en_passant, halfmove_clock, fullmove_number = fen.split()

    template = precompute_fen_template()
    one_hot = template.copy()

    rows = board_fen.split("/")
    for i, fen_row in enumerate(rows):
        row_number = 8 - i
        col_index = 0
        for char in fen_row:
            if char.isdigit():
                col_index += int(char)
            else:
                col_letter = chr(ord("a") + col_index)
                one_hot[f"{char}_{col_letter}{row_number}"] = 1
                col_index += 1

    one_hot[f"Turn_w"] = 1 if turn == "w" else 0
    one_hot[f"Turn_b"] = 1 if turn == "b" else 0
    one_hot[f"Castling_K"] = 1 if "K" in castling else 0
    one_hot[f"Castling_Q"] = 1 if "Q" in castling else 0
    one_hot[f"Castling_k"] = 1 if "k" in castling else 0
    one_hot[f"Castling_q"] = 1 if "q" in castling else 0
    one_hot[f"Castling_None"] = 1 if castling == "-" else 0
    one_hot[f"En_Passant_None"] = 1 if en_passant == "-" else 0
    if en_passant != "-":
        one_hot[f"En_Passant_{en_passant}"] = 1
    # one_hot[f"Halfmove_Clock"] = int(halfmove_clock)
    # one_hot[f"Fullmove_Number"] = int(fullmove_number)
    return one_hot
