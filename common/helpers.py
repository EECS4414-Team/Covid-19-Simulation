import random

def random_name(name_length :int=10):
    letters = list('abcdefghijklmnopqrstuvwxyz')
    return ''.join([random.choice(letters) for _ in range(name_length)])
