

from collections.abc import Iterable as ABCIterable
from .card import Card

from collections import Counter
from typing import Any, Callable, List, Tuple, Iterable, Union



class Hand:
    def __init__(self, hand_cards_tuple: tuple, arsenal_card: Card, count: int):
        self.hand = hand_cards_tuple
        self.arsenal = arsenal_card
        self.count = count
    
    def __iter__(self):
        return iter(self.hand)
    
    def has_arsenal(self) -> bool:
        return self.arsenal is not None
    
    def arsenal_is(self, cards) -> bool:
        if not isinstance(cards, ABCIterable):
            cards = [cards]
        return self.arsenal in cards
    
    def has_n_cards(self, n: int) -> bool:
        return len(self.hand) == n
    
    def evaluate(self, test: Callable[[Tuple[Card, ...]], bool]) -> bool:
        """
        Applies a boolean test to the hand.

        Args:
            test (Callable[[Tuple[Card, ...]], bool]): A function that takes a tuple of Cards and returns a boolean.

        Returns:
            bool: The result of the test.
        """
        return test(self)
    
    
    def hand_has_cards(self, cards, condition: Union[Callable[[Iterable], bool], None] = None) -> bool:
        """
        Checks if the hand contains cards based on a specified condition (e.g., any, all),
        or checks for any match if a single card is passed.

        Args:
            cards: A single card or an iterable of cards to check against the hand.
            condition (Union[Callable[[Iterable], bool], None]): A function that takes an iterable and returns a boolean
                (e.g., any, all). Defaults to None, which implies 'any' for single card inputs.

        Returns:
            bool: The result of applying the condition function to the presence checks of the specified cards.
        """
        if not isinstance(cards, ABCIterable):
            # Single card is passed, default to using 'any'
            return any(card in self.hand for card in [cards])
        
        if condition is None:
            raise ValueError("A condition function must be provided for iterable inputs.")

        return condition(card in self.hand for card in cards)


    def hand_lacks_cards(self, cards, condition: Union[Callable[[Iterable], bool], None] = None) -> bool:
        """
        Checks if the hand does not contain any of the specified cards.

        Args:
            cards: A single card or an iterable of cards to check against the hand.
            condition (Union[Callable[[Iterable], bool], None]): A function that takes an iterable and returns a boolean
                (e.g., any, all). For this method, it should be used to confirm the absence of all specified cards.

        Returns:
            bool: The result of applying the condition function to the absence checks of the specified cards.
        """
        if not isinstance(cards, ABCIterable):
            # Single card is passed
            return all(card not in self.hand for card in [cards])
        
        if condition is None:
            # If no condition is provided, check that none of the cards are in the hand
            return all(card not in self.hand for card in cards)

        # Apply the provided condition to check for the absence of cards
        return condition(card not in self.hand for card in cards)
    
    def __eq__(self, other):
        """Check if two Hand objects are equal based on their attributes."""
        if not isinstance(other, Hand):
            return False
        return sorted(self.hand, key=lambda card: card.unique_id) == sorted(other.hand, key=lambda card: card.unique_id) and self.arsenal == other.arsenal

    def __hash__(self):
        """Return the hash value of a Hand object."""
        return hash((self.hand, self.arsenal, self.count))

    def __getitem__(self, key):
        return self.hand[key]
    
    def __len__(self) -> int:
        return len(self.hand)
    
    def __str__(self) -> str:
        return f"[{self.count}] Hand: {self.hand}; Arsenal: {self.arsenal}"
    
    def __repr__(self) -> str:
        return f"[{self.count}] Hand: {self.hand}; Arsenal: {self.arsenal}"