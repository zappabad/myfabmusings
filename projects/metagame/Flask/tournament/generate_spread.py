from flask import request, render_template
from . import tournament

from names import get_full_name

@tournament.route('/')
def index():
    return render_template('index.html')  # Render the form

@tournament.route('/submit', methods=['POST'])
def submit():
    # Retrieve data from form
    deck_name = request.form.get('deckName')
    matchup_spread = request.form.get('matchupSpread')
    
    # Process the data (e.g., save to database, perform calculations)
    # For demonstration, we'll just print it
    print(f"Deck Name: {deck_name}, Matchup Spread: {matchup_spread}")
    
    # Redirect or render a page upon successful submission
    return 'Form submitted successfully!'

