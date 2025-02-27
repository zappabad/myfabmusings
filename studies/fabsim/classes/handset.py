from typing import Callable, Set, Tuple, List, Dict
import pandas as pd
from itertools import chain, combinations, product
from collections import Counter

from .card import Card
from .hand import Hand

from tqdm import tqdm


class HandSet:
    def __init__(self, hand_list):
        self.hands = set(hand_list)
        self.prev_handset_size = 0
        
    def aggregate(self, test_functions: List[Callable[[Hand], bool]]) -> Dict[int, Set[Hand]]:
        """
        Aggregates the hands in the handset based on a list of test functions.

        Each test function takes a Hand as an argument and returns a boolean.

        Args:
            test_functions (List[Callable[[Hand], bool]]): A list of test functions.

        Returns:
            Dict[int, Set[Hand]]: A dictionary where each key is an index of the test function,
            and its value is a set of hands that pass this test.
        """
        results = {i: set() for i in range(len(test_functions))}
        for hand in self.hands:
            for i, test_func in enumerate(test_functions):
                if test_func(hand):
                    results[i].add(hand)
        return results

    def difference(self, other_handset: 'HandSet') -> 'HandSet':
        """
        Compares this HandSet to another HandSet and returns a new HandSet containing
        hands that are in this HandSet but not in the other.

        Args:
            other_handset (HandSet): Another HandSet object to compare with.

        Returns:
            HandSet: A new HandSet containing hands unique to this HandSet.
        """
        set_self = set(self.hands)
        set_other = set(other_handset.hands)
        unique_hands = set_self - set_other
        return HandSet(list(unique_hands))

    def intersection(self, other_handset: 'HandSet') -> 'HandSet':
        """
        Compares this HandSet to another HandSet and returns a new HandSet containing
        hands that are in both HandSets.

        Args:
            other_handset (HandSet): Another HandSet object to compare with.

        Returns:
            HandSet: A new HandSet containing hands in both HandSets.
        """
        set_self = set(self.hands)
        set_other = set(other_handset.hands)
        unique_hands = set_self.intersection(set_other)
        return HandSet(list(unique_hands))
    

    def compare_size_to(self, other_handset: 'HandSet') -> float:
            """
            Calculates the percentage of this HandSet's total hand count relative to another HandSet.

            Args:
                other_handset (HandSet): Another HandSet object to compare with.

            Returns:
                float: The percentage of this HandSet's total count relative to the other HandSet.
            """
            total_count_self = sum(hand.count for hand in self.hands)
            total_count_other = sum(hand.count for hand in other_handset.hands)

            if total_count_other == 0:
                return 0.0  # Avoid division by zero

            return (total_count_self / total_count_other)
    
    def filter(self, condition_method_name: str, *args, **kwargs) -> 'HandSet':
        """
        Filters hands based on a provided condition function.

        Args:
            condition_function (Callable[[Hand], bool]): A function that takes a Hand object
                and returns True if the condition is met, False otherwise.

        Returns:
            HandSet: A new HandSet object containing hands that meet the condition.
        """
        filtered_hands = [hand for hand in self.hands if getattr(hand, condition_method_name)(*args, **kwargs)]
        return HandSet(filtered_hands)


    def find_hands_with_card_combinations(self, card_tuples_list: List[Tuple[Card]]) -> Tuple['HandSet', 'HandSet']:
        """
        [Refactored Method]
        Finds hands that contain all cards in any of the given tuples and returns two HandSets.
        """
        matching_handset = self.filter('_contains_cards_in_any_tuple', card_tuples_list)
        non_matching_handset = self.filter(lambda hand: not self._contains_cards_in_any_tuple(hand, card_tuples_list))
        return matching_handset, non_matching_handset

    def filter_with_custom_condition(self, condition_function, *args, **kwargs) -> 'HandSet':
        """
        Filters hands based on a provided custom condition function.
        """
        filtered_hands = [hand for hand in self.hands if condition_function(hand, *args, **kwargs)]
        return HandSet(filtered_hands)
    
    @staticmethod
    def _contains_cards_in_any_tuple(hand, card_tuples_list):
        """
        Helper function to check if a hand contains all cards in any of the tuples.
        """
        hand_count = Counter(hand)
        hand_length = len(hand)

        # Filter out tuples that are longer than the hand
        filtered_tuples = [t for t in card_tuples_list if len(t) <= hand_length]

        return any(all(hand_count[card] >= card_tuple.count(card) for card in card_tuple) for card_tuple in filtered_tuples)



    def power_set(self, iterable):
        """
        Create a power set of the given iterable.
        """
        s = list(iterable)
        return chain.from_iterable(combinations(s, r) for r in range(1, len(s)+1))

    def filter_handset_by_conditions(self, card_groups, condition_status):
        """
        Filters the handset based on a set of conditions.
        """
        filtered_hands = self.hands

        for condition, status in condition_status:
            card_list = card_groups[condition]
            if status:
                # Filter hands that pass the condition
                filtered_hands = [hand for hand in filtered_hands if self._contains_cards_in_any_tuple(hand, card_list)]
            elif not status:  # status == False
                # Filter hands that fail the condition
                filtered_hands = [hand for hand in filtered_hands if not self._contains_cards_in_any_tuple(hand, card_list)]
            else:
                raise ValueError("Invalid status value")

            # Check if filtered_hands is empty
            if not filtered_hands:
                # Return an empty HandSet immediately
                return HandSet(filtered_hands)

        return HandSet(filtered_hands)
    
    def analyze_card_list_combinations(self, card_groups: dict) -> pd.DataFrame:
        """
        Analyzes hands based on an arbitrary number of card groups, providing counts, hand counts, and percentages.
        """
        # Number of conditions
        num_conditions = len(card_groups)
        if num_conditions < 1:
            raise ValueError("At least one condition is required.")

        # Extract condition names
        condition_names = card_groups.keys()

        # Initialize DataFrame columns
        columns = list(condition_names) + ['Hand Counts', 'Combinations', 'Percentage', 'Hands']
        results = pd.DataFrame(columns=columns)

        # Generate all combinations of 'Pass' (True) and 'Fail' (False) for each condition
        status_combinations = product([True, False], repeat=num_conditions)

        for status_combination in tqdm(status_combinations):
            # Pair each condition with its corresponding status
            conditions_with_status = zip(condition_names, status_combination)

            # Filter handset based on conditions
            filtered_handset = self.filter_handset_by_conditions(card_groups, conditions_with_status)

            hands = filtered_handset
            hand_count = len(filtered_handset)
            total_combinations = sum(hand.count for hand in filtered_handset)
            percentage = hand_count / len(self)

            # Prepare new row
            row_data = dict(zip(columns, list(status_combination) + [hand_count, total_combinations, percentage, hands]))
            new_row = pd.DataFrame([row_data])

            # Add new row to DataFrame
            results = pd.concat([results, new_row], ignore_index=True)
            results = results[results["Hand Counts"] > 0].sort_values(by="Percentage", ascending=False)
        return results



    def __iter__(self):
        return iter(self.hands)

    def __getitem__(self, key):
        return self.hands[key]
    
    def __str__(self) -> str:
        return f"Handset object with {len(self.hands)} distinct hands, and {sum([hand.count for hand in self.hands])} hand combinations."
    
    def __repr__(self) -> str:
        return f"Handset object with {len(self.hands)} distinct hands, and {sum([hand.count for hand in self.hands])} hand combinations."
    
    def __len__(self) -> int:
        return len(self.hands)