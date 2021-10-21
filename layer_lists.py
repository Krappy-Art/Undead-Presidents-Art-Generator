def get_background_list_and_rarity() -> (list, list):
    background_list = [
        'White',
        'Red',
        'Blue',
        'Green',
        'Orange',
        'Purple'
    ]
    background_rarity = [
        0.30,
        0.22,
        0.08,
        0.20,
        0.18,
        0.02,
    ]
    return background_list, background_rarity


def get_face_list_and_rarity() -> (list, list):
    face_list = [
        'J.Werewolf',
        'J.Zombie',
        'J.Vampire',
        'J.Mummy',
        'T.Werewolf',
        'T.Zombie',
        'T.Vampire',
        'T.Mummy',
        'O.Werewolf',
        'O.Zombie',
        'O.Vampire',
        'O.Mummy',
        'G.Mummy',
        'B.Werewolf',
        'B.Vampire',
        'B.Zombie',
        'H.Vampire',
    ]
    face_rarity = [
        0.07,
        0.07,
        0.07,
        0.07,
        0.06,
        0.06,
        0.06,
        0.06,
        0.06,
        0.06,
        0.06,
        0.06,
        0.06,
        0.06,
        0.06,
        0.05,
        0.01,
    ]
    return face_list, face_rarity


def get_hat_list_and_rarity() -> (list, list):
    hat_list = [
        'None',
        'Red Trucker MZGA',
        'Cowboy hat',
        'Blue Trucker Seal',
        'Blue Trucker Jackass',
        'Helmet',
    ]
    hat_rarity = [
        0.50,
        0.10,
        0.10,
        0.10,
        0.10,
        0.10,
    ]
    return hat_list, hat_rarity


def get_jacket_list_and_rarity() -> (list, list):
    jacket_list = [
        'None',
        'Clown Suit',
        'Leather jacket',
        'Doctor Jacket',
        'Blue lewinski  Dress',
        'Bathrobe',
        'Red Flanel',
        'Red Hoodi',
        'Judge Robe',
        'BDU CAMO',
        'Blue suit',
        'Black suit',
        'Gold Suit',
    ]
    jacket_rarity = [
        0.25,
        0.01,
        0.10,
        0.10,
        0.01,
        0.01,
        0.01,
        0.03,
        0.12,
        0.01,
        0.17,
        0.17,
        0.01,
    ]
    return jacket_list, jacket_rarity


def get_shirt_list_and_rarity() -> (list, list):
    shirt_list = [
        'None',
        'Brown T',
        'White T',
        'Hawaiian',
        'Rainbow',
        'American Flag',
        'White Color',
    ]
    shirt_rarity = [
        0.01,
        0.05,
        0.02,
        0.05,
        0.11,
        0.21,
        0.55,
    ]
    return shirt_list, shirt_rarity


def get_tie_list_and_rarity() -> (list, list):
    tie_list = [
        'None',
        'Black',
        'Blue',
        'Red',
        'Blue Stripe',
        'Gold',
        'Rainbow',
        'Pink Polkadot',
        'Purple',
        'Ripped',
    ]
    tie_rarity = [
        0.30,
        0.10,
        0.10,
        0.10,
        0.10,
        0.02,
        0.03,
        0.10,
        0.10,
        0.05,
    ]
    return tie_list, tie_rarity


def get_object_list_and_rarity() -> (list, list):
    object_list = [
        'None',
        'Sunglasses, aviator',
        'Presidential covid mask',
        'Cigar',
        'Nose Worm',
        'Maggots',
        'Spider',
        'jaw hole',
        'Rott',
        'Gash',
        'Cuts',
        'Bite',
        'Blood',
    ]
    object_rarity = [
        0.15,
        0.05,
        0.03,
        0.03,
        0.05,
        0.09,
        0.06,
        0.07,
        0.10,
        0.09,
        0.10,
        0.08,
        0.10,
    ]
    return object_list, object_rarity