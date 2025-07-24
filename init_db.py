from app import app, db
from models import QuizQuestion, WordList
import json

def init_db():
    with app.app_context():
        # Create tables
        db.create_all()

        # Add quiz questions
        if QuizQuestion.query.count() == 0:
            questions = [
                {
                    'category': 'general',
                    'question': 'What is the capital of France?',
                    'correct_answer': 'Paris',
                    'wrong_answer1': 'London',
                    'wrong_answer2': 'Berlin',
                    'wrong_answer3': 'Madrid',
                    'difficulty': 'easy'
                },
                {
                    'category': 'science',
                    'question': 'What is the chemical symbol for gold?',
                    'correct_answer': 'Au',
                    'wrong_answer1': 'Ag',
                    'wrong_answer2': 'Fe',
                    'wrong_answer3': 'Cu',
                    'difficulty': 'easy'
                },
                {
                    'category': 'history',
                    'question': 'In which year did World War II end?',
                    'correct_answer': '1945',
                    'wrong_answer1': '1944',
                    'wrong_answer2': '1946',
                    'wrong_answer3': '1943',
                    'difficulty': 'medium'
                },
                {
                    'category': 'geography',
                    'question': 'Which is the largest ocean on Earth?',
                    'correct_answer': 'Pacific Ocean',
                    'wrong_answer1': 'Atlantic Ocean',
                    'wrong_answer2': 'Indian Ocean',
                    'wrong_answer3': 'Arctic Ocean',
                    'difficulty': 'easy'
                }
            ]

            for q in questions:
                question = QuizQuestion(
                    category=q['category'],
                    question=q['question'],
                    correct_answer=q['correct_answer'],
                    wrong_answer1=q['wrong_answer1'],
                    wrong_answer2=q['wrong_answer2'],
                    wrong_answer3=q['wrong_answer3'],
                    difficulty=q['difficulty']
                )
                db.session.add(question)

        # Add word list
        if WordList.query.count() == 0:
            words = [
                # Technology (Easy)
                {'word': 'code', 'difficulty': 'easy', 'category': 'technology'},
                {'word': 'data', 'difficulty': 'easy', 'category': 'technology'},
                {'word': 'file', 'difficulty': 'easy', 'category': 'technology'},
                {'word': 'link', 'difficulty': 'easy', 'category': 'technology'},
                {'word': 'user', 'difficulty': 'easy', 'category': 'technology'},
                {'word': 'wifi', 'difficulty': 'easy', 'category': 'technology'},
                {'word': 'blog', 'difficulty': 'easy', 'category': 'technology'},
                {'word': 'chat', 'difficulty': 'easy', 'category': 'technology'},
                {'word': 'disk', 'difficulty': 'easy', 'category': 'technology'},
                {'word': 'game', 'difficulty': 'easy', 'category': 'technology'},
                {'word': 'icon', 'difficulty': 'easy', 'category': 'technology'},
                {'word': 'mail', 'difficulty': 'easy', 'category': 'technology'},
                {'word': 'menu', 'difficulty': 'easy', 'category': 'technology'},
                {'word': 'save', 'difficulty': 'easy', 'category': 'technology'},
                {'word': 'sync', 'difficulty': 'easy', 'category': 'technology'},
                
                # Technology (Medium)
                {'word': 'python', 'difficulty': 'medium', 'category': 'technology'},
                {'word': 'server', 'difficulty': 'medium', 'category': 'technology'},
                {'word': 'router', 'difficulty': 'medium', 'category': 'technology'},
                {'word': 'backup', 'difficulty': 'medium', 'category': 'technology'},
                {'word': 'update', 'difficulty': 'medium', 'category': 'technology'},
                {'word': 'browser', 'difficulty': 'medium', 'category': 'technology'},
                {'word': 'coding', 'difficulty': 'medium', 'category': 'technology'},
                {'word': 'desktop', 'difficulty': 'medium', 'category': 'technology'},
                {'word': 'firewall', 'difficulty': 'medium', 'category': 'technology'},
                {'word': 'hosting', 'difficulty': 'medium', 'category': 'technology'},
                {'word': 'keyboard', 'difficulty': 'medium', 'category': 'technology'},
                {'word': 'network', 'difficulty': 'medium', 'category': 'technology'},
                {'word': 'program', 'difficulty': 'medium', 'category': 'technology'},
                {'word': 'storage', 'difficulty': 'medium', 'category': 'technology'},
                {'word': 'website', 'difficulty': 'medium', 'category': 'technology'},
                
                # Technology (Hard)
                {'word': 'algorithm', 'difficulty': 'hard', 'category': 'technology'},
                {'word': 'database', 'difficulty': 'hard', 'category': 'technology'},
                {'word': 'interface', 'difficulty': 'hard', 'category': 'technology'},
                {'word': 'javascript', 'difficulty': 'hard', 'category': 'technology'},
                {'word': 'framework', 'difficulty': 'hard', 'category': 'technology'},
                {'word': 'encryption', 'difficulty': 'hard', 'category': 'technology'},
                {'word': 'middleware', 'difficulty': 'hard', 'category': 'technology'},
                {'word': 'repository', 'difficulty': 'hard', 'category': 'technology'},
                {'word': 'blockchain', 'difficulty': 'hard', 'category': 'technology'},
                {'word': 'kubernetes', 'difficulty': 'hard', 'category': 'technology'},
                {'word': 'microservice', 'difficulty': 'hard', 'category': 'technology'},
                {'word': 'virtualization', 'difficulty': 'hard', 'category': 'technology'},
                {'word': 'authentication', 'difficulty': 'hard', 'category': 'technology'},
                {'word': 'cybersecurity', 'difficulty': 'hard', 'category': 'technology'},
                {'word': 'optimization', 'difficulty': 'hard', 'category': 'technology'},

                # Animals (Easy)
                {'word': 'cat', 'difficulty': 'easy', 'category': 'animals'},
                {'word': 'dog', 'difficulty': 'easy', 'category': 'animals'},
                {'word': 'bird', 'difficulty': 'easy', 'category': 'animals'},
                {'word': 'fish', 'difficulty': 'easy', 'category': 'animals'},
                {'word': 'lion', 'difficulty': 'easy', 'category': 'animals'},
                {'word': 'bear', 'difficulty': 'easy', 'category': 'animals'},
                {'word': 'deer', 'difficulty': 'easy', 'category': 'animals'},
                {'word': 'duck', 'difficulty': 'easy', 'category': 'animals'},
                {'word': 'frog', 'difficulty': 'easy', 'category': 'animals'},
                {'word': 'goat', 'difficulty': 'easy', 'category': 'animals'},
                {'word': 'hawk', 'difficulty': 'easy', 'category': 'animals'},
                {'word': 'mice', 'difficulty': 'easy', 'category': 'animals'},
                {'word': 'owl', 'difficulty': 'easy', 'category': 'animals'},
                {'word': 'pig', 'difficulty': 'easy', 'category': 'animals'},
                {'word': 'wolf', 'difficulty': 'easy', 'category': 'animals'},

                # Animals (Medium)
                {'word': 'monkey', 'difficulty': 'medium', 'category': 'animals'},
                {'word': 'giraffe', 'difficulty': 'medium', 'category': 'animals'},
                {'word': 'penguin', 'difficulty': 'medium', 'category': 'animals'},
                {'word': 'dolphin', 'difficulty': 'medium', 'category': 'animals'},
                {'word': 'elephant', 'difficulty': 'medium', 'category': 'animals'},
                {'word': 'buffalo', 'difficulty': 'medium', 'category': 'animals'},
                {'word': 'cheetah', 'difficulty': 'medium', 'category': 'animals'},
                {'word': 'gazelle', 'difficulty': 'medium', 'category': 'animals'},
                {'word': 'jaguar', 'difficulty': 'medium', 'category': 'animals'},
                {'word': 'leopard', 'difficulty': 'medium', 'category': 'animals'},
                {'word': 'octopus', 'difficulty': 'medium', 'category': 'animals'},
                {'word': 'panther', 'difficulty': 'medium', 'category': 'animals'},
                {'word': 'raccoon', 'difficulty': 'medium', 'category': 'animals'},
                {'word': 'squirrel', 'difficulty': 'medium', 'category': 'animals'},
                {'word': 'zebra', 'difficulty': 'medium', 'category': 'animals'},

                # Animals (Hard)
                {'word': 'chimpanzee', 'difficulty': 'hard', 'category': 'animals'},
                {'word': 'rhinoceros', 'difficulty': 'hard', 'category': 'animals'},
                {'word': 'hippopotamus', 'difficulty': 'hard', 'category': 'animals'},
                {'word': 'kangaroo', 'difficulty': 'hard', 'category': 'animals'},
                {'word': 'crocodile', 'difficulty': 'hard', 'category': 'animals'},
                {'word': 'anaconda', 'difficulty': 'hard', 'category': 'animals'},
                {'word': 'butterfly', 'difficulty': 'hard', 'category': 'animals'},
                {'word': 'chameleon', 'difficulty': 'hard', 'category': 'animals'},
                {'word': 'dragonfly', 'difficulty': 'hard', 'category': 'animals'},
                {'word': 'gorilla', 'difficulty': 'hard', 'category': 'animals'},
                {'word': 'jellyfish', 'difficulty': 'hard', 'category': 'animals'},
                {'word': 'orangutan', 'difficulty': 'hard', 'category': 'animals'},
                {'word': 'porcupine', 'difficulty': 'hard', 'category': 'animals'},
                {'word': 'scorpion', 'difficulty': 'hard', 'category': 'animals'},
                {'word': 'tarantula', 'difficulty': 'hard', 'category': 'animals'},

                # Food (Easy)
                {'word': 'rice', 'difficulty': 'easy', 'category': 'food'},
                {'word': 'bread', 'difficulty': 'easy', 'category': 'food'},
                {'word': 'milk', 'difficulty': 'easy', 'category': 'food'},
                {'word': 'cake', 'difficulty': 'easy', 'category': 'food'},
                {'word': 'soup', 'difficulty': 'easy', 'category': 'food'},
                {'word': 'bean', 'difficulty': 'easy', 'category': 'food'},
                {'word': 'corn', 'difficulty': 'easy', 'category': 'food'},
                {'word': 'eggs', 'difficulty': 'easy', 'category': 'food'},
                {'word': 'fish', 'difficulty': 'easy', 'category': 'food'},
                {'word': 'ham', 'difficulty': 'easy', 'category': 'food'},
                {'word': 'meat', 'difficulty': 'easy', 'category': 'food'},
                {'word': 'nuts', 'difficulty': 'easy', 'category': 'food'},
                {'word': 'pear', 'difficulty': 'easy', 'category': 'food'},
                {'word': 'salt', 'difficulty': 'easy', 'category': 'food'},
                {'word': 'tuna', 'difficulty': 'easy', 'category': 'food'},

                # Food (Medium)
                {'word': 'burger', 'difficulty': 'medium', 'category': 'food'},
                {'word': 'pizza', 'difficulty': 'medium', 'category': 'food'},
                {'word': 'pasta', 'difficulty': 'medium', 'category': 'food'},
                {'word': 'salad', 'difficulty': 'medium', 'category': 'food'},
                {'word': 'sushi', 'difficulty': 'medium', 'category': 'food'},
                {'word': 'bagel', 'difficulty': 'medium', 'category': 'food'},
                {'word': 'cheese', 'difficulty': 'medium', 'category': 'food'},
                {'word': 'cookie', 'difficulty': 'medium', 'category': 'food'},
                {'word': 'muffin', 'difficulty': 'medium', 'category': 'food'},
                {'word': 'noodle', 'difficulty': 'medium', 'category': 'food'},
                {'word': 'pickle', 'difficulty': 'medium', 'category': 'food'},
                {'word': 'salmon', 'difficulty': 'medium', 'category': 'food'},
                {'word': 'steak', 'difficulty': 'medium', 'category': 'food'},
                {'word': 'waffle', 'difficulty': 'medium', 'category': 'food'},
                {'word': 'yogurt', 'difficulty': 'medium', 'category': 'food'},

                # Food (Hard)
                {'word': 'spaghetti', 'difficulty': 'hard', 'category': 'food'},
                {'word': 'lasagna', 'difficulty': 'hard', 'category': 'food'},
                {'word': 'quesadilla', 'difficulty': 'hard', 'category': 'food'},
                {'word': 'bruschetta', 'difficulty': 'hard', 'category': 'food'},
                {'word': 'guacamole', 'difficulty': 'hard', 'category': 'food'},
                {'word': 'asparagus', 'difficulty': 'hard', 'category': 'food'},
                {'word': 'croissant', 'difficulty': 'hard', 'category': 'food'},
                {'word': 'enchilada', 'difficulty': 'hard', 'category': 'food'},
                {'word': 'fettuccine', 'difficulty': 'hard', 'category': 'food'},
                {'word': 'mozzarella', 'difficulty': 'hard', 'category': 'food'},
                {'word': 'parmesan', 'difficulty': 'hard', 'category': 'food'},
                {'word': 'prosciutto', 'difficulty': 'hard', 'category': 'food'},
                {'word': 'ravioli', 'difficulty': 'hard', 'category': 'food'},
                {'word': 'tiramisu', 'difficulty': 'hard', 'category': 'food'},
                {'word': 'zucchini', 'difficulty': 'hard', 'category': 'food'},

                # Sports (Easy)
                {'word': 'ball', 'difficulty': 'easy', 'category': 'sports'},
                {'word': 'race', 'difficulty': 'easy', 'category': 'sports'},
                {'word': 'team', 'difficulty': 'easy', 'category': 'sports'},
                {'word': 'goal', 'difficulty': 'easy', 'category': 'sports'},
                {'word': 'win', 'difficulty': 'easy', 'category': 'sports'},
                {'word': 'bat', 'difficulty': 'easy', 'category': 'sports'},
                {'word': 'game', 'difficulty': 'easy', 'category': 'sports'},
                {'word': 'jump', 'difficulty': 'easy', 'category': 'sports'},
                {'word': 'kick', 'difficulty': 'easy', 'category': 'sports'},
                {'word': 'pass', 'difficulty': 'easy', 'category': 'sports'},
                {'word': 'run', 'difficulty': 'easy', 'category': 'sports'},
                {'word': 'swim', 'difficulty': 'easy', 'category': 'sports'},
                {'word': 'throw', 'difficulty': 'easy', 'category': 'sports'},
                {'word': 'track', 'difficulty': 'easy', 'category': 'sports'},
                {'word': 'walk', 'difficulty': 'easy', 'category': 'sports'},

                # Sports (Medium)
                {'word': 'soccer', 'difficulty': 'medium', 'category': 'sports'},
                {'word': 'tennis', 'difficulty': 'medium', 'category': 'sports'},
                {'word': 'hockey', 'difficulty': 'medium', 'category': 'sports'},
                {'word': 'rugby', 'difficulty': 'medium', 'category': 'sports'},
                {'word': 'boxing', 'difficulty': 'medium', 'category': 'sports'},
                {'word': 'archer', 'difficulty': 'medium', 'category': 'sports'},
                {'word': 'cricket', 'difficulty': 'medium', 'category': 'sports'},
                {'word': 'diving', 'difficulty': 'medium', 'category': 'sports'},
                {'word': 'fencing', 'difficulty': 'medium', 'category': 'sports'},
                {'word': 'karate', 'difficulty': 'medium', 'category': 'sports'},
                {'word': 'rowing', 'difficulty': 'medium', 'category': 'sports'},
                {'word': 'skiing', 'difficulty': 'medium', 'category': 'sports'},
                {'word': 'surfing', 'difficulty': 'medium', 'category': 'sports'},
                {'word': 'cycling', 'difficulty': 'medium', 'category': 'sports'},
                {'word': 'running', 'difficulty': 'medium', 'category': 'sports'},

                # Sports (Hard)
                {'word': 'volleyball', 'difficulty': 'hard', 'category': 'sports'},
                {'word': 'basketball', 'difficulty': 'hard', 'category': 'sports'},
                {'word': 'badminton', 'difficulty': 'hard', 'category': 'sports'},
                {'word': 'wrestling', 'difficulty': 'hard', 'category': 'sports'},
                {'word': 'gymnastics', 'difficulty': 'hard', 'category': 'sports'},
                {'word': 'athletics', 'difficulty': 'hard', 'category': 'sports'},
                {'word': 'decathlon', 'difficulty': 'hard', 'category': 'sports'},
                {'word': 'marathon', 'difficulty': 'hard', 'category': 'sports'},
                {'word': 'pentathlon', 'difficulty': 'hard', 'category': 'sports'},
                {'word': 'taekwondo', 'difficulty': 'hard', 'category': 'sports'},
                {'word': 'triathlon', 'difficulty': 'hard', 'category': 'sports'},
                {'word': 'waterpolo', 'difficulty': 'hard', 'category': 'sports'},
                {'word': 'bobsleigh', 'difficulty': 'hard', 'category': 'sports'},
                {'word': 'snowboard', 'difficulty': 'hard', 'category': 'sports'},
                {'word': 'skateboard', 'difficulty': 'hard', 'category': 'sports'}
            ]

            for w in words:
                word = WordList(
                    word=w['word'],
                    difficulty=w['difficulty'],
                    category=w['category']
                )
                db.session.add(word)

        db.session.commit()
        print("Database initialized successfully!")

if __name__ == '__main__':
    init_db() 