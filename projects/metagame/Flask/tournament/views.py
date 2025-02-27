from flask import render_template, request, redirect, url_for
from . import tournament_bp

@tournament_bp.route('/submit_decks', methods=['GET'])
def submit_decks():
    # Render the initial form for deck submission
    return render_template('tournament/submit_decks.html')

@tournament_bp.route('/matchup_spreads', methods=['POST'])
def matchup_spreads():
    # Extract form data
    deck_names = request.form.getlist('deck_names[]')
    quantities = request.form.getlist('quantities[]')
    number_of_players = request.form['number_of_players']
    rounds = request.form['rounds']
    skill_modifier = request.form['skill_modifier']

    # Render the matchup spreads table based on the number of decks
    return render_template('tournament/matchup_spreads.html', deck_names=deck_names)



