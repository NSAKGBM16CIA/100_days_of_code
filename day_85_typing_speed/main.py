
# FOR BACKSPACE functionality
from tkinter import END

from pynput.keyboard import Key, Controller
# measure time to determine speed
from datetime import datetime as dt , timedelta

"""
for multi threading we could use Ray and the @remote decorator ray.int() ray.get([func1.remote()])
or we could import Thread from threading, if name == main, Thread(target = func1).start() 
import threading and chain Timer this bad news
"""
# import ray
# from threading import Thread
# import threading
# import thread
import time

# dictionary words
wordlist = ''
# typed sentence
# sentence = ''
start_time = dt.now()
end_time = start_time + timedelta(minutes=1)
timer = 60

def load_words():
    global wordlist
    with open('data/english_wordlist.txt', 'r') as file:
        words = file.read()
        wordlist = [word.lower() for word in words.split("\n")]
        print(f"Loaded {wordlist[0]} to {wordlist[-1]}")
        return wordlist

# @ray.remote
# TODO :// After every 2-3 secondes check if the the tying stopped and prass backspace twice
def check_activity(entry):
    print("checking...")
    last_sentence = entry.get('1.0' , END)
    # threading.Timer(5, check_activity(entry)).start()
    time.sleep(3)
    new_sentence = entry.get('1.0', END)
    if last_sentence == new_sentence:
        line = entry.get('1.0', END)[:-1]
        entry.delete('1.0', END)
        entry.insert(END, line)


def countdown(window):
    # TODO: add timer functionality
    global timer
    timer = window.after(1000, countdown(window), timer-1)
    if timer == 0:
        window.after_cancel(timer)



def start_timer():
    global start_time
    global end_time
    # get current time and add a minute
    start_time = dt.now()
    end_time = start_time + timedelta(minutes=1)



def get_text(entry):
    global sentence
    # pass the starting point this is passed as a string '1.0' in text widget not int 0 as other widget
    sentence = entry.get('1.0', END)
    # print(sentence)
    # ray.init()
    # ray.get([check_activity(entry)])
    # if __name__ == '__main__':
    # Thread(target=check_activity(entry)).start()
    # print('started')
    # Thread(target=check_activity(entry)).start()
    check_word(entry, sentence)

def delete_word(entry, start, end):
    entry.delete(start, end)

def backspace():
    kb = Controller()
    kb.press(Key.backspace)
    kb.release(Key.backspace)
    print('backspace')

def check_word(entry, sentence):

    words = sentence.strip().split(" ")
    print(f"before check : {words}")

    # test complete then return (test complete! is inserted when the test is complete)
    if words[-1] =='COMPLETE!':
        return

    new_word = words[-1].lower()

    # handle punctuations
    punc_marks = ["'", ".", ",", "/", ":", ";", ">", "<", "!", "@", "?", '"', "'s"]
    for mark in punc_marks:
        if mark in new_word:
            new_word = new_word.replace(mark, '')

    print(new_word)
    if new_word in wordlist:
        print("Got the word")
        print(new_word)
    else:
        print("Bad word")
        # delete the word and one space
        try:
            delete_word(entry, f'1.{sentence.index(new_word)-1}', f'1.{sentence.index(new_word)+len(new_word)}')
        except IndexError:
            delete_word(entry, f'1.{sentence.index(new_word)}', f'1.{sentence.index(new_word) + len(new_word)}')


def measure_speed():
    # this function will be called at the end of a minute or at intervals
    global sentence
    speed = len(sentence) / 5
    return f"Final Result: {speed} Words per Minute!"

