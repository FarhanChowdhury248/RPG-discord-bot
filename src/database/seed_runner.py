import os

PATH_TO_SEEDS = os.path.join(os.path.dirname(__file__), 'seeds')

def get_seed_files():
    return os.listdir(PATH_TO_SEEDS)

for f in get_seed_files():
    exec(open(os.path.join(PATH_TO_SEEDS, f)).read())