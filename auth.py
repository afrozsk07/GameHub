from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from extensions import db
from models import User, Score, GameState
from forms import LoginForm, RegistrationForm, ProfileUpdateForm
from datetime import datetime

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None or not check_password_hash(user.password_hash, form.password.data):
            flash('Invalid email or password', 'error')
            return redirect(url_for('auth.login'))
        
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or not next_page.startswith('/'):
            next_page = url_for('index')
        return redirect(next_page)
    
    return render_template('auth/login.html', title='Sign In', form=form)

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(
            username=form.username.data,
            email=form.email.data,
            password_hash=generate_password_hash(form.password.data)
        )
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!', 'success')
        return redirect(url_for('auth.login'))
    
    return render_template('auth/register.html', title='Register', form=form)

@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@auth_bp.route('/profile')
@login_required
def profile():
    form = ProfileUpdateForm(current_user.email)
    form.email.data = current_user.email

    # Get game statistics
    stats = {}
    games = ['tic_tac_toe', 'snakes_and_ladders', 'chess_game', 'anagram_puzzle', 'wordscapes', 'sudoku_puzzle']
    
    for game in games:
        game_scores = Score.query.filter_by(user_id=current_user.id, game_type=game).all()
        total_games = len(game_scores)
        high_score = max([score.score for score in game_scores]) if game_scores else 0
        wins = len([score for score in game_scores if score.score > 0]) if game_scores else 0
        win_rate = round((wins / total_games * 100) if total_games > 0 else 0)
        
        stats[game] = {
            'played': total_games,
            'high_score': high_score,
            'win_rate': win_rate
        }

    # Get achievements
    achievements = [
        {
            'name': 'Tic Tac Pro',
            'description': 'Win 10 consecutive Tic Tac Toe games against computer',
            'icon': 'fa-times',
            'unlocked': stats['tic_tac_toe']['win_rate'] >= 80
        },
        {
            'name': 'Snake Charmer',
            'description': 'Win 5 games of Snakes & Ladders against computer',
            'icon': 'fa-dice',
            'unlocked': stats['snakes_and_ladders']['played'] >= 5 and stats['snakes_and_ladders']['win_rate'] >= 60
        },
        {
            'name': 'Chess Novice',
            'description': 'Win your first chess game',
            'icon': 'fa-chess-knight',
            'unlocked': stats['chess_game']['win_rate'] > 0
        },
        {
            'name': 'Word Wizard',
            'description': 'Solve 50 anagrams',
            'icon': 'fa-spell-check',
            'unlocked': stats['anagram_puzzle']['played'] >= 50
        },
        {
            'name': 'Wordscapes Expert',
            'description': 'Complete 10 levels in Wordscapes',
            'icon': 'fa-book-open',
            'unlocked': stats['wordscapes']['played'] >= 10
        },
        {
            'name': 'Sudoku Solver',
            'description': 'Complete a hard Sudoku puzzle',
            'icon': 'fa-th-large',
            'unlocked': stats['sudoku_puzzle']['played'] >= 1
        }
    ]

    # Get recent activity
    recent_activity = []
    recent_scores = Score.query.filter_by(user_id=current_user.id).order_by(Score.timestamp.desc()).limit(5).all()
    
    for score in recent_scores:
        activity = {
            'icon': 'fa-gamepad',
            'description': f'Scored {score.score} points in {score.game_type.replace("_", " ").title()}',
            'timestamp': score.timestamp
        }
        recent_activity.append(activity)

    return render_template('auth/profile.html',
                         title='Profile',
                         form=form,
                         stats=stats,
                         achievements=achievements,
                         recent_activity=recent_activity)

@auth_bp.route('/profile/update', methods=['POST'])
@login_required
def update_profile():
    form = ProfileUpdateForm(current_user.email)
    if form.validate_on_submit():
        current_user.email = form.email.data
        if form.new_password.data:
            current_user.password_hash = generate_password_hash(form.new_password.data)
        db.session.commit()
        flash('Your profile has been updated.', 'success')
        return redirect(url_for('auth.profile'))
    
    for field, errors in form.errors.items():
        for error in errors:
            flash(f'{getattr(form, field).label.text}: {error}', 'error')
    return redirect(url_for('auth.profile')) 