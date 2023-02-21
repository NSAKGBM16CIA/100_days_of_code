# @your_gardener 11/02/23 Guess the song.
# session helps keep track and store date when user visits our page
import os
from flask import Flask , render_template , request , redirect , url_for , session , jsonify , flash
from flask_login import UserMixin , LoginManager , logout_user , login_required , login_user , current_user
from werkzeug.security import generate_password_hash , check_password_hash

from questions_manager import get_random_answers, get_random_song_db, get_highscores
from streampy import get_song_url
from user_manager import RegistrationForm, LoginForm

from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)
Bootstrap(app)



# SQLALCHEMY_TRACK_MODIFICATIONS adds significant overhead
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db/Users.db"

# set CSRF key which is required by flask (I am using a random key) OR PROVIDE BOTH LIKE
SECRET_KEY = os.urandom(32)
app.config.update(dict(
    SECRET_KEY=SECRET_KEY,
    WTF_CSRF_SECRET_KEY=f"crsf_{SECRET_KEY}"
))
# todo: UserWarning: Neither SQLALCHEMY_DATABASE_URI nor SQLALCHEMY_BINDS is set. Defaulting SQLALCHEMY_DATABASE_URI to "sqlite:///:memory:".

# db to store users, nationality, and score
class User(UserMixin,db.Model):
    __tablename__ = "players"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(32))
    country = db.Column(db.String(150))
    score = db.Column(db.Integer)
    emoji = db.Column(db.String(5))
# db.create_all()


# stuff to run
# @app.before_first_request
# def create_tables():
#     db.create_all()

# setup login manager
login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
#     get the id from db
    return User.query.get(user_id)


# the variables acting as the nuts
user_db = "db/Users.db"
question_bank = []
right_answer = ''
user_score = 0
game_level = 0
MAX_QUESTIONS = 3

# get the song and data
def get_new_song_data():
    db = "db/answers.db"
    table = 'songs_table'
    song_choice = get_random_song_db()

    return get_random_answers(database_file=db, table_name=table, song_choice=song_choice)


#get the lyric by level
def make_question(song_lyrics):
    global game_level
    if song_lyrics.startswith("featuring"):
        #         split once for the word, and split once for the first space
        parts = song_lyrics.split("featuring " , 1)
        song_lyrics = parts[1].split(' ', 1)[1].strip()

    lyrics = []
    if game_level == 1:
        for lyric in song_lyrics.split('\n')[:3]:
            if '\r' in lyric:
                lyric = lyric.replace('\r','')
            lyrics.append(lyric+'\n')
    if game_level == 2:
        for lyric in song_lyrics.split('\n')[:2]:
            if '\r' in lyric:
                lyric = lyric.replace('\r','')
            lyrics.append(lyric+'\n')
    if game_level == 3:
        for lyric in song_lyrics.split('\n')[:1]:
            if '\r' in lyric:
                lyric = lyric.replace('\r','')
            lyrics.append(lyric+'\n')
    return lyrics

# censor coarse songs
def is_clean_song(lyrics):
    dirty_words = ['fuck', 'sex', 'bitch', 'nigga', 'gay', 'shit', 'dick', 'pussy', 'fucking']
    for word in dirty_words:
        if word in lyrics:
            return False
    return True

# homepage
def load_new_question():
    global question_bank
    # max questions per session 10 true to proceed false to end
    if len(question_bank) == MAX_QUESTIONS:
        return False
        # data is returned as (right_answer , lyric , list of answers)
    song_data = get_new_song_data()
    # add clean songs and not added already
    if is_clean_song(song_data[1]):
        if song_data not in question_bank:
            question_bank.append(song_data)
    return True


@app.route('/', methods=['GET', 'POST'])
def home():

    global question_bank, game_level

    # print('home', session)
    # print(session['question_index'])
    if request.method == 'GET':
        # if level is 0 game is starting set question index to 0 [index_error]
        # if game_level == 0:
        # reset all the progress when starting
        # session['question_index'] = 0
        # user_score = 0
        reset_game()
        index = 1
        while index <= 2:
            # we call this function to add a new question to the question bank
            load_new_question()
            index += 1
        # print(question_bank)
        return render_template('welcome.html')
    else:
        # set level select from the button choice
        id = request.form.get('button_id')
        game_level = int(id)
        return redirect(url_for('play'))


# next question funtion
@app.route('/next')
def next_question():
    session['question_index'] += 1
    if load_new_question():
        return redirect(url_for('play'))
    else:
        # reset
        session['question_index'] = 0
        # register first if first time
        if current_user.is_anonymous:
            message = f'''
                          You got {user_score} points!!! 
                               '''
            link = 'register'
            return render_template('error.html' , message=message , link=link)
        return redirect(url_for('fame'))


#check answer
@app.route('/check_answer', methods=['POST'])
def check_answer():
    selected_answer = request.get_json()['selected_answer']
    # Check if the answer is correct
    is_correct = check_if_correct(selected_answer)
    score = get_score()
    right_answer = get_answer()
    return jsonify({'is_correct': is_correct, 'score': score, 'current_song':right_answer})


