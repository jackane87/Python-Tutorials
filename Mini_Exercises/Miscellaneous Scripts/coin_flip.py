from random import random

def coin_flip():
    if random() > 0.5:
        return "Heads"
    else:
        return "Tails"
    
print(coin_flip())