from flask import Flask, render_template
from flask_assets import Bundle
import os
from extensions import db, migrate, assets

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY') or 'your-secret-key-here'
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL') or 'sqlite:///gamehub.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    assets.init_app(app)

    # Asset bundles
    css = Bundle('scss/main.scss', filters='libsass,cssmin', output='css/main.css')
    js = Bundle('js/*.js', filters='jsmin', output='js/bundle.js')
    assets.register('css', css)
    assets.register('js', js)

    # Import routes after app initialization to avoid circular imports
    from api import api_bp
    from routes import games_bp

    # Register blueprints
    app.register_blueprint(api_bp)
    app.register_blueprint(games_bp, url_prefix='/games')

    # Error handlers
    @app.errorhandler(404)
    def not_found_error(error):
        return render_template('errors/404.html'), 404

    @app.errorhandler(500)
    def internal_error(error):
        db.session.rollback()
        return render_template('errors/500.html'), 500

    # Main routes
    @app.route('/')
    def index():
        return render_template('index.html')

    return app

app = create_app()

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True) 