from flask import Blueprint, render_template, jsonify, request
from flask_login import login_required, current_user
from models import db, Score, WordList
from datetime import datetime
import random
import os
import importlib
import sys

games = Blueprint('games', __name__)

@games.route('/api/debug-words')
def debug_words():
    try:
        # Force reload the word database module
        import data.word_database
        importlib.reload(data.word_database)
        from data.word_database import WORD_DATABASE
        
        # Get words from database
        db_words = WordList.query.all()
        
        result = {
            'file_data': {
                'difficulties': list(WORD_DATABASE.keys()),
                'counts': {
                    diff: len(words) for diff, words in WORD_DATABASE.items()
                },
                'sample_words': {
                    diff: [w['word'] for w in words[:5]] for diff, words in WORD_DATABASE.items()
                }
            },
            'db_data': {
                'total_words': len(db_words),
                'sample_words': [w.word for w in db_words[:5]] if db_words else []
            }
        }
        return jsonify(result)
    except Exception as e:
        import traceback
        traceback.print_exc()
        return jsonify({"error": str(e)}), 500

@games.route('/api/words/<difficulty>')
@login_required
def get_words(difficulty):
    try:
        print("\n=== Word Database Debug ===")
        db_path = os.path.abspath('data/word_database.py')
        print(f"Database file location: {db_path}")
        print(f"Database file exists: {os.path.exists(db_path)}")
        
        # Force reload the word database module
        import data.word_database
        importlib.reload(data.word_database)
        from data.word_database import WORD_DATABASE
        
        print(f"Available difficulties: {list(WORD_DATABASE.keys())}")
        print(f"Requested difficulty: {difficulty}")
        
        if difficulty not in WORD_DATABASE:
            print(f"Error: Invalid difficulty '{difficulty}'")
            return jsonify([]), 404

        # Create a deep copy of the words list
        words = list(WORD_DATABASE[difficulty])
        
        # Debug information
        print(f"Number of words: {len(words)}")
        print(f"First 5 words: {[w['word'] for w in words[:5]]}")
        print(f"All words: {[w['word'] for w in words]}")
        print("=========================\n")

        # Shuffle the words
        random.shuffle(words)
        return jsonify(words)
    except Exception as e:
        print(f"Error in get_words: {str(e)}")
        import traceback
        traceback.print_exc()
        return jsonify({"error": str(e)}), 500

@games.route('/tictactoe')
@login_required
def tictactoe():
    return render_template('games/tictactoe.html')

@games.route('/snakes_and_ladders')
@login_required
def snakes_and_ladders():
    return render_template('games/snakes_and_ladders.html')

@games.route('/chess_game')
@login_required
def chess_game():
    return render_template('games/chess_game.html')

@games.route('/anagram-solver')
@login_required
def anagram_solver():
    return render_template('games/anagram_solver.html')

@games.route('/api/test-words')
@login_required
def test_words():
    try:
        # Force reload the word database module
        import data.word_database
        importlib.reload(data.word_database)
        from data.word_database import WORD_DATABASE
        
        result = {
            'difficulties': list(WORD_DATABASE.keys()),
            'counts': {
                diff: len(words) for diff, words in WORD_DATABASE.items()
            },
            'sample_words': {
                diff: [w['word'] for w in words[:5]] for diff, words in WORD_DATABASE.items()
            }
        }
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@games.route('/save-score', methods=['POST'])
@login_required
def save_score():
    data = request.get_json()
    game_name = data.get('game')
    score = data.get('score')
    
    if game_name and score:
        game_score = Score(
            user_id=current_user.id,
            game_type=game_name,
            score=score,
            timestamp=datetime.utcnow()
        )
        db.session.add(game_score)
        db.session.commit()
        return jsonify({'status': 'success'})
    
    return jsonify({'status': 'error', 'message': 'Invalid data'}), 400

@games.route('/sudoku_puzzle')
@login_required
def sudoku_puzzle():
    return render_template('games/sudoku_puzzle.html') 