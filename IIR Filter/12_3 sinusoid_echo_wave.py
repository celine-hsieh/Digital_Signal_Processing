import numpy as np
import wave
from scipy.io.wavfile import read, write
import struct
import scipy.signal as signal

wav = wave.open( "hello.wav", 'rb' )
num_channels = wav.getnchannels( )	# 通道數
sampwidth	 = wav.getsampwidth( )	# 樣本寬度
frequency	 = wav.getframerate( )	# 取樣頻率(Hz)
num_frames	 = wav.getnframes( )	# 音框數 = 樣本數
comptype	 = wav.getcomptype( )	# 壓縮型態
compname	 = wav.getcompname( )	# 無壓縮
wav.close( )

sampling_rate, x = read("hello.wav")	# 輸入訊號


file = "hello echo.wav"	# 檔案名稱

amplitude = 20000           # 振幅
#frequency = 200				# 頻率(Hz)
duration = 10				# 時間長度(秒)
fs = 44100				   	# 取樣頻率(Hz)
num_samples = duration * fs	# 樣本數
 
#num_channels = 1			# 通道數
#sampwidth = 2				# 樣本寬度
#num_frames = num_samples	# 音框數 = 樣本數
#comptype = "NONE"		   	# 壓縮型態
#compname = "not compressed" # 無壓縮

#t = np.linspace( 0, 1, fs, endpoint = False )
#x = np.exp( -t ) * amplitude * np.sin( 2 * np.pi * frequency * t )
#x = np.pad( x, ( 0, 4 * fs ), 'constant' )

b = np.array( [ 1 ] )
a = np.zeros( duration * fs )

num_echos = 5
for i in range( num_echos ):
	a[ int( i * fs * 5 / num_echos ) ] = 1 - i / num_echos

y = signal.lfilter( x, b, a )
y = np.clip( y, -30000, 30000 )

wav_file = wave.open( "hello echo(b).wav", 'w' )
wav_file.setparams(( num_channels, sampwidth, fs, num_frames, comptype, compname )) 

for s in y :
   wav_file.writeframes( struct.pack( 'h', int ( s ) ) )

wav_file.close( ) 


b = np.array( [ 1 ] )
a = np.zeros( duration * fs )

num_echos = 10
for i in range( num_echos ):
	a[ int( i * fs * 5 / num_echos ) ] = 1 - i / num_echos

y = signal.lfilter( x, b, a )
y = np.clip( y, -30000, 30000 )

wav_file = wave.open( "hello echo(c).wav", 'w' )
wav_file.setparams(( num_channels, sampwidth, fs, num_frames, comptype, compname )) 

for s in y :
   wav_file.writeframes( struct.pack( 'h', int ( s ) ) )

wav_file.close( ) 