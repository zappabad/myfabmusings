import itertools
import numpy as np
from tqdm import tqdm
from collections import Counter

from .hand import Hand
from .handset import HandSet

class Deck:
    def __init__(self, deck_string, card_database):
        self.cards = []
        self.parse_deck_string(deck_string, card_database)

    def group_by(self, condition):
        """
        Groups cards based on the provided condition.
        condition: a lambda function that returns a boolean.
        """
        grouped_cards = [card for card in self.cards if condition(card)]
        return grouped_cards

    def parse_deck_string(self, deck_string, card_database):
        lines = deck_string.split('\n')
        for line in lines:
            if '(' in line and ')' in line:
                quantity, rest = line.split(')', 1)
                quantity = int(quantity.strip('('))
                name, pitch_color = rest.rsplit(' ', 1)
                name = name.strip()
                pitch = self.color_to_pitch(pitch_color)

                card = self.find_card_in_database(card_database, name, pitch)
                if card:
                    for _ in range(quantity):
                        self.cards.append(card)

    @staticmethod
    def color_to_pitch(color):
        return {'(red)': 1, '(yellow)': 2, '(blue)': 3}.get(color, '')

    @staticmethod
    def find_card_in_database(card_database, name, pitch):
        # Assuming card_database is a list of Card objects
        for card in card_database:
            if card.name == name and card.pitch == pitch:
                return card
        return None
    

    def calculate_hands(self):
        hand_counts = Counter()
        deck_counts = Counter(self.cards)

        # Generate combinations for hand sizes 1, 2, 3, and 4
        for hand_size in range(0, 5):
            print(f"Calculating permutations for hand size {hand_size}")
            total_combinations = itertools.combinations(self.cards, hand_size)

            for combination in tqdm(total_combinations):
                # Count occurrences of each card in the combination
                combination_counts = Counter(combination)
                sorted_combination = tuple(sorted(combination, key=lambda card: card.unique_id))

                # Count the hand without any arsenal card
                hand_counts[(sorted_combination, None)] += 1

                # Append each possible arsenal card to the sorted combination
                for arsenal_card in self.cards:
                    if deck_counts[arsenal_card] > combination_counts[arsenal_card]:
                        full_hand = (sorted_combination, arsenal_card)
                        hand_counts[full_hand] += 1

        # Create a list to store the hands and their counts
        hands_list = []

        # Fill the list with hands and their counts
        for hand, count in hand_counts.items():
            hand_obj = Hand(hand[0], hand[1], count)
            hands_list.append((hand_obj))  # Appending the count to the hand tuple

        
        return HandSet(hands_list)

    def __str__(self):
        return f"Deck with {len(self.cards)} cards"
    
    def __repr__(self):
        return f"Deck with {len(self.cards)} cards"