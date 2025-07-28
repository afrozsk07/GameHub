from flask import Blueprint, render_template, jsonify, request, session
from extensions import db
from models import Score
from datetime import datetime
import uuid

games_bp = Blueprint('games', __name__)

@games_bp.route('/chess-game')
def chess_game():
    return render_template('games/chess_game.html')

@games_bp.route('/games/save-score', methods=['POST'])
def save_score():
    data = request.get_json()
    game_name = data.get('game')
    score_value = data.get('score')
    player_name = data.get('player_name', 'Anonymous')
    
    if game_name and score_value:
        score = Score(
            player_name=player_name,
            game_type=game_name,
            score=score_value,
            timestamp=datetime.utcnow()
        )
        db.session.add(score)
        db.session.commit()
        return jsonify({'success': True})
    return jsonify({'success': False, 'error': 'Invalid data'}), 400

@games_bp.route('/tictactoe')
def tictactoe():
    return render_template('games/tictactoe.html')

@games_bp.route('/snakes-and-ladders')
def snakes_and_ladders():
    return render_template('games/snakes_and_ladders.html')

# API endpoints for game state
@games_bp.route('/api/tictactoe/move', methods=['POST'])
def tictactoe_move():
    data = request.get_json()
    # Process move and return updated game state
    return jsonify(data)

@games_bp.route('/api/snakes-and-ladders/roll', methods=['POST'])
def snake_ladder_roll():
    data = request.get_json()
    # Process dice roll and return updated game state
    return jsonify(data) 