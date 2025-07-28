from flask import Blueprint, jsonify, request, session
from extensions import db
from models import Score, GameState, WordList
from datetime import datetime
import random
import uuid

api_bp = Blueprint('api', __name__)

# Score management
@api_bp.route('/api/games/submit-score', methods=['POST'])
def submit_score():
    data = request.get_json()
    game_type = data.get('game_type')
    score = data.get('score')
    player_name = data.get('player_name', 'Anonymous')

    if not game_type or score is None:
        return jsonify({'error': 'Missing required fields'}), 400

    # Get player's previous high score
    high_score = Score.query.filter_by(
        player_name=player_name,
        game_type=game_type
    ).order_by(Score.score.desc()).first()

    # Create new score entry
    new_score = Score(
        player_name=player_name,
        game_type=game_type,
        score=score,
        timestamp=datetime.utcnow()
    )
    db.session.add(new_score)
    db.session.commit()

    return jsonify({
        'success': True,
        'highScore': not high_score or score > high_score.score
    })

# Game state management
@api_bp.route('/api/games/save-state', methods=['POST'])
def save_game_state():
    data = request.get_json()
    game_type = data.get('game_type')
    state_data = data.get('state_data')

    if not game_type or not state_data:
        return jsonify({'error': 'Missing required fields'}), 400

    # Generate session ID if not exists
    if 'session_id' not in session:
        session['session_id'] = str(uuid.uuid4())

    # Update or create game state
    game_state = GameState.query.filter_by(
        session_id=session['session_id'],
        game_type=game_type
    ).first()

    if game_state:
        game_state.state_data = state_data
        game_state.timestamp = datetime.utcnow()
    else:
        game_state = GameState(
            session_id=session['session_id'],
            game_type=game_type,
            state_data=state_data,
            timestamp=datetime.utcnow()
        )
        db.session.add(game_state)

    db.session.commit()
    return jsonify({'success': True})

@api_bp.route('/api/games/load-state/<game_type>')
def load_game_state(game_type):
    if 'session_id' not in session:
        return jsonify({'state_data': None})

    game_state = GameState.query.filter_by(
        session_id=session['session_id'],
        game_type=game_type
    ).first()

    if not game_state:
        return jsonify({'state_data': None})

    return jsonify({'state_data': game_state.state_data})

# Leaderboard
@api_bp.route('/api/games/leaderboard/<game_type>')
def get_leaderboard(game_type):
    top_scores = db.session.query(
        Score.player_name,
        db.func.max(Score.score).label('max_score')
    ).filter_by(game_type=game_type).group_by(Score.player_name).order_by(
        db.text('max_score DESC')
    ).limit(10).all()

    leaderboard = []
    for player_name, score in top_scores:
        leaderboard.append({
            'player_name': player_name,
            'score': score
        })

    return jsonify(leaderboard)

# Word list for word games
@api_bp.route('/api/words/<difficulty>')
def get_words(difficulty):
    words = WordList.query.filter_by(difficulty=difficulty).order_by(db.func.random()).limit(20).all()
    return jsonify([{
        'word': w.word,
        'category': w.category
    } for w in words]) 