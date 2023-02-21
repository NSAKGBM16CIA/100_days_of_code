# this module is to explore and pull data from the database

import sqlite3
import random
from sqlalchemy import create_engine
import pandas as pd

def get_random_song_db():
    conn = sqlite3.connect("db/questions.db")
    engine = create_engine(f"sqlite:///db/questions.db", echo=False)

    # read sql to df
    df = pd.read_sql_table('songs_table', con=engine)

    index = random.randint(0, len(df) - 1)
    question = df.iloc[index]
    # print(question)
    song = (question.Artist, question.Song, question.Lyrics)
    return song


def get_random_answers(database_file, table_name, song_choice):
    """
    :param database_file: lyrics.db
    :param table_name: lyrics is the table name inside db, lol obvious naming
    :param song_choice: a random song from the textfile list of billboard top 20 since 1997
    :return: a tupple (right answer, lyric, and [answers]
    """
    conn = sqlite3.connect(database_file)
    cursor = conn.cursor()

    # Get the number of rows in the table
    cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
    num_rows = cursor.fetchone()[0] #same as len(db)

    # Concatenate the values from the song choice columns for the right answer
    right_answer = f"{song_choice[0]} - {song_choice[1]}"
    # print(right_answer)
    lyric = f"{song_choice[2]}"

    # Pick 3 random rows that are not the right answer
    random_rows = random.sample(range(1, num_rows + 1), 3)
    random_rows = [row for row in random_rows if row != song_choice[0]]

    answers = []
    while True:
        if len(answers) == 3:
                break
        for i, random_row in enumerate(random_rows):
            # Get the data for the random row
            cursor.execute(f"SELECT * FROM {table_name} LIMIT 1 OFFSET {random_row - 1}")
            random_entry = cursor.fetchone()
            # print(random_entry)
            # Concatenate the values from the first and third columns
            answer = f"{random_entry[1]} - {random_entry[2]}"
            if answer not in answers and answer != right_answer:
                answers.append(answer)

    # after random picking we plug in the right_ans randomly as well lol which i think is not necessary,
    answers.insert(random.randint(0, 3), right_answer)
    # shuffle twice just for emphasis
    random.shuffle(answers)
    random.shuffle(answers)

    return (right_answer, lyric, answers)

# get all the scores
# def get_highscores(db, table_name):
#     '''
#     :param db: database (db file)
#     :param table_name: the name within the db
#     :return: the top 50 entries by score
#     '''
#
#     conn = sqlite3.connect(db)
#     cur = conn.cursor()
#
#     # get all scores and sort descending and grab the top 50
#     query = f"SELECT * FROM {table_name} ORDER BY score DESC"
#     all_scores = cur.execute(query)
#
#     # Get the number of rows in the table
#     cur.execute(f"SELECT COUNT(*) FROM {table_name}")
#     num_rows = cur.fetchone()[0]
#     if num_rows > 50:
#         top_50 = all_scores.fetchmany(50)
#     else:
#         top_50 = all_scores.fetchmany(num_rows)
#     print(num_rows, all_scores, top_50)
#     for p in top_50:
#         print(p)
#         print(p[1],p[0],p[2],p[3])
#     return top_50



def get_highscores(db, table_name):
    '''
    :param db: database (db file)
    :param table_name: the name within the db
    :return: the top 50 entries by score
    '''

    conn = sqlite3.connect(db)
    cur = conn.cursor()

    query = f"SELECT * FROM {table_name} ORDER BY score DESC LIMIT 50"
    all_scores = cur.execute(query).fetchall()

    # for row in all_scores:
    #     print(row[1])
    conn.close()
    return all_scores
