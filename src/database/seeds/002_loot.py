import os
import json

PATH_TO_DATA = os.path.dirname(__file__)

MAX_RANK = 100

def get_path(file):
    return os.path.join(PATH_TO_DATA, 'data', '{}.json'.format(file))

'''
individual treasure -> max CR -> max roll on d100 -> list of die rolls for coins
treasure hoard      -> max CR -> max roll on d100 -> valuables + magic items received
                              -> coins            -> list of die rolls for coins
'''
with open(get_path('loot'), 'w+') as f:
    data = {
        'individual treasure': {
            4: {
                30:  [{'num_dice': 5, 'die_type': 6, 'piece_type': 'copper',   'multiplier': 1}],
                60:  [{'num_dice': 4, 'die_type': 6, 'piece_type': 'silver',   'multiplier': 1}],
                70:  [{'num_dice': 3, 'die_type': 6, 'piece_type': 'electrum', 'multiplier': 1}],
                95:  [{'num_dice': 3, 'die_type': 6, 'piece_type': 'gold',     'multiplier': 1}],
                100: [{'num_dice': 3, 'die_type': 6, 'piece_type': 'platinum', 'multiplier': 1}],
            },
            10: {
                30:  [{'num_dice': 4, 'die_type': 6, 'piece_type': 'copper',   'multiplier': 100},
                      {'num_dice': 1, 'die_type': 6, 'piece_type': 'electrum', 'multiplier': 10}],
                60:  [{'num_dice': 6, 'die_type': 6, 'piece_type': 'silver',   'multiplier': 10},
                      {'num_dice': 2, 'die_type': 6, 'piece_type': 'gold',     'multiplier': 10}],
                70:  [{'num_dice': 1, 'die_type': 6, 'piece_type': 'electrum', 'multiplier': 100},
                      {'num_dice': 2, 'die_type': 6, 'piece_type': 'gold',     'multiplier': 10}],
                95:  [{'num_dice': 4, 'die_type': 6, 'piece_type': 'gold',     'multiplier': 10}],
                100: [{'num_dice': 2, 'die_type': 6, 'piece_type': 'gold',     'multiplier': 10},
                      {'num_dice': 3, 'die_type': 6, 'piece_type': 'platinum', 'multiplier': 1}],
            },
            16: {
                20:  [{'num_dice': 4, 'die_type': 6, 'piece_type': 'silver',   'multiplier': 100},
                      {'num_dice': 1, 'die_type': 6, 'piece_type': 'gold',     'multiplier': 100}],
                35:  [{'num_dice': 1, 'die_type': 6, 'piece_type': 'electrum', 'multiplier': 100},
                      {'num_dice': 1, 'die_type': 6, 'piece_type': 'gold',     'multiplier': 100}],
                75:  [{'num_dice': 2, 'die_type': 6, 'piece_type': 'gold',     'multiplier': 100},
                      {'num_dice': 1, 'die_type': 6, 'piece_type': 'platinum', 'multiplier': 10}],
                100: [{'num_dice': 2, 'die_type': 6, 'piece_type': 'gold',     'multiplier': 100},
                      {'num_dice': 2, 'die_type': 6, 'piece_type': 'platinum', 'multiplier': 10}]
            },
            MAX_RANK: {
                15:  [{'num_dice': 2, 'die_type': 6, 'piece_type': 'electrum', 'multiplier': 1000},
                      {'num_dice': 8, 'die_type': 6, 'piece_type': 'gold',     'multiplier': 100}],
                55:  [{'num_dice': 1, 'die_type': 6, 'piece_type': 'gold',     'multiplier': 1000},
                      {'num_dice': 1, 'die_type': 6, 'piece_type': 'platinum', 'multiplier': 100}],
                100: [{'num_dice': 1, 'die_type': 6, 'piece_type': 'gold',     'multiplier': 100},
                      {'num_dice': 2, 'die_type': 6, 'piece_type': 'platinum', 'multiplier': 100}]
            }
        },
        'treasure hoard': {
            4: {
                'coins': [
                    {'num_dice': 6, 'die_type': 6, 'piece_type': 'copper', 'multiplier': 100},
                    {'num_dice': 3, 'die_type': 6, 'piece_type': 'silver', 'multiplier': 100},
                    {'num_dice': 2, 'die_type': 6, 'piece_type': 'gold',   'multiplier': 10}
                ],
                'treasure': {
                    6: {
                        'valuable': None,
                        'magic items': []
                    },
                    16: {
                        'valuable': { 'num_dice': 2, 'die_type': 6, 'value': 10, 'valuable_type': 'gem'},
                        'magic items': []
                    },
                    26: {
                        'valuable': { 'num_dice': 2, 'die_type': 4, 'value': 25, 'valuable_type': 'art object'},
                        'magic items': []
                    },
                    36: {
                        'valuable': { 'num_dice': 2, 'die_type': 6, 'value': 50, 'valuable_type': 'gem'},
                        'magic items': []
                    },
                    44: {
                        'valuable': { 'num_dice': 2, 'die_type': 6, 'value': 10, 'valuable_type': 'gem'},
                        'magic items': [{ 'num_dice': 1, 'die_type': 6, 'magic_item_table': 'A' }]
                    },
                    52: {
                        'valuable': { 'num_dice': 2, 'die_type': 4, 'value': 25, 'valuable_type': 'art object'},
                        'magic items': [{ 'num_dice': 1, 'die_type': 6, 'magic_item_table': 'A' }]
                    },
                    60: {
                        'valuable': { 'num_dice': 2, 'die_type': 6, 'value': 50, 'valuable_type': 'gem'},
                        'magic items': [{ 'num_dice': 1, 'die_type': 6, 'magic_item_table': 'A' }]
                    },
                    65: {
                        'valuable': { 'num_dice': 2, 'die_type': 6, 'value': 10, 'valuable_type': 'gem'},
                        'magic items': [{ 'num_dice': 1, 'die_type': 4, 'magic_item_table': 'B' }]
                    },
                    70: {
                        'valuable': { 'num_dice': 2, 'die_type': 4, 'value': 25, 'valuable_type': 'art object'},
                        'magic items': [{ 'num_dice': 1, 'die_type': 4, 'magic_item_table': 'B' }]
                    },
                    75: {
                        'valuable': { 'num_dice': 2, 'die_type': 6, 'value': 50, 'valuable_type': 'gem'},
                        'magic items': [{ 'num_dice': 1, 'die_type': 4, 'magic_item_table': 'B' }]
                    },
                    78: {
                        'valuable': { 'num_dice': 2, 'die_type': 6, 'value': 10, 'valuable_type': 'gem'},
                        'magic items': [{ 'num_dice': 1, 'die_type': 4, 'magic_item_table': 'C' }]
                    },
                    80: {
                        'valuable': { 'num_dice': 2, 'die_type': 4, 'value': 25, 'valuable_type': 'art object'},
                        'magic items': [{ 'num_dice': 1, 'die_type': 4, 'magic_item_table': 'C' }]
                    },
                    85: {
                        'valuable': { 'num_dice': 2, 'die_type': 6, 'value': 50, 'valuable_type': 'gem'},
                        'magic items': [{ 'num_dice': 1, 'die_type': 4, 'magic_item_table': 'C' }]
                    },
                    92: {
                        'valuable': { 'num_dice': 2, 'die_type': 4, 'value': 25, 'valuable_type': 'art object'},
                        'magic items': [{ 'num_dice': 1, 'die_type': 4, 'magic_item_table': 'F' }]
                    },
                    97: {
                        'valuable': { 'num_dice': 2, 'die_type': 6, 'value': 50, 'valuable_type': 'gem'},
                        'magic items': [{ 'num_dice': 1, 'die_type': 4, 'magic_item_table': 'F' }]
                    },
                    99: {
                        'valuable': { 'num_dice': 2, 'die_type': 4, 'value': 25, 'valuable_type': 'art object'},
                        'magic items': [{ 'num_dice': 1, 'die_type': 1, 'magic_item_table': 'G' }]
                    },
                    100: {
                        'valuable': { 'num_dice': 2, 'die_type': 6, 'value': 50, 'valuable_type': 'gem'},
                        'magic items': [{ 'num_dice': 1, 'die_type': 1, 'magic_item_table': 'G' }]
                    }
                }
            },
            10: {
                'coins': [
                    {'num_dice': 2, 'die_type': 6, 'piece_type': 'copper',     'multiplier': 100},
                    {'num_dice': 2, 'die_type': 6, 'piece_type': 'silver',     'multiplier': 1000},
                    {'num_dice': 6, 'die_type': 6, 'piece_type': 'gold',       'multiplier': 100},
                    {'num_dice': 3, 'die_type': 6, 'piece_type': 'platinum',   'multiplier': 10}
                ],
                'treasure': {
                    4: {
                        'valuable': None,
                        'magic items': []
                    },
                    10: {
                        'valuable': { 'num_dice': 2, 'die_type': 4, 'value': 25, 'valuable_type': 'art object'},
                        'magic items': []
                    },
                    16: {
                        'valuable': { 'num_dice': 3, 'die_type': 6, 'value': 50, 'valuable_type': 'gem'},
                        'magic items': []
                    },
                    22: {
                        'valuable': { 'num_dice': 3, 'die_type': 6, 'value': 100, 'valuable_type': 'gem'},
                        'magic items': []
                    },
                    28: {
                        'valuable': { 'num_dice': 2, 'die_type': 4, 'value': 25, 'valuable_type': 'art object'},
                        'magic items': []
                    },
                    32: {
                        'valuable': { 'num_dice': 2, 'die_type': 4, 'value': 25, 'valuable_type': 'art object'},
                        'magic items': [{ 'num_dice': 1, 'die_type': 6, 'magic_item_table': 'A' }]
                    },
                    36: {
                        'valuable': { 'num_dice': 3, 'die_type': 6, 'value': 50, 'valuable_type': 'gem'},
                        'magic items': [{ 'num_dice': 1, 'die_type': 6, 'magic_item_table': 'A' }]
                    },
                    40: {
                        'valuable': { 'num_dice': 3, 'die_type': 6, 'value': 100, 'valuable_type': 'gem'},
                        'magic items': [{ 'num_dice': 1, 'die_type': 6, 'magic_item_table': 'A' }]
                    },
                    44: {
                        'valuable': { 'num_dice': 2, 'die_type': 4, 'value': 250, 'valuable_type': 'art object'},
                        'magic items': [{ 'num_dice': 1, 'die_type': 6, 'magic_item_table': 'A' }]
                    },
                    49: {
                        'valuable': { 'num_dice': 2, 'die_type': 4, 'value': 25, 'valuable_type': 'art object'},
                        'magic items': [{ 'num_dice': 1, 'die_type': 6, 'magic_item_table': 'B' }]
                    },
                    54: {
                        'valuable': { 'num_dice': 3, 'die_type': 6, 'value': 50, 'valuable_type': 'gem'},
                        'magic items': [{ 'num_dice': 1, 'die_type': 4, 'magic_item_table': 'B' }]
                    },
                    59: {
                        'valuable': { 'num_dice': 3, 'die_type': 6, 'value': 100, 'valuable_type': 'gem'},
                        'magic items': [{ 'num_dice': 1, 'die_type': 4, 'magic_item_table': 'B' }]
                    },
                    63: {
                        'valuable': { 'num_dice': 2, 'die_type': 4, 'value': 250, 'valuable_type': 'art object'},
                        'magic items': [{ 'num_dice': 1, 'die_type': 4, 'magic_item_table': 'B' }]
                    },
                    66: {
                        'valuable': { 'num_dice': 2, 'die_type': 4, 'value': 25, 'valuable_type': 'art object'},
                        'magic items': [{ 'num_dice': 1, 'die_type': 4, 'magic_item_table': 'C' }]
                    },
                    69: {
                        'valuable': { 'num_dice': 3, 'die_type': 6, 'value': 50, 'valuable_type': 'gem'},
                        'magic items': [{ 'num_dice': 1, 'die_type': 6, 'magic_item_table': 'C' }]
                    },
                    72: {
                        'valuable': { 'num_dice': 3, 'die_type': 6, 'value': 100, 'valuable_type': 'gem'},
                        'magic items': [{ 'num_dice': 1, 'die_type': 6, 'magic_item_table': 'C' }]
                    },
                    74: {
                        'valuable': { 'num_dice': 2, 'die_type': 4, 'value': 250, 'valuable_type': 'art object'},
                        'magic items': [{ 'num_dice': 1, 'die_type': 6, 'magic_item_table': 'C' }]
                    },
                    76: {
                        'valuable': { 'num_dice': 2, 'die_type': 4, 'value': 25, 'valuable_type': 'art object'},
                        'magic items': [{ 'num_dice': 1, 'die_type': 1, 'magic_item_table': 'D' }]
                    },
                    78: {
                        'valuable': { 'num_dice': 3, 'die_type': 6, 'value': 50, 'valuable_type': 'gem'},
                        'magic items': [{ 'num_dice': 1, 'die_type': 1, 'magic_item_table': 'D' }]
                    },
                    79: {
                        'valuable': { 'num_dice': 3, 'die_type': 6, 'value': 100, 'valuable_type': 'gem'},
                        'magic items': [{ 'num_dice': 1, 'die_type': 1, 'magic_item_table': 'D' }]
                    },
                    80: {
                        'valuable': { 'num_dice': 2, 'die_type': 4, 'value': 250, 'valuable_type': 'art object'},
                        'magic items': [{ 'num_dice': 1, 'die_type': 1, 'magic_item_table': 'D' }]
                    },
                    84: {
                        'valuable': { 'num_dice': 2, 'die_type': 4, 'value': 25, 'valuable_type': 'art object'},
                        'magic items': [{ 'num_dice': 1, 'die_type': 4, 'magic_item_table': 'F' }]
                    },
                    88: {
                        'valuable': { 'num_dice': 3, 'die_type': 6, 'value': 50, 'valuable_type': 'gem'},
                        'magic items': [{ 'num_dice': 1, 'die_type': 4, 'magic_item_table': 'F' }]
                    },
                    91: {
                        'valuable': { 'num_dice': 3, 'die_type': 6, 'value': 100, 'valuable_type': 'gem'},
                        'magic items': [{ 'num_dice': 1, 'die_type': 4, 'magic_item_table': 'F' }]
                    },
                    94: {
                        'valuable': { 'num_dice': 2, 'die_type': 4, 'value': 250, 'valuable_type': 'art object'},
                        'magic items': [{ 'num_dice': 1, 'die_type': 4, 'magic_item_table': 'F' }]
                    },
                    96: {
                        'valuable': { 'num_dice': 3, 'die_type': 6, 'value': 100, 'valuable_type': 'gem'},
                        'magic items': [{ 'num_dice': 1, 'die_type': 4, 'magic_item_table': 'G' }]
                    },
                    98: {
                        'valuable': { 'num_dice': 2, 'die_type': 4, 'value': 250, 'valuable_type': 'art object'},
                        'magic items': [{ 'num_dice': 1, 'die_type': 6, 'magic_item_table': 'G' }]
                    },
                    98: {
                        'valuable': { 'num_dice': 3, 'die_type': 6, 'value': 100, 'valuable_type': 'gem'},
                        'magic items': [{ 'num_dice': 1, 'die_type': 1, 'magic_item_table': 'H' }]
                    },
                    100: {
                        'valuable': { 'num_dice': 2, 'die_type': 4, 'value': 250, 'valuable_type': 'art object'},
                        'magic items': [{ 'num_dice': 1, 'die_type': 1, 'magic_item_table': 'H' }]
                    }
                }
            },
            16: {
                'coins': [
                    {'num_dice': 4, 'die_type': 6, 'piece_type': 'gold',     'multiplier': 1000},
                    {'num_dice': 5, 'die_type': 6, 'piece_type': 'platinum', 'multiplier': 100}
                ],
                'treasure': {
                    3: {
                        'valuable': None,
                        'magic items': []
                    },
                    6: {
                        'valuable': { 'num_dice': 2, 'die_type': 4, 'value': 250, 'valuable_type': 'art object'},
                        'magic items': []
                    },
                    10: {
                        'valuable': { 'num_dice': 2, 'die_type': 4, 'value': 750, 'valuable_type': 'art object'},
                        'magic items': []
                    },
                    12: {
                        'valuable': { 'num_dice': 3, 'die_type': 6, 'value': 500, 'valuable_type': 'gem'},
                        'magic items': []
                    },
                    15: {
                        'valuable': { 'num_dice': 3, 'die_type': 6, 'value': 1000, 'valuable_type': 'gem'},
                        'magic items': []
                    },
                    19: {
                        'valuable': { 'num_dice': 2, 'die_type': 4, 'value': 250, 'valuable_type': 'art object'},
                        'magic items': [
                            { 'num_dice': 1, 'die_type': 4, 'magic_item_table': 'A' },
                            { 'num_dice': 1, 'die_type': 6, 'magic_item_table': 'B' }
                        ]
                    },
                    23: {
                        'valuable': { 'num_dice': 2, 'die_type': 4, 'value': 750, 'valuable_type': 'art object'},
                        'magic items': [
                            { 'num_dice': 1, 'die_type': 4, 'magic_item_table': 'A' },
                            { 'num_dice': 1, 'die_type': 6, 'magic_item_table': 'B' }
                        ]
                    },
                    26: {
                        'valuable': { 'num_dice': 3, 'die_type': 6, 'value': 500, 'valuable_type': 'gem'},
                        'magic items': [
                            { 'num_dice': 1, 'die_type': 4, 'magic_item_table': 'A' },
                            { 'num_dice': 1, 'die_type': 6, 'magic_item_table': 'B' }
                        ]
                    },
                    29: {
                        'valuable': { 'num_dice': 3, 'die_type': 6, 'value': 1000, 'valuable_type': 'gem'},
                        'magic items': [
                            { 'num_dice': 1, 'die_type': 4, 'magic_item_table': 'A' },
                            { 'num_dice': 1, 'die_type': 6, 'magic_item_table': 'B' }
                        ]
                    },
                    35: {
                        'valuable': { 'num_dice': 2, 'die_type': 4, 'value': 250, 'valuable_type': 'art object'},
                        'magic items': [
                            { 'num_dice': 1, 'die_type': 6, 'magic_item_table': 'C' }
                        ]
                    },
                    40: {
                        'valuable': { 'num_dice': 2, 'die_type': 4, 'value': 750, 'valuable_type': 'art object'},
                        'magic items': [
                            { 'num_dice': 1, 'die_type': 6, 'magic_item_table': 'C' }
                        ]
                    },
                    45: {
                        'valuable': { 'num_dice': 3, 'die_type': 6, 'value': 500, 'valuable_type': 'gem'},
                        'magic items': [
                            { 'num_dice': 1, 'die_type': 6, 'magic_item_table': 'C' }
                        ]
                    },
                    50: {
                        'valuable': { 'num_dice': 3, 'die_type': 6, 'value': 1000, 'valuable_type': 'gem'},
                        'magic items': [
                            { 'num_dice': 1, 'die_type': 6, 'magic_item_table': 'C' }
                        ]
                    },
                    54: {
                        'valuable': { 'num_dice': 2, 'die_type': 4, 'value': 250, 'valuable_type': 'art object'},
                        'magic items': [
                            { 'num_dice': 1, 'die_type': 4, 'magic_item_table': 'D' }
                        ]
                    },
                    58: {
                        'valuable': { 'num_dice': 2, 'die_type': 4, 'value': 750, 'valuable_type': 'art object'},
                        'magic items': [
                            { 'num_dice': 1, 'die_type': 4, 'magic_item_table': 'D' }
                        ]
                    },
                    62: {
                        'valuable': { 'num_dice': 3, 'die_type': 6, 'value': 500, 'valuable_type': 'gem'},
                        'magic items': [
                            { 'num_dice': 1, 'die_type': 4, 'magic_item_table': 'D' }
                        ]
                    },
                    66: {
                        'valuable': { 'num_dice': 3, 'die_type': 6, 'value': 1000, 'valuable_type': 'gem'},
                        'magic items': [
                            { 'num_dice': 1, 'die_type': 4, 'magic_item_table': 'D' }
                        ]
                    },
                    68: {
                        'valuable': { 'num_dice': 2, 'die_type': 4, 'value': 250, 'valuable_type': 'art object'},
                        'magic items': [
                            { 'num_dice': 1, 'die_type': 1, 'magic_item_table': 'E' }
                        ]
                    },
                    70: {
                        'valuable': { 'num_dice': 2, 'die_type': 4, 'value': 750, 'valuable_type': 'art object'},
                        'magic items': [
                            { 'num_dice': 1, 'die_type': 1, 'magic_item_table': 'E' }
                        ]
                    },
                    72: {
                        'valuable': { 'num_dice': 3, 'die_type': 6, 'value': 500, 'valuable_type': 'gem'},
                        'magic items': [
                            { 'num_dice': 1, 'die_type': 1, 'magic_item_table': 'E' }
                        ]
                    },
                    74: {
                        'valuable': { 'num_dice': 3, 'die_type': 6, 'value': 1000, 'valuable_type': 'gem'},
                        'magic items': [
                            { 'num_dice': 1, 'die_type': 1, 'magic_item_table': 'E' }
                        ]
                    },
                    76: {
                        'valuable': { 'num_dice': 2, 'die_type': 4, 'value': 250, 'valuable_type': 'art object'},
                        'magic items': [
                            { 'num_dice': 1, 'die_type': 4, 'magic_item_table': 'G' },
                            { 'num_dice': 1, 'die_type': 1, 'magic_item_table': 'F' }
                        ]
                    },
                    78: {
                        'valuable': { 'num_dice': 2, 'die_type': 4, 'value': 750, 'valuable_type': 'art object'},
                        'magic items': [
                            { 'num_dice': 1, 'die_type': 4, 'magic_item_table': 'G' },
                            { 'num_dice': 1, 'die_type': 1, 'magic_item_table': 'F' }
                        ]
                    },
                    80: {
                        'valuable': { 'num_dice': 3, 'die_type': 6, 'value': 500, 'valuable_type': 'gem'},
                        'magic items': [
                            { 'num_dice': 1, 'die_type': 4, 'magic_item_table': 'G' },
                            { 'num_dice': 1, 'die_type': 1, 'magic_item_table': 'F' }
                        ]
                    },
                    82: {
                        'valuable': { 'num_dice': 3, 'die_type': 6, 'value': 1000, 'valuable_type': 'gem'},
                        'magic items': [
                            { 'num_dice': 1, 'die_type': 4, 'magic_item_table': 'G' },
                            { 'num_dice': 1, 'die_type': 1, 'magic_item_table': 'F' }
                        ]
                    },
                    85: {
                        'valuable': { 'num_dice': 2, 'die_type': 4, 'value': 250, 'valuable_type': 'art object'},
                        'magic items': [
                            { 'num_dice': 1, 'die_type': 4, 'magic_item_table': 'H' }
                        ]
                    },
                    88: {
                        'valuable': { 'num_dice': 2, 'die_type': 4, 'value': 750, 'valuable_type': 'art object'},
                        'magic items': [
                            { 'num_dice': 1, 'die_type': 4, 'magic_item_table': 'H' }
                        ]
                    },
                    90: {
                        'valuable': { 'num_dice': 3, 'die_type': 6, 'value': 500, 'valuable_type': 'gem'},
                        'magic items': [
                            { 'num_dice': 1, 'die_type': 4, 'magic_item_table': 'H' }
                        ]
                    },
                    92: {
                        'valuable': { 'num_dice': 3, 'die_type': 6, 'value': 1000, 'valuable_type': 'gem'},
                        'magic items': [
                            { 'num_dice': 1, 'die_type': 4, 'magic_item_table': 'H' }
                        ]
                    },
                    94: {
                        'valuable': { 'num_dice': 2, 'die_type': 4, 'value': 250, 'valuable_type': 'art object'},
                        'magic items': [
                            { 'num_dice': 1, 'die_type': 1, 'magic_item_table': 'I' }
                        ]
                    },
                    96: {
                        'valuable': { 'num_dice': 2, 'die_type': 4, 'value': 750, 'valuable_type': 'art object'},
                        'magic items': [
                            { 'num_dice': 1, 'die_type': 1, 'magic_item_table': 'I' }
                        ]
                    },
                    98: {
                        'valuable': { 'num_dice': 3, 'die_type': 6, 'value': 500, 'valuable_type': 'gem'},
                        'magic items': [
                            { 'num_dice': 1, 'die_type': 1, 'magic_item_table': 'I' }
                        ]
                    },
                    100: {
                        'valuable': { 'num_dice': 3, 'die_type': 6, 'value': 1000, 'valuable_type': 'gem'},
                        'magic items': [
                            { 'num_dice': 1, 'die_type': 1, 'magic_item_table': 'I' }
                        ]
                    }
                }
            },
            MAX_RANK: {
                'coins': [
                    {'num_dice': 12, 'die_type': 6, 'piece_type': 'gold',     'multiplier': 1000},
                    {'num_dice': 8,  'die_type': 6, 'piece_type': 'platinum', 'multiplier': 1000}
                ],
                'treasure': {
                    2: {
                        'valuable': None,
                        'magic items': []
                    },
                    5: {
                        'valuable': { 'num_dice': 3, 'die_type': 6, 'value': 1000, 'valuable_type': 'gem'},
                        'magic items': [
                            { 'num_dice': 1, 'die_type': 8, 'magic_item_table': 'C' }
                        ]
                    },
                    8: {
                        'valuable': { 'num_dice': 1, 'die_type': 10, 'value': 2500, 'valuable_type': 'art object'},
                        'magic items': [
                            { 'num_dice': 1, 'die_type': 8, 'magic_item_table': 'C' }
                        ]
                    },
                    11: {
                        'valuable': { 'num_dice': 1, 'die_type': 4, 'value': 7500, 'valuable_type': 'art object'},
                        'magic items': [
                            { 'num_dice': 1, 'die_type': 8, 'magic_item_table': 'C' }
                        ]
                    },
                    14: {
                        'valuable': { 'num_dice': 1, 'die_type': 8, 'value': 5000, 'valuable_type': 'gem'},
                        'magic items': [
                            { 'num_dice': 1, 'die_type': 8, 'magic_item_table': 'C' }
                        ]
                    },
                    22: {
                        'valuable': { 'num_dice': 3, 'die_type': 6, 'value': 1000, 'valuable_type': 'gem'},
                        'magic items': [
                            { 'num_dice': 1, 'die_type': 6, 'magic_item_table': 'D' }
                        ]
                    },
                    30: {
                        'valuable': { 'num_dice': 1, 'die_type': 10, 'value': 2500, 'valuable_type': 'art object'},
                        'magic items': [
                            { 'num_dice': 1, 'die_type': 6, 'magic_item_table': 'D' }
                        ]
                    },
                    38: {
                        'valuable': { 'num_dice': 1, 'die_type': 4, 'value': 7500, 'valuable_type': 'art object'},
                        'magic items': [
                            { 'num_dice': 1, 'die_type': 6, 'magic_item_table': 'D' }
                        ]
                    },
                    46: {
                        'valuable': { 'num_dice': 1, 'die_type': 8, 'value': 5000, 'valuable_type': 'gem'},
                        'magic items': [
                            { 'num_dice': 1, 'die_type': 6, 'magic_item_table': 'D' }
                        ]
                    },
                    52: {
                        'valuable': { 'num_dice': 3, 'die_type': 6, 'value': 1000, 'valuable_type': 'gem'},
                        'magic items': [
                            { 'num_dice': 1, 'die_type': 6, 'magic_item_table': 'E' }
                        ]
                    },
                    58: {
                        'valuable': { 'num_dice': 1, 'die_type': 10, 'value': 2500, 'valuable_type': 'art object'},
                        'magic items': [
                            { 'num_dice': 1, 'die_type': 6, 'magic_item_table': 'E' }
                        ]
                    },
                    63: {
                        'valuable': { 'num_dice': 1, 'die_type': 4, 'value': 7500, 'valuable_type': 'art object'},
                        'magic items': [
                            { 'num_dice': 1, 'die_type': 6, 'magic_item_table': 'E' }
                        ]
                    },
                    68: {
                        'valuable': { 'num_dice': 1, 'die_type': 8, 'value': 5000, 'valuable_type': 'gem'},
                        'magic items': [
                            { 'num_dice': 1, 'die_type': 6, 'magic_item_table': 'E' }
                        ]
                    },
                    69: {
                        'valuable': { 'num_dice': 3, 'die_type': 6, 'value': 1000, 'valuable_type': 'gem'},
                        'magic items': [
                            { 'num_dice': 1, 'die_type': 4, 'magic_item_table': 'G' }
                        ]
                    },
                    70: {
                        'valuable': { 'num_dice': 1, 'die_type': 10, 'value': 2500, 'valuable_type': 'art object'},
                        'magic items': [
                            { 'num_dice': 1, 'die_type': 4, 'magic_item_table': 'G' }
                        ]
                    },
                    71: {
                        'valuable': { 'num_dice': 1, 'die_type': 4, 'value': 7500, 'valuable_type': 'art object'},
                        'magic items': [
                            { 'num_dice': 1, 'die_type': 4, 'magic_item_table': 'G' }
                        ]
                    },
                    72: {
                        'valuable': { 'num_dice': 1, 'die_type': 8, 'value': 5000, 'valuable_type': 'gem'},
                        'magic items': [
                            { 'num_dice': 1, 'die_type': 4, 'magic_item_table': 'G' }
                        ]
                    },
                    74: {
                        'valuable': { 'num_dice': 3, 'die_type': 6, 'value': 1000, 'valuable_type': 'gem'},
                        'magic items': [
                            { 'num_dice': 1, 'die_type': 4, 'magic_item_table': 'H' }
                        ]
                    },
                    76: {
                        'valuable': { 'num_dice': 1, 'die_type': 10, 'value': 2500, 'valuable_type': 'art object'},
                        'magic items': [
                            { 'num_dice': 1, 'die_type': 4, 'magic_item_table': 'H' }
                        ]
                    },
                    78: {
                        'valuable': { 'num_dice': 1, 'die_type': 4, 'value': 7500, 'valuable_type': 'art object'},
                        'magic items': [
                            { 'num_dice': 1, 'die_type': 4, 'magic_item_table': 'H' }
                        ]
                    },
                    80: {
                        'valuable': { 'num_dice': 1, 'die_type': 8, 'value': 5000, 'valuable_type': 'gem'},
                        'magic items': [
                            { 'num_dice': 1, 'die_type': 4, 'magic_item_table': 'H' }
                        ]
                    },
                    85: {
                        'valuable': { 'num_dice': 3, 'die_type': 6, 'value': 1000, 'valuable_type': 'gem'},
                        'magic items': [
                            { 'num_dice': 1, 'die_type': 4, 'magic_item_table': 'I' }
                        ]
                    },
                    90: {
                        'valuable': { 'num_dice': 1, 'die_type': 10, 'value': 2500, 'valuable_type': 'art object'},
                        'magic items': [
                            { 'num_dice': 1, 'die_type': 4, 'magic_item_table': 'I' }
                        ]
                    },
                    95: {
                        'valuable': { 'num_dice': 1, 'die_type': 4, 'value': 7500, 'valuable_type': 'art object'},
                        'magic items': [
                            { 'num_dice': 1, 'die_type': 1, 'magic_item_table': 'F' },
                            { 'num_dice': 1, 'die_type': 4, 'magic_item_table': 'G' }
                        ]
                    },
                    100: {
                        'valuable': { 'num_dice': 1, 'die_type': 8, 'value': 5000, 'valuable_type': 'gem'},
                        'magic items': [
                            { 'num_dice': 1, 'die_type': 4, 'magic_item_table': 'I' }
                        ]
                    },
                }
            }
        },
        'gems': {
            10: [
                'Azurite (opaque mottled deep blue)', 
                'Banded agate (translucent striped brown, blue, white, or red)', 
                'Blue quartz (transparent pale blue)', 
                'Eye agate (translucent circles of gray, white, brown, blue, or green)', 
                'Hematite (opaque gray-black)', 
                'Lapis lazuli (opaque light and dark blue with yellow flecks)', 
                'Malachite (opaque striated light and dark green)', 
                'Moss agate (translucent pink or yellow-white with mossy gray or green markings)', 
                'Obsidian (opaque black)', 
                'Rhodochrosite (opaque light pink)', 
                'Tiger eye (translucent brown with golden center)', 
                'Turquoise (opaque light blue-green)'
            ],
            50: [
                'Bloodstone (opaque dark gray with red flecks)',
                'Carnelian (opaque orange to red-brown)',
                'Chalcedony (opaque white)',
                'Chrysoprase (translucent green)',
                'Citrine (transparent pale yellow-brown)',
                'Jasper (opaque blue, black, or brown)',
                'Moonstone (translucent white with pale blue glow)',
                'Onyx (opaque bands of black and white, or pure black or white)',
                'Quartz (transparent white, smoky gray, or yellow)',
                'Sardonyx (opaque bands of red and white)',
                'Star rose quartz (translucent rosy stone with white star-shaped center)',
                'Zircon (transparent pale blue-green)'
            ],
            500: [
                'Alexandrite (transparent dark green)',
                'Aquamarine (transparent pale blue-green)',
                'Black pearl (opaque pure black)',
                'Blue spinel (transparent deep blue)',
                'Peridot (transparent rich olive green)',
                'Topaz (transparent golden yellow)',
                'Topaz (transparent golden yellow)'
            ],
            1000: [
                'Black opal (translucent dark green with black mottling and golden flecks)',
                'Blue sapphire (transparent blue-white to medium blue)',
                'Emerald (transparent deep bright green)',
                'Fire opal (translucent fiery red)',
                'Opal (translucent pale blue with green and golden mottling)',
                'Star ruby (translucent ruby with white star-shaped center)',
                'Star sapphire (translucent blue sapphire with white star-shaped center)',
                'Yellow sapphire (transparent fiery yellow or yellow green)'
            ],
            5000: [
                'Black sapphire (translucent lustrous black with glowing highlights)',
                'Diamond (transparent blue-white, canary, pink, brown, or blue)',
                'Jacinth (transparent fiery orange)',
                'Ruby (transparent clear red to deep crimson)'
            ]
        },
        'art objects': {
            25: [
                'Silver ewer',
                'Carved bone statuette',
                'Small gold bracelet',
                'Cloth-of-gold vestments',
                'Black velvet mask stitched with silver thread',
                'Copper chalice with silver filigree',
                'Pair of engraved bone dice',
                'Small mirror set in a painted wooden frame',
                'Embroidered silk handkerchief',
                'Gold locket with a painted portrait inside'
            ],
            250: [
                'Gold ring set with bloodstones',
                'Carved ivory statuette',
                'Large gold bracelet',
                'Silver necklace with a gemstone pendant',
                'Bronze crown',
                'Silk robe with gold embroidery',
                'Large well-made tapestry',
                'Brass mug with jade inlay',
                'Box of turquoise animal figurines',
                'Gold bird cage with electrum filigree'
            ],
            750: [
                'Silver chalice set with moonstones',
                'Silver-plated steellongsword with jet set in hilt',
                'Carved harp of exotic wood with ivory inlay and zircon gems',
                'Small gold idol',
                'Gold dragon comb set with red garnets as eyes',
                'Bottle stopper cork embossed with gold leaf and set with amethysts',
                'Ceremonial electrum dagger with a black pearl in the pommel',
                'Silver and gold brooch',
                'Obsidian statuette with gold fittings and inlay',
                'Painted gold war mask'
            ],
            2500: [
                'Fine gold chain set with a fire opal',
                'Old masterpiece painting',
                'Embroidered silk and velvet mantle set with numerous moonstones',
                'Platinum bracelet set with a sapphire',
                'Embroidered glove set with jewel chips',
                'Jeweled anklet',
                'Gold music box',
                'Gold circlet set with four aquamarines',
                'Eye patch with a mock eye set in blue sapphire andmoonstone',
                'A necklace string of small pink pearls'
            ],
            7500: [
                'Jeweled gold crown',
                'Jeweled platinum ring',
                'Small gold statuette set with rubies',
                'Gold cup set with emeralds',
                'Gold jewelry box with platinum filigree',
                'Painted gold child\'s sarcophagus',
                'Jade game board with solid gold playing pieces',
                'Bejeweled ivory drinking horn with gold filigree'
            ]
        }
    }
    json.dump(data, f, indent=4, sort_keys=True)
    print('\tSeeded loot')