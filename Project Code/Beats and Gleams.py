import alsaaudio as aa 
import wave 
from struct import unpack 
import numpy as np 
from sense_hat import SenseHat 
 
wavfile = wave.open('test.wav') 
sample_rate = wavfile.getframerate() 
no_channels = wavfile.getnchannels() 
 
s= SenseHat() 
s.low_light = True 
 
chunk = 4096 
 
matrix = [0] * 8 
 
weighting = [0]*8 
weighting[0] = 2 
power = [] 
 
for i in range(7): 
        if i%2==0: 
                weighting[i+1] = 2**(2+i) 
        else: 
                weighting[i+1] = 2**(1+i) 
 
output = aa.PCM(aa.PCM_PLAYBACK,aa.PCM_NORMAL) 
output.setchannels(2) 
output.setrate(sample_rate) 
output.setformat(aa.PCM_FORMAT_S16_LE) 
output.setperiodsize(chunk) 
 
def piff(val): 
        return int(2*chunk*val/sample_rate) 
         
def calculate_levels(data, chunk, sample_rate): 
        data = unpack("%dh"%(len(data)/2),data) 
        data = np.array(data,dtype='h') 
        fourier = np.fft.rfft(data) 
        fourier = np.delete(fourier,len(fourier)-1) 
        power = np.log10(np.abs(fourier))**2 
        power = np.reshape(power,(8,chunk/8)) 
        matrix = np.int_(np.average(power,axis=1)) 
        return matrix 
 
data = wavfile.readframes(chunk) 
while data != '': 
        output.write(data) 
        matrix = calculate_levels(data,chunk,sample_rate) 
        s.clear(0,0,0) 
        for y in range(0,8): 
                for x in range(matrix[y]): 
                        x = int(x/4.7) 
                        print(x) 
                        if x < 4: 
                                s.set_pixel(y,x,0,200,0) 
                                if(x > 0): 
                                        s.set_pixel(y,x-1,0,200,0) 
                        elif x < 6: 
                                s.set_pixel(y,x,150,150,0) 
                                s.set_pixel(y,x-1,150,150,0) 
                        else:                              
                                s.set_pixel(y,x,200,0,0) 
                                s.set_pixel(y,x-1,200,0,0)  
         
        data = wavfile.readframes(chunk)
