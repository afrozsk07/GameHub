from flask import Blueprint, render_template, jsonify, request
from flask_login import login_required, current_user
from extensions import db
from models import Score
from datetime import datetime

games_bp = Blueprint('games', __name__)

@games_bp.route('/chess-game')
@login_required
def chess_game():
    return render_template('games/chess_game.html')

@games_bp.route('/games/save-score', methods=['POST'])
@login_required
def save_score():
    data = request.get_json()
    game_name = data.get('game')
    score_value = data.get('score')
    
    if game_name and score_value:
        score = Score(
            user_id=current_user.id,
            game=game_name,
            score=score_value,
            date=datetime.utcnow()
        )
        db.session.add(score)
        db.session.commit()
        return jsonify({'success': True})
    return jsonify({'success': False, 'error': 'Invalid data'}), 400

@games_bp.route('/tictactoe')
@login_required
def tictactoe():
    return render_template('games/tictactoe.html')

@games_bp.route('/snakes-and-ladders')
@login_required
def snakes_and_ladders():
    return render_template('games/snakes_and_ladders.html')

# API endpoints for game state
@games_bp.route('/api/tictactoe/move', methods=['POST'])
@login_required
def tictactoe_move():
    data = request.get_json()
    # Process move and return updated game state
    return jsonify(data)

@games_bp.route('/api/snakes-and-ladders/roll', methods=['POST'])
@login_required
def snake_ladder_roll():
    data = request.get_json()
    # Process dice roll and return updated game state
    return jsonify(data) 