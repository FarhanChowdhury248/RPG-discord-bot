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
        }
    }
    json.dump(data, f, indent=4, sort_keys=True)
    print('\tSeeded loot')