import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile as wf
import librosa as rosa
import soundfile as sf
import parselmouth as pm


filename = input('Type the name of the .wav file: ')

# ---- Using soundfile ---- #
data_sf, samplerate_sf = sf.read(filename+'.wav') # reading the file
duration_sf = len(data_sf)/samplerate_sf          # for information
max_sf = max(data_sf)  # taking the maximum value of the signal
min_sf = min(data_sf)  # taking the minimum value of the signal
## --- informations about the file:
print('----> SoundFile <----')
print('By using the SoundFile lib, we have:')
print('File: %s \nSampling Rate: %d Hz \nDuration: %4.4f s \nRange: [%4.4f , %4.4f]\n\n' % (filename, samplerate_sf, duration_sf, min_sf, max_sf))  


# ---- Using scipy ---- #
samplerate_wf, data_wf  = wf.read(filename+'.wav') # reading the file
duration_wf = len(data_wf)/samplerate_wf          # for information
max_wf = max(data_wf)  # taking the maximum value of the signal
min_wf = min(data_wf)  # taking the minimum value of the signal
## --- informations about the file:
print('----> Scipy <----')
print('By using the Scipy lib, we have:')
print('File: %s \nSampling Rate: %d Hz \nDuration: %4.4f s \nRange: [%4.4f , %4.4f]\n' % (filename, samplerate_wf, duration_wf, min_wf, max_wf))  
## normalizing between [-1 , 1]:
scale_factor = (2**15)-1 # assuming  16 bits of digitalization
data_wf_norm = data_wf/scale_factor
max_wf_norm = max(data_wf_norm)  # taking the maximum value of the normalized signal
min_wf_norm = min(data_wf_norm)  # taking the minimum value of the normalized signal
print('----> Scipy, with normalization <----')
print('Normalized Range: [%4.4f , %4.4f]\n\n' % (min_wf_norm, max_wf_norm))  


# ---- Using librosa ---- #
data_rosa, samplerate_rosa = rosa.load(filename+'.wav', sr=11025) # reading the file
duration_rosa = len(data_rosa)/samplerate_rosa          # for information
max_rosa = max(data_rosa)  # taking the maximum value of the signal
min_rosa = min(data_rosa)  # taking the minimum value of the signal
## --- informations about the file:
print('----> Librosa <----')
print('By using the Librosa lib, we have:')
print('File: %s \nSampling Rate: %d Hz \nDuration: %4.4f s \nRange: [%4.4f , %4.4f]\n\n' % (filename, samplerate_rosa, duration_rosa, min_rosa, max_rosa))  


# ---- Using parselmouth ---- #
sound_pm = pm.Sound(filename+'.wav') # reading the file
data_pm = sound_pm.values
samplerate_pm = int(sound_pm.sampling_frequency)
duration_pm = len(data_pm[0])/samplerate_pm   # for information
max_pm = max(data_pm[0])  # taking the maximum value of the signal
min_pm = min(data_pm[0])  # taking the minimum value of the signal
## --- informations about the file:
print('----> ParselMouth <----')
print('By using the ParselMouth lib, we have:')
print('File: %s \nSampling Rate: %d Hz \nDuration: %4.4f s \nRange: [%4.4f , %4.4f]\n\n' % (filename, samplerate_pm, duration_pm, min_pm, max_pm))  
