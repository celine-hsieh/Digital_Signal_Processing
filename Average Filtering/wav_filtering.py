import numpy as np
import wave
from scipy.io.wavfile import read, write
import struct
import scipy.signal as signal
import matplotlib.pyplot as plt

def average_filtering( x, filter_size ):
	h = np.ones( filter_size ) / filter_size
	y = np.convolve( x, h, 'same' )
	return y
	
def gaussian_filtering( x, sigma):
	filter_size = 6 * sigma + 1  
	gauss = signal.gaussian( filter_size, sigma )	
	sum = np.sum( gauss )
	gauss = gauss / sum
	y = np.convolve( x, gauss, 'same' )
	return y
	
def normalization( x ):
	x_abs = abs( x )
	max_value = max( x_abs )
	y = x / max_value * 2000	#正規化數值乘上2000倍
	return y
	
def main( ):
	# ----------------------------------------------------
	#  輸入模組
	# ----------------------------------------------------	
	wav = wave.open( "0929_1.wav", 'rb' )
	num_channels = wav.getnchannels( )	# 通道數
	sampwidth	 = wav.getsampwidth( )	# 樣本寬度
	fs			 = wav.getframerate( )	# 取樣頻率(Hz)
	num_frames	 = wav.getnframes( )	# 音框數 = 樣本數
	comptype	 = wav.getcomptype( )	# 壓縮型態
	compname	 = wav.getcompname( )	# 無壓縮
	wav.close( )

	sampling_rate, x = read("0929_1.wav")	# 輸入訊號

	# ----------------------------------------------------
	#  DSP 模組
	# ----------------------------------------------------	
	print( "Gaussian Filtering" )
	sigma = 5
	y = gaussian_filtering( x, sigma )

	# ----------------------------------------------------
	#  輸出模組
	# ----------------------------------------------------		
	wav_file = wave.open("N76101012.wav", 'w' )
	wav_file.setparams(( num_channels, sampwidth, fs, num_frames, comptype, compname )) 

	for s in y:
		wav_file.writeframes( struct.pack( 'h', int ( s ) ) )
	wav_file.close( ) 

	# ----------------------------------------------------
	#  輸出高斯濾波後數值
	# ----------------------------------------------------	
	var = ','.join(str(i) for i in y)
	#var = y
	with open('npN76101012.txt','w') as f:
		f.write(var)

	# ----------------------------------------------------
	#  儲存正規化後數值圖片
	# ----------------------------------------------------	
	y = normalization( x )
	plt.figure(2)
	plt.plot(y)
	plt.xlabel('non_frames')
	plt.ylabel('value')

	plt.savefig ('正規化後數值.png')
	plt.show()
	
main( )