import pyaudio
import wave
def LuYin():
    CHUNK = 1024              #wav文件是由若干个CHUNK组成的，CHUNK我们就理解成数据包或者数据片段。
    FORMAT = pyaudio.paInt16  #使用量化位数 16位来进行录音。
    CHANNELS = 1              #单声道。
    RATE = 16000              # 采样率16k
    RECORD_SECONDS = 10     #采样时间
    WAVE_OUTPUT_FILENAME = "test.wav"   #输出文件名

    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    print("* 录音开始")

    frames = []

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    print("* 录音结束")

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()

LuYin()