class Card:
    def __init__(self, card_info):
        # Assigning basic card properties
        self.unique_id = card_info["unique_id"]
        self.name = card_info["name"]
        # Try converting to integer, assign 0 if it fails
        converted_pitch = str(card_info["pitch"]).replace("X", "").replace("*","")
        try:
            self.pitch = int(converted_pitch) if converted_pitch != "" else 0
        except ValueError:
            self.pitch = 0

        # Similarly for other properties
        converted_cost = str(card_info["cost"]).replace("X", "").replace("*","")
        try:
            self.cost = int(converted_cost) if converted_cost != "" else 0
        except ValueError:
            self.cost = 0

        converted_power = str(card_info["power"]).replace("X", "").replace("*","")
        try:
            self.power = int(converted_power) if converted_power != "" else 0
        except ValueError:
            self.power = 0

        converted_defense = str(card_info["defense"]).replace("X", "").replace("*","")
        try:
            self.defense = int(converted_defense) if converted_defense != "" else 0
        except ValueError:
            self.defense = 0
        self.health = card_info["health"]
        self.intelligence = card_info["intelligence"]
        self.types = card_info["types"]
        self.card_keywords = card_info["card_keywords"]
        self.abilities_and_effects = card_info["abilities_and_effects"]
        self.ability_and_effect_keywords = card_info["ability_and_effect_keywords"]
        self.granted_keywords = card_info["granted_keywords"]
        self.removed_keywords = card_info["removed_keywords"]
        self.interacts_with_keywords = card_info["interacts_with_keywords"]
        self.functional_text = card_info["functional_text"]
        self.functional_text_plain = card_info["functional_text_plain"]
        self.type_text = card_info["type_text"]
        self.played_horizontally = card_info["played_horizontally"]
        self.blitz_legal = card_info["blitz_legal"]
        self.cc_legal = card_info["cc_legal"]
        self.commoner_legal = card_info["commoner_legal"]
        self.blitz_living_legend = card_info["blitz_living_legend"]
        self.cc_living_legend = card_info["cc_living_legend"]
        self.blitz_banned = card_info["blitz_banned"]
        self.cc_banned = card_info["cc_banned"]
        self.commoner_banned = card_info["commoner_banned"]
        self.upf_banned = card_info["upf_banned"]
        self.blitz_suspended = card_info["blitz_suspended"]
        self.cc_suspended = card_info["cc_suspended"]
        self.commoner_suspended = card_info["commoner_suspended"]
        self.ll_restricted = card_info["ll_restricted"]

        # Handling True/False conditions about card properties in objects.
        self.properties = CardProperties(card_info["functional_text_plain"])

        # Handling printings as a list of dictionaries
        self.printings = [Printing(p) for p in card_info["printings"]]

    def __str__(self):
        return f"{self.name} ({self.pitch})"
        
    def __repr__(self):
        return f"{self.name} ({self.pitch})"
    
class CardProperties:
    def __init__(self, functional_text_plain):
        self.has_boost = "Boost" in functional_text_plain
        self.has_go_again = "Go again" in functional_text_plain.split("\n")

    def __repr__(self):
        properties_dict = {prop: getattr(self, prop) for prop in vars(self)}
        return f"{properties_dict}"

    def __str__(self):
        properties_dict = {prop: getattr(self, prop) for prop in vars(self)}
        return f"{properties_dict}"



class Printing:
    def __init__(self, printing_info):
        self.unique_id = printing_info["unique_id"]
        self.set_printing_unique_id = printing_info["set_printing_unique_id"]
        self.id = printing_info["id"]
        self.set_id = printing_info["set_id"]
        self.edition = printing_info["edition"]
        self.foiling = printing_info["foiling"]
        self.rarity = printing_info["rarity"]
        self.artist = printing_info["artist"]
        self.art_variation = printing_info["art_variation"]
        self.flavor_text = printing_info["flavor_text"]
        self.flavor_text_plain = printing_info["flavor_text_plain"]
        self.image_url = printing_info["image_url"]