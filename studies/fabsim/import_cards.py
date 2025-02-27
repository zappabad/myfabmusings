import os
import django
import requests
from collections import Counter
from myapp.models import Card, Printing, CardProperties

# Set up Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")
django.setup()

# URL for card data
CARD_DATA_URL = "https://raw.githubusercontent.com/the-fab-cube/flesh-and-blood-cards/develop/json/english/card.json"

def import_cards():
    # Fetch card data
    response = requests.get(CARD_DATA_URL)
    if response.status_code != 200:
        print("Failed to fetch card data")
        return

    card_data = response.json()
    print("Successfully fetched card data")

    # Process each card
    for card_info in card_data:
        # Create or get CardProperties
        properties_data = card_info.pop("properties", {})
        properties_obj, _ = CardProperties.objects.get_or_create(
            has_boost=properties_data.get("has_boost", False),
            has_go_again=properties_data.get("has_go_again", False)
        )

        # Create or get Card
        card_obj, created = Card.objects.update_or_create(
            unique_id=card_info["unique_id"],
            defaults={
                "name": card_info["name"],
                "pitch": card_info.get("pitch", 0),
                "cost": card_info.get("cost", 0),
                "power": card_info.get("power", 0),
                "defense": card_info.get("defense", 0),
                "health": card_info.get("health", 0),
                "intelligence": card_info.get("intelligence", 0),
                "types": card_info.get("types", []),
                "card_keywords": card_info.get("card_keywords", []),
                "abilities_and_effects": card_info.get("abilities_and_effects", []),
                "ability_and_effect_keywords": card_info.get("ability_and_effect_keywords", []),
                "granted_keywords": card_info.get("granted_keywords", []),
                "removed_keywords": card_info.get("removed_keywords", []),
                "interacts_with_keywords": card_info.get("interacts_with_keywords", []),
                "functional_text": card_info.get("functional_text", ""),
                "functional_text_plain": card_info.get("functional_text_plain", ""),
                "type_text": card_info.get("type_text", ""),
                "played_horizontally": card_info.get("played_horizontally", False),
                "blitz_legal": card_info.get("blitz_legal", False),
                "cc_legal": card_info.get("cc_legal", False),
                "commoner_legal": card_info.get("commoner_legal", False),
                "blitz_living_legend": card_info.get("blitz_living_legend", False),
                "cc_living_legend": card_info.get("cc_living_legend", False),
                "blitz_banned": card_info.get("blitz_banned", False),
                "cc_banned": card_info.get("cc_banned", False),
                "commoner_banned": card_info.get("commoner_banned", False),
                "upf_banned": card_info.get("upf_banned", False),
                "blitz_suspended": card_info.get("blitz_suspended", False),
                "cc_suspended": card_info.get("cc_suspended", False),
                "commoner_suspended": card_info.get("commoner_suspended", False),
                "ll_restricted": card_info.get("ll_restricted", False),
                "properties": properties_obj
            }
        )

        # Process each printing for the card
        printings_data = card_info.get("printings", [])
        for printing_data in printings_data:
            printing_obj, _ = Printing.objects.get_or_create(
                unique_id=printing_data["unique_id"],
                defaults={
                    "set_printing_unique_id": printing_data.get("set_printing_unique_id", ""),
                    "id": printing_data.get("id", ""),
                    "set_id": printing_data.get("set_id", ""),
                    "edition": printing_data.get("edition", ""),
                    "foiling": printing_data.get("foiling", ""),
                    "rarity": printing_data.get("rarity", ""),
                    "artist": printing_data.get("artist"),
                    "art_variation": printing_data.get("art_variation"),
                    "flavor_text": printing_data.get("flavor_text", ""),
                    "flavor_text_plain": printing_data.get("flavor_text_plain", ""),
                    "image_url": printing_data.get("image_url"),
                }
            )
            # Associate printing with the card
            card_obj.printings.add(printing_obj)

        if created:
            print(f"Added card: {card_obj.name}")
        else:
            print(f"Updated card: {card_obj.name}")

if __name__ == "__main__":
    import_cards()