def check_if_correct(selected_answer):
    global user_score
    # logic to check if the answer is correct
    # print('selected ', selected_answer.lower(), 'right', right_answer.lower())

    if right_answer.lower() == selected_answer.lower():
        if game_level == 1:
            user_score = user_score + 10
        if game_level == 2:
            user_score = user_score + 20
        if game_level == 3:
            user_score = user_score + 30
        return True
    return False


# get user current score
def get_score():
    global user_score
    return user_score


# get current correct song
def get_answer():
    global right_answer
    return right_answer

# reset game
def reset_game():
    global question_bank, user_score, game_level
    question_bank = []
    user_score = 0
    game_level = 0
    session['question_index'] = 0



# play function
@app.route('/play', methods=['GET', 'POST'])
def play():
    global question_bank, right_answer, user_score
    try:
        # first time qeustion_index reset to 0
        if 'question_index' not in session:
            session['question_index'] = 0

        #     get current song
        current_question = question_bank[session['question_index']]
        # print(current_question)
        lyrics = make_question(current_question[1])
        answers = current_question[2]
        right_answer = current_question[0]

        # get song url
        song , singer = right_answer.split(' - ')[0], right_answer.split(' - ')[1]
        # print(song , singer)
        audio_url = get_song_url(song_title=f"{song}", artist_name=f"{singer}")
        # audio_url = '/Users/fb/Downloads/test.m4a'
        # print(audio_url)

    except ConnectionError:
        message = '''Oops! Your internet dropped
                     <p>Try again when re-connected.</p> 
                  '''
        link = 'home'
        reset_game()
        return render_template('error.html', message=message, link=link)

    except IndexError:
        message = "Game session not started"
        link = 'home'
        reset_game()
        return render_template('error.html', message=message, link=link)

    except Exception:
        message = '''Oops! Your internet dropped
                     <p>Try again when re-connected.</p> 
                  '''
        link = 'home'
        reset_game()
        return render_template('error.html', message=message, link=link)

    return render_template('game.html', lyrics=lyrics, answers=answers, audio_url=audio_url, score=user_score)


@app.route("/fame", methods=['GET'])
def fame():
    global user_score, user_db

    # update first is user is logged in
    if current_user.is_authenticated and not current_user.is_anonymous:
        user = User.query.filter_by(username=current_user.username).first()
        # update the user score in db
        prev_score = user.score
        user.score = prev_score + user_score
        # add fire emojis
        if user.score < 1000:
            user.emoji = '🔥'
        elif user.score < 2500:
            user.emoji = '🔥🔥'
        elif user.score < 10000:
            user.emoji = '🔥🔥🔥'
        elif user.score > 20000:
            user.emoji = '🔥🔥🔥🔥'
        elif user.score > 50000:
            user.emoji = '🔥🔥🔥🔥🔥'
        db.session.commit()

    # load other db scores to create the top-scorers chart regardless of user login profile
    top_players = get_highscores(user_db, 'players')

    return render_template('hall_of_fame.html', top_players=top_players)


@app.route("/about", methods=['GET'])
def about():
    return render_template('about_us.html')

@app.route("/register", methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        # get the data from the form
        username = form.username.data
        # hash and sal the password to secure it from hackers
        password = generate_password_hash(form.password.data,method="pbkdf2:sha256", salt_length=8)
        country = form.country.data

        # create a new user to put in a db
        new_user = User(
            username=username,
            password=password,
            country=country,
            score=0,
            emoji=''
        )
        # check if user already exists
        if User.query.filter_by(username=new_user.username).first():
            flash("Error: Username Exists! Try Logging in...")
            return redirect(url_for('login'))
        else:
            db.session.add(new_user)
            db.session.commit()
            flash('Registration Successful!')
            login_user(new_user)
            return redirect('fame')
    return render_template('register.html', form=form)


def save_score(user, user_score):
    try:
        # update the user score in db
        prev_score = user.score
        user.score = prev_score + user_score
        # add fire emojis
        if user.score < 1000:
            user.emoji = '🔥'
        elif user.score < 2500:
            user.emoji = '🔥🔥'
        elif user.score < 10000:
            user.emoji = '🔥🔥🔥'
        elif user.score > 20000:
            user.emoji = '🔥🔥🔥🔥'
        elif user.score > 50000:
            user.emoji = '🔥🔥🔥🔥🔥'
        db.session.commit()
        flash('Score Saved Successfully!')

    except Exception:
        message = '''Oops! We did not catch that!!
                           <p>Try logging in before playing.</p> 
                        '''
        link = 'home'
        reset_game()
        return render_template('error.html' , message=message , link=link)


@app.route("/login", methods=['GET','POST'])
def login():
    global question_bank , MAX_QUESTIONS, user_score

    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        user = User.query.filter_by(username=username).first()
        if user:
            if check_password_hash(user.password, password):
                login_user(user)
                # check if user has a pending score and save
                if len(question_bank) == MAX_QUESTIONS and user_score > 0:
                    save_score(user, user_score)
                    return redirect(url_for('fame'))
            return redirect(url_for('home'))
    return render_template('login.html', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logged out!')
    reset_game()
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, debug=True)

