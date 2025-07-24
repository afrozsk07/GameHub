from flask import Blueprint, jsonify, request
from flask_login import current_user, login_required
from extensions import db
from models import Score, GameState, WordList, User
from datetime import datetime
import random

api_bp = Blueprint('api', __name__)

# Wordscapes endpoints
@api_bp.route('/api/wordscapes/level/<difficulty>/<int:level>')
@login_required
def get_wordscapes_level(difficulty, level):
    # Word puzzles for each difficulty level
    puzzles = {
        'easy': [
            {'letters': 'star', 'words': ['star', 'art', 'tar', 'rat', 'sat']},
            {'letters': 'heart', 'words': ['heart', 'heat', 'hear', 'art', 'ear', 'hat']},
            {'letters': 'dream', 'words': ['dream', 'dare', 'dear', 'read', 'made', 'ram']},
            {'letters': 'smile', 'words': ['smile', 'slim', 'mile', 'lime', 'isle']},
            {'letters': 'paint', 'words': ['paint', 'pain', 'pint', 'tap', 'nap', 'pat']},
            {'letters': 'cloud', 'words': ['cloud', 'loud', 'cold', 'duo', 'doc']},
            {'letters': 'stone', 'words': ['stone', 'tone', 'sent', 'nest', 'set']},
            {'letters': 'light', 'words': ['light', 'tight', 'hit', 'lit', 'gilt']},
            {'letters': 'beach', 'words': ['beach', 'each', 'ache', 'cab', 'be']},
            {'letters': 'fresh', 'words': ['fresh', 'href', 'she', 'her', 'ref']},
            # New Easy Levels
            {'letters': 'bread', 'words': ['bread', 'bear', 'dare', 'read', 'bar', 'bed']},
            {'letters': 'plate', 'words': ['plate', 'leap', 'peal', 'tale', 'tap', 'eat']},
            {'letters': 'steam', 'words': ['steam', 'team', 'meat', 'tame', 'same', 'eat']},
            {'letters': 'crane', 'words': ['crane', 'care', 'race', 'near', 'can', 'ear']},
            {'letters': 'spare', 'words': ['spare', 'spear', 'pear', 'reap', 'rap', 'ear']},
            {'letters': 'train', 'words': ['train', 'rain', 'tain', 'air', 'tan', 'art']},
            {'letters': 'coast', 'words': ['coast', 'cast', 'coat', 'cat', 'sat', 'at']},
            {'letters': 'flame', 'words': ['flame', 'fame', 'male', 'meal', 'lame', 'am']},
            {'letters': 'share', 'words': ['share', 'hear', 'hare', 'sear', 'has', 'ear']},
            {'letters': 'trace', 'words': ['trace', 'care', 'race', 'cat', 'eat', 'tea']}
        ],
        'medium': [
            {'letters': 'garden', 'words': ['garden', 'danger', 'range', 'anger', 'grade', 'near', 'read']},
            {'letters': 'planet', 'words': ['planet', 'plane', 'plant', 'petal', 'leap', 'neat']},
            {'letters': 'spring', 'words': ['spring', 'sprig', 'ring', 'ping', 'spin', 'sip']},
            {'letters': 'flower', 'words': ['flower', 'lower', 'flow', 'wolf', 'fowl', 'flew']},
            {'letters': 'stream', 'words': ['stream', 'master', 'teams', 'steam', 'tame', 'rest']},
            {'letters': 'bridge', 'words': ['bridge', 'ridge', 'bride', 'grid', 'bed', 'bid']},
            {'letters': 'forest', 'words': ['forest', 'store', 'rest', 'sort', 'set', 'for']},
            {'letters': 'window', 'words': ['window', 'wind', 'down', 'win', 'now', 'own']},
            {'letters': 'silver', 'words': ['silver', 'liver', 'lives', 'rise', 'veil', 'lie']},
            {'letters': 'castle', 'words': ['castle', 'scale', 'case', 'lace', 'sale', 'eat']},
            # New Medium Levels
            {'letters': 'monkey', 'words': ['monkey', 'money', 'key', 'men', 'one', 'my']},
            {'letters': 'turtle', 'words': ['turtle', 'true', 'rule', 'let', 'lure', 'tel']},
            {'letters': 'rabbit', 'words': ['rabbit', 'bait', 'trait', 'tab', 'bar', 'bit']},
            {'letters': 'jaguar', 'words': ['jaguar', 'jar', 'rug', 'jar', 'rag', 'jar']},
            {'letters': 'parrot', 'words': ['parrot', 'part', 'trap', 'port', 'tap', 'top']},
            {'letters': 'donkey', 'words': ['donkey', 'done', 'deny', 'key', 'one', 'end']},
            {'letters': 'spider', 'words': ['spider', 'pride', 'ride', 'side', 'ripe', 'sip']},
            {'letters': 'beaver', 'words': ['beaver', 'brave', 'bear', 'ever', 'ear', 'bar']},
            {'letters': 'cheese', 'words': ['cheese', 'cheer', 'here', 'see', 'she', 'he']},
            {'letters': 'coffee', 'words': ['coffee', 'force', 'free', 'face', 'fee', 'of']}
        ],
        'hard': [
            {'letters': 'rainbow', 'words': ['rainbow', 'brain', 'warn', 'rain', 'bow', 'raw', 'win']},
            {'letters': 'diamond', 'words': ['diamond', 'domain', 'maid', 'mind', 'dam', 'aid', 'man']},
            {'letters': 'thunder', 'words': ['thunder', 'hunter', 'under', 'hurt', 'red', 'den', 'run']},
            {'letters': 'crystal', 'words': ['crystal', 'scary', 'stay', 'lacy', 'last', 'car', 'try']},
            {'letters': 'mystery', 'words': ['mystery', 'system', 'term', 'rest', 'yes', 'try', 'set']},
            {'letters': 'journey', 'words': ['journey', 'enjoy', 'your', 'jury', 'joy', 'run', 'one']},
            {'letters': 'harmony', 'words': ['harmony', 'manor', 'harm', 'many', 'horn', 'man', 'hay']},
            {'letters': 'blossom', 'words': ['blossom', 'bloom', 'loss', 'moss', 'solo', 'sob', 'mom']},
            {'letters': 'sunrise', 'words': ['sunrise', 'ruins', 'sure', 'rise', 'sun', 'sir', 'run']},
            {'letters': 'whisper', 'words': ['whisper', 'swipe', 'wise', 'wish', 'whip', 'sip', 'we']},
            # New Hard Levels
            {'letters': 'creative', 'words': ['creative', 'reactive', 'active', 'trace', 'care', 'eat', 'tea']},
            {'letters': 'triangle', 'words': ['triangle', 'integral', 'alert', 'angle', 'tale', 'real', 'gate']},
            {'letters': 'mountain', 'words': ['mountain', 'amount', 'mount', 'main', 'team', 'aim', 'man']},
            {'letters': 'elephant', 'words': ['elephant', 'help', 'plant', 'heal', 'leap', 'tale', 'pant']},
            {'letters': 'dinosaur', 'words': ['dinosaur', 'sound', 'raid', 'road', 'sand', 'said', 'sun']},
            {'letters': 'computer', 'words': ['computer', 'compute', 'tempo', 'route', 'come', 'core', 'pet']},
            {'letters': 'butterfly', 'words': ['butterfly', 'flutter', 'beauty', 'truly', 'fruit', 'try', 'but']},
            {'letters': 'crocodile', 'words': ['crocodile', 'cooler', 'circle', 'door', 'dice', 'cold', 'rod']},
            {'letters': 'penguin', 'words': ['penguin', 'ping', 'pine', 'gun', 'pen', 'pig', 'up']},
            {'letters': 'octopus', 'words': ['octopus', 'scout', 'spot', 'stop', 'cup', 'top', 'up']}
        ]
    }
    
    try:
        if difficulty not in puzzles:
            return jsonify({'error': 'Invalid difficulty level'}), 400
        
        # Randomly select a puzzle for the given difficulty
        puzzle = random.choice(puzzles[difficulty])
        return jsonify(puzzle)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@api_bp.route('/api/wordscapes/score', methods=['POST'])
