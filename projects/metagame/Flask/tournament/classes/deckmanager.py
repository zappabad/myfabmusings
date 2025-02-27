import numpy as np
import pandas as pd
from threading import Lock
from uuid import uuid4


class Match:
    def __init__(self, win_prob_1, win_prob_2):
        self.win_prob_p1 = win_prob_1
        self.win_prob_p2 = win_prob_2
        self.result = self.random_generator
    
    def random_generator():
        return np.random(0, 1)
        
        
        
class Player:
    def __init__(self, player_id, alias, player_skill=0):
        self.id = str(uuid4())
        self.alias = alias
        self.skill = player_skill