# from pydub import AudioSegment
# from pydub.playback import play
import requests
import os
from dotenv import load_dotenv

load_dotenv()
#get preview of song title and artist of the song

def get_song_url(song_title, artist_name):

    url = os.getenv('STREAM_URL')
    params = {'term' : f'{song_title} {artist_name}', 'entity' : 'musicTrack', 'media' : 'music'}
    # try:
    response = requests.get(url=url, params=params)
    data = response.json()['results']
    # print(data)
    # except Exception:
    #     message = '''Oops! Your internet dropped
    #                  <p>Try again when re-connected.</p>
    #               '''
    #     link = 'home'
    #     return render_template('error.html', message=message, link=link)

    # orginally wanted to be sure on both the name and song but there are some small differences at times so commenting out
    # for d in data:
    #     print(d)
    #     if song_title in d['trackName'].lower() or artist_name in d['artistName']:
    #         song_url = f"{d['previewUrl']}"
    #         print(song_url)
    #         return song_url
    # just taking the first result now
    song_url = data[0]['previewUrl']
    return song_url

# get_song_url(song_title="i don't want to miss a thing", artist_name='mark chesnutt')