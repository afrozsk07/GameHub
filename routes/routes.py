from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user

games_bp = Blueprint('games', __name__)

@games_bp.route('/chess-game')
@login_required
def chess_game():
    return render_template('games/chess_game.html')

@games_bp.route('/wordscapes')
@login_required
def wordscapes():
    return render_template('games/wordscapes.html')

@games_bp.route('/tictactoe')
@login_required
def tictactoe():
    return render_template('games/tictactoe.html')

@games_bp.route('/snakes-and-ladders')
@login_required
def snakes_and_ladders():
    return render_template('games/snakes_and_ladders.html')

@games_bp.route('/anagram-solver')
@login_required
def anagram_solver():
    return render_template('games/anagram_solver.html')

@games_bp.route('/word-scramble')
@login_required
def word_scramble():
    return render_template('games/word_scramble.html')

@games_bp.route('/sudoku-puzzle')
@login_required
def sudoku_puzzle():
    return render_template('games/sudoku_puzzle.html') 