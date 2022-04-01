import numpy as np
import wave
from scipy.io.wavfile import read, write
import struct
import scipy.signal as signal
import pyaudio
#import wavio

#def type_audio():
    #語音文件 shape、rate
    #wav_s = wavio.read("hello.wav")
    #print(wav_s)

def record_audio():
    #錄音
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1   #通道數
    RATE = 44100
    RECORD_SECONDS = 5  # 錄音時間
    WAVE_OUTPUT_FILENAME = "record.wav"
    
    p = pyaudio.PyAudio()
    stream = p.open(format = FORMAT, channels = CHANNELS,
                    rate = RATE, input = True,
                    frames_per_buffer = CHUNK)
    print("* recording")
    
    frames = []
    for i in range(0, int(RATE/CHUNK*RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)
        
    print("* done recording")
    
    stream.stop_stream()
    stream.close()
    p.terminate()
    
    wav = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wav.setnchannels(CHANNELS)
    wav.setsampwidth(p.get_sample_size(FORMAT))
    wav.setframerate(RATE)
    wav.writeframes(b''.join(frames))
    wav.close()

record_audio()
wav = wave.open( "record.wav", 'rb' )
num_channels = wav.getnchannels( )	# 通道數
sampwidth	 = wav.getsampwidth( )	# 樣本寬度
frequency	 = wav.getframerate( )	# 取樣頻率(Hz)
num_frames	 = wav.getnframes( )	# 音框數 = 樣本數
comptype	 = wav.getcomptype( )	# 壓縮型態
compname	 = wav.getcompname( )	# 無壓縮
wav.close( )

sampling_rate, x = read("record.wav")	# 輸入訊號


#file = "record echo.wav"	# 檔案名稱

amplitude = 20000           # 振幅
#frequency = 200				# 頻率(Hz)
duration = 10				# 時間長度(秒)
fs = 44100				   	# 取樣頻率(Hz)
num_samples = duration * fs	# 樣本數
 

b = np.array( [ 1 ] )
a = np.zeros( duration * fs )

num_echos = 5
for i in range( num_echos ):
	a[ int( i * fs * 5 / num_echos ) ] = 1 - i / num_echos

y = signal.lfilter( x, b, a )
y = np.clip( y, -30000, 30000 )

wav_file = wave.open( "record echo.wav", 'w' )
wav_file.setparams(( num_channels, sampwidth, fs, num_frames, comptype, compname )) 
for s in y :
   wav_file.writeframes( struct.pack( 'h', int ( s ) ) )

wav_file.close( ) 