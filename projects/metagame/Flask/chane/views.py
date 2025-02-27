from flask import Flask, jsonify, request, render_template
import random
from . import chane_bp

# Example deck with N cards
deck = list(range(1, 61))  # A deck of 60 cards for example
banished = []
hand = []
arsenal = []
soul_shackles = 0
pitched = []

@chane_bp.route('/draw_card', methods=['POST'])
def draw_card():
    global deck, hand
    if len(hand) < 4 and deck:
        card = deck.pop(0)
        hand.append(card)
        return jsonify({"card": card, "deck_count": len(deck)})
    return jsonify({"error": "Cannot draw more cards"}), 400

@chane_bp.route('/pluck_card', methods=['POST'])
def pluck_card():
    global deck, hand
    card_id = request.json.get('card_id')
    if card_id in deck:
        deck.remove(card_id)
        hand.append(card_id)
    return jsonify({"deck_count": len(deck), "hand": hand})

@chane_bp.route('/banish_card', methods=['POST'])
def banish_card():
    global deck, banished, soul_shackles
    for _ in range(soul_shackles):
        if deck:
            card = deck.pop(0)
            banished.append(card)
    return jsonify({"banished": banished, "deck_count": len(deck)})

@chane_bp.route('/pitch_card', methods=['POST'])
def pitch_card():
    global deck, hand, pitched
    card_id = request.json.get('card_id')
    if card_id in hand:
        hand.remove(card_id)
        pitched.append(card_id)
    return jsonify({"deck_count": len(deck), "hand": hand})

@chane_bp.route('/play_card', methods=['POST'])
def play_card():
    global hand
    card_id = request.json.get('card_id')
    if card_id in hand:
        hand.remove(card_id)
    return jsonify({"deck_count": len(deck), "hand": hand})

@chane_bp.route('/shuffle_deck', methods=['POST'])
def shuffle_deck():
    global deck
    random.shuffle(deck)
    return jsonify({"deck_count": len(deck)})

@chane_bp.route('/end_turn', methods=['POST'])
def end_turn():
    global hand, arsenal, pitched, soul_shackles, deck
    create_shackle = request.json.get('create_shackle', False)
    
    if create_shackle:
        soul_shackles += 1

    # Option to skip arseling a card
    if len(arsenal) == 0 and len(hand) > 0:
        arsenal_option = request.json.get('arsenal_card', False)
        if arsenal_option:
            arsenal.append(hand.pop())

    # Add pitched cards to the bottom of the deck
    deck.extend(pitched)
    pitched = []

    while len(hand) < 4 and deck:
        card = deck.pop(0)
        hand.append(card)
    
    return jsonify({
        "deck_count": len(deck),
        "hand": hand,
        "arsenal": arsenal,
        "soul_shackles": soul_shackles
    })

@chane_bp.route('/waste_card', methods=['POST'])
def waste_card():
    global hand
    card_id = request.json.get('card_id')
    if card_id in hand:
        hand.remove(card_id)
    return jsonify({"deck_count": len(deck), "hand": hand})

@chane_bp.route('/deck_status', methods=['GET'])
def deck_status():
    global deck, soul_shackles
    drawn_cards = []
    banished_cards = []
    current_shackles = soul_shackles
    index = 0

    while index < len(deck):
        # Calculate drawn cards for this turn
        drawn_this_turn = deck[index:index + 4]
        drawn_cards.extend(drawn_this_turn)
        index += 4
        
        # Calculate banished cards for this turn
        banished_this_turn = deck[index:index + current_shackles]
        banished_cards.extend(banished_this_turn)
        index += current_shackles

        # Increase the number of soul shackles if a shackle is assumed to be created each turn
        current_shackles += 1

    return jsonify({
        "deck": deck,
        "hand": hand,
        "banished": banished,
        "arsenal": arsenal,
        "deck_count": len(deck),
        "drawn_cards": drawn_cards,
        "banished_cards": banished_cards,
        "soul_shackles": soul_shackles
    })

@chane_bp.route('/')
def index():
    return render_template('chane/chane.html')