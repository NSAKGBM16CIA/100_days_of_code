"""
collb project with Abi
slate: pdf to text
gtts : google translate speech engine
playsound : plays audio files
os : path setting and saving files
flask : for web version of the app
pyttsx3: offline speech engime like gtts offline version
"""

import os
import requests
import slate
import fitz #$ pip install pymupdf
import gtts
from playsound import playsound
import pyttsx3
from flask import Flask , render_template, redirect, request, url_for, send_from_directory
from werkzeug.utils import secure_filename
from glob import glob

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['DOWNLOAD_FOLDER'] = 'downloads'
book_path = ""

# the state are converted to audio and read to the user to let them know what process is running currently
state = ["welcome, please upload your pdf file, preferably with text only",
         "we are uploading your book, it should be ready to start converting in a minute",
         "We are converting the text into audio. This may take time depending on the size of your book",
         "Conversion complete! you may click download to save audio file"
         ]

def say_state(state):
#     try to say it online using gtts if offline say it using pyttsx3
    try:
        reader = gtts.gTTS(text=state, lang='en' , slow=False)
        sound = reader.save(os.path.join(app.config['DOWNLOAD_FOLDER'] , 'state.mp3'))
        playsound(sound)
    except Exception:
        engine = pyttsx3.init()
        engine.save_to_file(state , os.path.join(app.config['DOWNLOAD_FOLDER'] , 'state.mp3'))
        engine.say(os.path.join(app.config['DOWNLOAD_FOLDER'] , 'state.mp3'))
        engine.runAndWait()
        engine.endLoop()
#       todo//: having issues with ending this loop in order to play other states


@app.route('/', methods=['GET','POST'])
def home():
    # os.path.join(app.config['UPLOAD_FOLDER'] , '*.pdf'
    # functionality of uploding and reading the files should happen on the first page of the homepage
    say_state(state[0])
    if request.method == 'POST':
        print("post")
        try:
            say_state(state[1])
            pdf_file = request.files['pdf_file']
            filename = secure_filename(pdf_file.filename)

            print(pdf_file.filename)
            if pdf_file.filename != '':
                pdf_file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                book_path = pdf_file.filename
                make_thumbnail(book_path)
        except Exception:
            print("Got a thumbnail issue...")
            #proceed if thumbnail cant be made
        return redirect(url_for('home'))
    return render_template('index.html')

@app.route("/open_book")
def open_pdf():
    # TODO:// I do not want this function to open a new tab/route Everything should happen on the single page
    say_state(state[2])
    pattern = os.path.join(app.config['UPLOAD_FOLDER'], '*.pdf')
    last_file = sorted(glob(pathname=pattern))[-1]
    print(last_file)
    with open(last_file, 'rb') as file:
        text = slate.PDF(file)
    # if there is internet connection read online
    if requests.get('https://google.com').state == 200:
        read_online(text)
    else:  #ConnectionError
        read_offline(text)
    say_state(state[3])
    
    return redirect(url_for('home'))

def make_thumbnail(book_path):
    # fitz converts pages to images we use the first image as thumbnail
    # TODO: Check if a new image is generated everytime a pdf is created
    pdf_file = os.path.join(app.config['UPLOAD_FOLDER'],book_path)
    print('pdf file', pdf_file)
    images = fitz.open(pdf_file)
    print(len(images))
    if len(images) > 0:
        img = images[0].get_pixmap()
        img.save("static/images/cover.jpg")
    return redirect(url_for('home'))


def read_online(page):
    # google engine

    reader = gtts.gTTS(text=page, lang='en', slow=False)
    reader.save(os.path.join(app.config['DOWNLOAD_FOLDER'],'test.mp3'))
    playsound('test.mp3')

def read_offline(book):
    # pyttsx3 engine
    # we just try to read the last page
    page = book[-1]
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    # page = "This is sample text"
    engine.save_to_file(page,os.path.join(app.config['DOWNLOAD_FOLDER'],'test.mp3'))
    engine.say(os.path.join(app.config['DOWNLOAD_FOLDER'],'test.mp3'))
    engine.runAndWait()
    engine.endLoop()
    return redirect(url_for('home'))


@app.route("/download")
def download(methods=['GET']):
    # TODO:// check if downloads tab working and 3 more to dos in the index html file
    send_from_directory(os.path.join(app.config['DOWNLOAD_FOLDER'],'test.mp3'))


if __name__ == '__main__':
    app.run(debug=True)
