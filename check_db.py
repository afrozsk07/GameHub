from app import app
from models import WordList, db
from data.word_database import WORD_DATABASE

def check_database():
    with app.app_context():
        # Check words in the database
        db_words = WordList.query.all()
        print("\n=== Database Words ===")
        print(f"Total words in database: {len(db_words)}")
        if db_words:
            print("Sample words:", [w.word for w in db_words[:5]])
        else:
            print("No words in database")

        # Check words in the file
        print("\n=== Word Database File ===")
        for difficulty, words in WORD_DATABASE.items():
            print(f"\nDifficulty: {difficulty}")
            print(f"Number of words: {len(words)}")
            print("Sample words:", [w['word'] for w in words[:5]])

if __name__ == '__main__':
    check_database() 