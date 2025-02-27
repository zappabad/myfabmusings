from typing import List, Tuple, Optional
from itertools import product
from collections import Counter

from classes.card import Card
from classes.hand import Hand
from classes.handset import HandSet
from classes.deck import Deck

from math import factorial

def generate_handsets(deck: Deck, card_options_tuple: Tuple[List[Card], ...], arsenal_options: Optional[List[Card]] = None) -> Tuple[HandSet, int]:
    """
    Optimized generation of handsets from a deck, considering sorted hand combinations and arsenal options.

    Args:
        deck (Deck): The deck to generate hands from.
        card_options_tuple (Tuple[List[Card], ...]): Options for each card slot in the hand.
        arsenal_options (Optional[List[Card]]): Options for the arsenal card.

    Returns:
        Tuple[HandSet, int]: Generated handsets and total number of combinations.
    """

    deck_counter = Counter(deck.cards)
    hand_counts = Counter()

    # Generate all possible hand combinations, including overcounted ones
    for raw_hand_combination in product(*card_options_tuple):
        sorted_hand_combination = tuple(sorted(raw_hand_combination, key=lambda card: card.unique_id))
        
        # Consider each arsenal card option
        if arsenal_options is not None:
            for arsenal_card in arsenal_options:
                if deck_counter[arsenal_card] > 0:  # Only consider available arsenal cards
                    hand_key = (sorted_hand_combination, arsenal_card)
                    hand_counts[hand_key] += 1
        else:
            # No arsenal card
            hand_key = (sorted_hand_combination, None)
            hand_counts[hand_key] += 1

    # Prune invalid hands that exceed the available card counts
    valid_hand_counts = Counter()
    for hand, count in hand_counts.items():
        combination_counter = Counter(hand[0])
        if hand[1] is not None:  # Consider the arsenal card
            combination_counter[hand[1]] += 1

        if all(deck_counter[card] >= count for card, count in combination_counter.items()):
            valid_hand_counts[hand] = calculate_hand_permutations(deck_counter, hand[0], hand[1])


    # Convert to HandSet
    hands_list = [Hand(hand[0], hand[1], valid_hand_counts[hand]) for hand in valid_hand_counts]

    return HandSet(hands_list)

from collections import Counter
from typing import Tuple, Optional


def calculate_hand_permutations(deck_counter: Counter, hand_cards: Tuple[Card, ...], arsenal_card: Optional[Card]) -> int:
    """
    Calculate the number of distinct combinations of a given hand from the deck, considering that order does not matter.

    Args:
        deck_counter (Counter): A counter of cards in the deck.
        hand_cards (Tuple[Card, ...]): The cards in the hand.
        arsenal_card (Optional[Card]): The arsenal card, if any.

    Returns:
        int: The number of distinct combinations of the hand from the deck.
    """
    if arsenal_card:
        hand_cards += (arsenal_card,)

    # Calculate permutations considering order, then divide by factorial of counts to get combinations
    permutations = 1
    hand_counter = Counter(hand_cards)
    for card, hand_count in hand_counter.items():
        deck_count = deck_counter[card]
        for i in range(hand_count):
            permutations *= deck_count - i
        permutations //= factorial(hand_count)  # Divide by the factorial of the count of each card

    return permutations