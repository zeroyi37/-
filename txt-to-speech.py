from aip import AipSpeech
from playsound import playsound
from pydub import AudioSegment
from pydub.playback import play

""" 你的 APPID AK SK """
APP_ID = '25013414'
API_KEY = 'A78F8aswrTceMOh5tT0ItMdj'
SECRET_KEY = 'ZSUGYxvg0KbEC574Z8OkyjjeH3V2yVUR'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
infile = 'demo.txt'

#读取文件
with open(infile, 'r', encoding='utf-8') as f:
    content_s = f.read()
    #print(content_s)
result = client.synthesis(content_s, 'zh', 1, {
    'vol': 5,
    'spd': 3,
    'pit': 6,
    'per': 4,
})

#转女音并保存
if not isinstance(result, dict):
    with open('auido.mp3', 'wb') as f:
        f.write(result)
#print(result['err_msg'])

#播放
playsound("auido.mp3")