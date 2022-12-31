# Loading .wav Files in Python

This repository brings some tips on loading .wav files in **Python**. 


## Tip #1 -- Choose the library

In this case, you can see different ways to open wav files.

- Access the **loading_wav_files.ipynb** jupyter notebook.

In this example, you can see how to use 4 different libraries.

#### Libraries:
- SoundFile [https://pysoundfile.readthedocs.io/en/latest/]
- Scipy [https://docs.scipy.org/doc/scipy/reference/generated/scipy.io.wavfile.read.html]
- Librosa [https://librosa.org/doc/latest/generated/librosa.load.html#librosa.load]
- Parselmouth [https://parselmouth.readthedocs.io/en/stable/index.html]

#### Libraries notes:
- **Soundfile**, **Librosa** and **Parselmouth** libraries have the input signal in the range [-1, 1]. On the other hand, **Scipy** library has the input signal in the range according to the digitalization level (e.g., 16 bits). Thus, for **Scipy**, we can define a normalization method (see the aforementioned jupyter notebook).
- For the **Librosa library**, if you do not specify the sampling rate, it will consider sr = 22050 Hz.

## Tip #2

In this case, you are interested in asking the user to put the file name. 

- Access the **loading1.py** file.
  
In this example, you can see four different ways to open the input file.

## Tip #3

In this case, you are interested in loading a sequence of files with a specific prefix word.  
- Access the **loading2.py** file and/or the **loading2.ipynb** jupyter notebook.
  
In this example, you can choose whether you or the user put the file name and the amount of files.

## Tip #4

In this case, you are interested in loading any **.wav** file from a folder.

- Access the **loading3.py** file and/or the **loading3.ipynb** jupyter notebook.



# Repository Notes

All **.wav** files in this repository are just examples of usage. You can apply to your own files.

## Acknowledgments

I would like to thank the developers of all the aforementioned libraries. It is important to note that all these libraries have a lot of other interesting functions. Feel free to access and explore them.
