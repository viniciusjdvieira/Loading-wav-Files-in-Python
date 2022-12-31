import glob
import numpy as np
import soundfile as sf


path = './arbritary-wav-files/'
files = glob.glob(path+'*.wav')
amnt_files = len(files)

for i in np.arange(amnt_files):
    file_in = files[i]
    name_file = file_in.split('\\')[1]
    print('Openning file...', file_in)
    data_sf, sr_sf = sf.read(file_in)
    duration_sf = len(data_sf)/sr_sf # for information
    print('File: %s \nSampling Rate: %d Hz \nDuration: %4.4f s \n\n' % (name_file, sr_sf, duration_sf))  
