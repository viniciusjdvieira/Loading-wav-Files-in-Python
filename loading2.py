import numpy as np
import soundfile as sf

amnt_sf = 10
prefix_word = 'ang'
path = './sequenced-wav-files/'

for i in np.arange(amnt_sf):
    file_in = path+prefix_word+str(i+1)+'.wav'
    print('Openning file...', file_in)
    data_sf, sr_sf = sf.read(file_in)
    duration_sf = len(data_sf)/sr_sf # for information
    print('File: %s \nSampling Rate: %d Hz \nDuration: %4.4f s \n\n' % (prefix_word+str(i+1), sr_sf, duration_sf))  