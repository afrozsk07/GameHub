# GameHub

GameHub is a Python-based web application featuring a collection of engaging games, built with Flask and modern web technologies. The platform offers a beautiful, responsive UI, smooth animations, and a rich user experience with authentication, profiles, achievements, and leaderboards.

## Games Available

1. **Tic Tac Toe** – Classic X's and O's with human vs human and human vs computer modes
2. **Snakes & Ladders** – Digital version of the classic board game, play against a friend or the computer
3. **Chess Game** – Fully functional chess with local multiplayer and human vs computer (easy, medium, hard)
4. **Anagram Puzzle** – Unscramble words and improve your vocabulary
5. **Wordscapes** – Create words from a circle of letters in a relaxing word puzzle
6. **Sudoku Puzzle** – Challenge your logic and number skills with multiple difficulty levels

## Features

- Modern, responsive UI with Tailwind CSS
- User authentication (register, login, logout) and profile management
- Game statistics, achievements, and recent activity on user profiles
- Persistent score tracking and leaderboards
- Beautiful animations and transitions
- Cross-platform compatibility (desktop and mobile)
- Save and resume game progress
- Secure password hashing and session management

## Technical Stack

- **Backend**: Python Flask
- **Database**: SQLite with SQLAlchemy ORM
- **Frontend**: HTML5, Tailwind CSS, JavaScript
- **Authentication**: Flask-Login
- **Asset Management**: Flask-Assets
- **Dependencies**: See requirements.txt

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/GameHub.git
   cd GameHub
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Initialize the database:
   ```bash
   flask db init
   flask db migrate
   flask db upgrade
   ```

5. Run the application:
   ```bash
   python app.py
   ```

6. Open your browser and navigate to:
   ```
   http://localhost:5000
   ```

## Project Structure

```
GameHub/
├── app.py              # Main application file
├── models.py           # Database models
├── auth.py             # Authentication and profile routes
├── api.py              # API endpoints for scores, state, word lists
├── routes/             # Game route blueprints
├── forms.py            # WTForms definitions
├── requirements.txt    # Project dependencies
├── static/             # Static files (CSS, JS, images)
├── templates/          # HTML templates
│   ├── base.html       # Base template
│   ├── index.html      # Home page
│   ├── auth/           # Auth/profile templates
│   ├── games/          # Game-specific templates
│   └── errors/         # Error pages
└── instance/
    └── gamehub.db      # SQLite database
```

## Contributing

1. Fork the repository
2. Create a new branch for your feature
3. Commit your changes
4. Push to your branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Flask team for the excellent web framework
- Tailwind CSS for the beautiful UI components
- Font Awesome for the icons
- chess.js and chessboard.js for chess logic/UI
- All contributors and users of GameHub 