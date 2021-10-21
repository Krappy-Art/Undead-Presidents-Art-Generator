"""
Building an Undead President image
    After each choice, put the chosen entity into a dict so we can refer back to it for rules
    Choose background
    Choose face
    Choose hat
        If face = Hillary, and hat = helmet
            choose none
    Choose jacket
        If face = Hillary, and jacket = Red Flanel | Red Hoodi
            keep choosing jacket until you get something else
        If Clown Suit|BDU CAMO| Bathrobe
            Choose shirt None
        If Blue lewinski  Dress
            Choose shirt until you get None | Rainbow | American Flag
    Choose shirt
        If shirt already chosen, skip
        If jacket = Blue lewinski  Dress
                Choose shirt until you get None | Rainbow | American Flag
        if shirt = Rainbow|American Flag|White Color
            Choose tie
    Choose 4 objects
        Per choice
            If hat != None and we choose Gash OR we choose an object that conflicts with an already chosen object,
                ignore the choice and move on
"""

from layer_lists import *
from random import choices
from random import seed
import json

objects_per_image = 4
rand_seed = 564229865
total_nft = 3000

def choose_layer(selections: dict, list_and_rarity_func, rule_func) -> dict:
    layer_list, rarity_list = list_and_rarity_func()
    selection = choices(layer_list, rarity_list)
    selections = rule_func(selections, selection)

    return selections


def background_rule_func(selections: dict, selection: str) -> dict:
    selections['background'] = selection
    return selections


def face_rule_func(selections: dict, selection: str) -> dict:
    selections['face'] = selection
    return selections


def hat_rule_func(selections: dict, selection: str) -> dict:
    """
        Choose hat
            If face = Hillary, and hat = helmet
                choose none
    """
    if selections['face'] == 'H.Vampire' and selection == 'Helmet':
        selections['hat'] = 'None'
    else:
        selections['hat'] = selection

    return selections


def jacket_rule_func(selections: dict, selection: str) -> dict:
    """
        Choose jacket
            If face = Hillary, and jacket = Red Flanel | Red Hoodi
                keep choosing jacket until you get something else (loop 100 times, if can't find anything, choose None)
            If Clown Suit|BDU CAMO| Bathrobe
                Choose shirt None
    """
    if selections['face'] == 'H.Vampire' and selection in ['Red Flanel', 'Red Hoodi']:
        selection = choose_new_selection_loop(['Red Flanel', 'Red Hoodi'], get_jacket_list_and_rarity)
    if selection in ['Clown Suit', 'Bathrobe', 'BDU CAMO']:
        selections['shirt'] = 'None'

    selections['jacket'] = selection
    return selections


def choose_new_selection_loop(exclusion_list: list, list_and_rarity_func) -> str:
    for i in range(1, 100):
        layer_list, rarity_list = list_and_rarity_func()
        selection = choices(layer_list, rarity_list)
        if selection not in exclusion_list:
            return selection

    return 'None'


def shirt_rule_func(selections: dict, selection: str) -> dict:
    """
    Choose shirt
        If shirt already chosen, skip
        If jacket = Blue lewinski  Dress
                Choose shirt until you get None | Rainbow | American Flag
        if shirt = Rainbow|American Flag|White Color
            Choose tie
    """
    dict_key = 'shirt'
    if dict_key in selections:
        if selection in ['Rainbow', 'American Flag', 'White Color']:
            selections = choose_layer(selections, get_tie_list_and_rarity, tie_rule_func)

        return selections

    if selections['jacket'] == 'Blue lewinski  Dress':
        selection = choose_new_selection_loop(['Brown T', 'White T', 'Hawaiian', 'White Color', ],
                                              get_shirt_list_and_rarity)

    if selection in ['Rainbow', 'American Flag', 'White Color']:
        selections = choose_layer(selections, get_tie_list_and_rarity, tie_rule_func)

    selections['shirt'] = selection
    return selections


def tie_rule_func(selections: dict, selection: str) -> dict:
    selections['tie'] = selection
    return selections


def object_rule_func(selections: dict, selection: str) -> dict:
    """
    Choose 4 objects
        Per choice
            If hat != None and we choose Gash OR we choose an object that conflicts with an already chosen object OR
            we choose an object that's already been chosen
                ignore the choice and move on
    """

    dict_key = 'objects'
    if selection == 'Gash' and selections['hat'] != 'None':
        return selections

    if dict_key not in selections:
        selections[dict_key] = [selection]
        return selections

    if selection in selections['objects']:
        return selections

    if selection == 'Nose Worm' and ['Sunglasses, aviator', 'Presidential covid mask'] in selections['objects']:
        return selections

    if selection == 'Presidential covid mask' and ['Cigar', 'Nose Worm', 'Spider', 'jaw hole', 'Rott'] \
            in selections['objects']:
        return selections

    if selection in ['Cigar', 'Spider', 'jaw hole', 'Rott'] and ['Presidential covid mask'] \
            in selections['objects']:
        return selections

    selections[dict_key].append(selection)
    return selections


def get_random_selections() -> dict:
    current_selections = choose_layer({}, get_background_list_and_rarity, background_rule_func)
    current_selections = choose_layer(current_selections, get_face_list_and_rarity, face_rule_func)
    current_selections = choose_layer(current_selections, get_hat_list_and_rarity, hat_rule_func)
    current_selections = choose_layer(current_selections, get_jacket_list_and_rarity, jacket_rule_func)
    current_selections = choose_layer(current_selections, get_shirt_list_and_rarity, shirt_rule_func)

    for i in range(1, objects_per_image):
        current_selections = choose_layer(current_selections, get_object_list_and_rarity, object_rule_func)

    return current_selections


if __name__ == '__main__':
    all_images = {}
    for iteration in range(1, total_nft+1):
        seed(iteration + rand_seed)

        dup_image_check = True
        counter = 1
        while dup_image_check:
            output = get_random_selections()
            if iteration == 1:
                dup_image_check = False
            else:
                checker = list(all_images.values())
                if output in checker:
                    # duplicate - update seed and reselect
                    seed(rand_seed - iteration - counter)
                    counter += 1
                else:
                    # not a duplicate
                    dup_image_check = False

        all_images[iteration] = output

    with open("output.txt", "w") as file1:
        file1.writelines(json.dumps(all_images))