@login_required
def submit_wordscapes_score():
    data = request.get_json()
    score = Score(
        user_id=current_user.id,
        game_type='wordscapes',
        score=data['score'],
        timestamp=datetime.utcnow()
    )
    db.session.add(score)
    db.session.commit()
    return jsonify({'message': 'Score submitted successfully'})

# Score management
@api_bp.route('/api/games/submit-score', methods=['POST'])
@login_required
def submit_score():
    data = request.get_json()
    game_type = data.get('game_type')
    score = data.get('score')

    if not game_type or score is None:
        return jsonify({'error': 'Missing required fields'}), 400

    # Get user's previous high score
    high_score = Score.query.filter_by(
        user_id=current_user.id,
        game_type=game_type
    ).order_by(Score.score.desc()).first()

    # Create new score entry
    new_score = Score(
        user_id=current_user.id,
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
@login_required
def save_game_state():
    data = request.get_json()
    game_type = data.get('game_type')
    state_data = data.get('state_data')

    if not game_type or not state_data:
        return jsonify({'error': 'Missing required fields'}), 400

    # Update or create game state
    game_state = GameState.query.filter_by(
        user_id=current_user.id,
        game_type=game_type
    ).first()

    if game_state:
        game_state.state_data = state_data
        game_state.timestamp = datetime.utcnow()
    else:
        game_state = GameState(
            user_id=current_user.id,
            game_type=game_type,
            state_data=state_data,
            timestamp=datetime.utcnow()
        )
        db.session.add(game_state)

    db.session.commit()
    return jsonify({'success': True})

@api_bp.route('/api/games/load-state/<game_type>')
@login_required
def load_game_state(game_type):
    game_state = GameState.query.filter_by(
        user_id=current_user.id,
        game_type=game_type
    ).first()

    if not game_state:
        return jsonify({'state_data': None})

    return jsonify({'state_data': game_state.state_data})

# Leaderboard
@api_bp.route('/api/games/leaderboard/<game_type>')
def get_leaderboard(game_type):
    top_scores = db.session.query(
        Score.user_id,
        db.func.max(Score.score).label('max_score')
    ).filter_by(game_type=game_type).group_by(Score.user_id).order_by(
        db.text('max_score DESC')
    ).limit(10).all()

    leaderboard = []
    for user_id, score in top_scores:
        user = User.query.get(user_id)
        leaderboard.append({
            'username': user.username,
            'score': score
        })

    return jsonify(leaderboard)

# Word list for word games
@api_bp.route('/api/words/<difficulty>')
@login_required
def get_words(difficulty):
    words = WordList.query.filter_by(difficulty=difficulty).order_by(db.func.random()).limit(20).all()
    return jsonify([{
        'word': w.word,
        'category': w.category
    } for w in words]) 