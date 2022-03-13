from aip import AipSpeech

""" 你的 APPID AK SK """
APP_ID = '24988009'
API_KEY = '8evPUvT6ZEz0yTWHhbX1nHCB'
SECRET_KEY = 'qYl2sA34ftaq4l7ZSvV2FiRG0AEarRVG'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
outfile = 'demo.txt'
audio_file = 'save.wav'

    # 读取文件
def get_file_content(audio_file):
    with open(audio_file, 'rb') as fp:
        return fp.read()


 #   result = client.asr(get_file_content('save.wav'), 'pcm', 16000, {
#      'dev_pid': 1537,
 #   })
    #print(result['err_no'])

    #print(result['result'][0])
def get_text():
    # 识别本地语音文件
    result = client.asr(get_file_content(audio_file), 'wav', 16000, {'dev_pid': 1537,})
    print(result['err_msg'])
    text = result['result'][0]
    #保存为文本文件
    f = open("demo.txt", 'w', encoding='utf-8')
    f.write(text)
    return text


res = get_text()
print (res)



