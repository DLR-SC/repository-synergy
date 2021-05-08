- README.md : [[ English ](README.md)]  [[ 한국어 ](README_kor.md)]
- Homepage : [[ Korean Only (한국어) ]](http://jamonglab.com/computer_music/?utm_source=github&utm_medium=link_click&utm_campaign=deeplearning&utm_term=music-rnn&utm_content=README.md_01) 

music-rnn
========
Machine Learning / Deep Learning with RNN(LSTM, JZS1) - Compose Music, Waltz
>
- After training with notes information of midi files of Data Set,
- machine will compose simple trained style music.
- This Project is composed of simple python codes to do above process.

Composing simple music with Machine Learning / Deep Learning
--------
>
- Even if you don`t have prior knowledge of Deep Learning,
- as you modify and test following the **python codes** and the **dependencies in below**,
- without knowledge of mathematics,
- basically you can experience glimpse of Deep Learning in python.



Dependencies
--------
### OpenBLAS
- an optimized BLAS(Basic Linear Algebra subroutines) library based on [GotoBLAS2](https://www.tacc.utexas.edu/research-development/tacc-software/gotoblas2) 1.13 BSD version.
- Requires NumPy
- **gfortran** is required before installing OpenBLAS
- http://www.openblas.net/
- https://github.com/xianyi/OpenBLAS/wiki

### NumPy
- NumPy is the fundamental package for scientific computing with Python.
  * a powerful N-dimensional array object
  * sophisticated (broadcasting) functions
  * tools for integrating C/C++ and Fortran code
  * useful linear algebra, Fourier transform, and random number capabilities
- Normally used with SciPy in combination
- http://www.numpy.org/

### SciPy
- http://www.scipy.org/

### Theano
- Theano is a Python library that allows you to define, optimize, and evaluate mathematical expressions involving multi-dimensional arrays efficiently.
  * tight integration with NumPy – Use numpy.ndarray in Theano-compiled functions.
  * transparent use of a GPU – Perform data-intensive calculations up to 140x faster than with CPU.(float32 only)
  * efficient symbolic differentiation – Theano does your derivatives for function with one or many inputs.
  * speed and stability optimizations – Get the right answer for log(1+x) even when x is really tiny.
  * dynamic C code generation – Evaluate expressions faster.
  * extensive unit-testing and self-verification – Detect and diagnose many types of mistake.
- http://deeplearning.net/software/theano/#

### Keras
- Neural Network Library (by Python)
- Keras is a minimalist, highly modular neural network library in the spirit of Torch, written in Python, that uses Theano under the hood for optimized tensor manipulation on GPU and CPU.
- https://github.com/fchollet/keras
- http://keras.io/

### UnRoll
- Zulko made this library.
- Unroll is a Python module for the transcription of piano rolls to sheet music.
- It can transcribe from a MIDI file or from a video of a piano roll. It finds the notes, the tempo, roughly separates the hands, and writes the result in a Lilypond file.
- http://zulko.github.io/blog/2014/02/12/transcribing-piano-rolls/
- http://zulko.github.io/unroll/
- https://github.com/Zulko/unroll

### music21
- a toolkit for computer-aided musicology (MIT)
- http://web.mit.edu/music21/
- http://web.mit.edu/music21/doc/index.html



Data Set for Train / Test
--------
### Modeling Temporal Dependencies in High-Dimensional Sequences: Application to Polyphonic Music Generation and Transcription
- http://www-etud.iro.umontreal.ca/~boulanni/icml2012
- Above midi files data set was used to train and test.
- If you want to train with above Data Set directly, please refer **Usage : Change Data Set** below


Usage
--------
### Data Set, Source Code Structure
```
music-rnn
├── README.md
└── rnn_lstm_jzs1_eng
    ├── data
    │   ├── JSB Chorales
    │   │   ├── test
    │   │   ├── train
    │   │   └── valid
    │   ├── MuseData
    │   │   ├── test
    │   │   ├── train
    │   │   └── valid
    │   ├── Nottingham
    │   │   ├── test
    │   │   ├── train
    │   │   └── valid
    │   └── Piano-midi.de
    │       ├── test
    │       ├── train
    │       └── valid
    ├── data_for_train
    │   └── waltzes
    │       ├── waltzes_simple_chords_1.mid
    │       ├── waltzes_simple_chords_2.mid
    │       ├── waltzes_simple_chords_3.mid
    │       ├── waltzes_simple_chords_6.mid
    │       └── waltzes_simple_chords_7.mid
    ├── predict_Waltzes
    ├── predMidi_Waltzes
    │   └── bach_lstm_pred_midi_2015.11.11.15:32:34.mid
    ├── wts_Waltzes
    │   └── train_piano_wts_seq_model_2015.11.11.23:52:29.wts
    ├── __init__.py
    ├── data_init.py
    ├── model_util.py
    ├── train_piano.py
    └── readme.md 

```


### Basic Usage
- when executing train_piano.py with Python Compiler
  * /music-rnn/rnn_lstm_jzs1_eng/wts_Waltzes/train_piano_wts_seq_model_2015.11.11.23:52:29.wt
  * LSTM(Long Short Term Memory) training model will load above weights file
  * next, start training with 5 midi files in music-rnn/rnn_lstm_jzs1_eng/data_for_train/waltzes

```python
$ git clone https://github.com/jamonglab/music-rnn.git
$ cd music-rnn
$ python train_piano.py
```
- use command **git clone(copy)**, download(clone) music-rnn project
- move to directory, music-rnn project downloaded
- execute train_piano.py
  
  * directory to save composed waltz (midi format)
    * in source code of train_piano.py
    ```
    if iteration % 10 == 0:
    ```
    * during training, prediction is processed at every 10th iteration
    * after prediction, it composes new waltz with using calculated weights.
    ```
    DIR_PREDICTED_MIDI = "./predMidi_Waltzes/"          # save predicted(created) midi file
    ```
    * and new waltz will be saved at /predMidi_Waltzes automatically.

### Creating weights file / Using other weights file
- If you don`t edit any source code of this project, train_piano.py will load weights file(see below source code) and apply it to Training Model.
```python
# load automatically : load weights which is containing the latest weights infomation
try:
    wts_list = os.listdir(DIR_WEIGHTS)
    if len(wts_list) != 0:
        wts_list.sort()
        model.load_weights(DIR_WEIGHTS + wts_list[-1])
        print "\n...... Loaded weights file : {0} ......".format(wts_list[-1])
except:
    pass

# # load passively
# #
# # waltzes wts file ==> loss: 1.5240 - acc: 0.3573
# # ./wts_Waltzes/train_piano_wts_seq_model_2015.11.11.23:52:29.wts
# filename_wts = "train_piano_wts_seq_model_2015.11.11.23:52:29.wts"
# try:
#     model.load_weights(DIR_WEIGHTS + filename_wts)
#     print "\n... Loaded weights file : {0} ...".format(filename_wts)
# except:
#     pass
```
- Creating weights file
  * delete music-rnn/rnn_lstm_jzs1_eng/wts_Waltzes/train_piano_wts_seq_model_2015.11.11.23:52:29.wts file
  * or move above file to another path
  * just follow above **Basic Usage**
- Using other weights file
  * (see above source codes) comment **load automatically block**, and uncomment **load passively block**,
  * next, move other weights file that you want to use for train to DIR_WEIGHTS directory,
  * write the weights file name to **filename_wts = "other_file_name"**,
  * follow above **Basic Usage**

### Change Data Set
- In case of using Data set of Modeling Temporal Dependencies in High-Dimensional Sequences as in this source,
- http://www-etud.iro.umontreal.ca/~boulanni/icml2012
- move to above link, and download below Source files (4 files)
  - Piano-midi.de1 : Source (124 files, 951 KB) or Piano-roll (7.1 MB)
  - Nottingham2 : Source (1037 files, 676.1 KB) or Piano-roll (23.2 MB)
  - MuseData3 : Source (783 files, 3.0 MB) or Piano-roll (30.1 MB)
  - JSB Chorales : Source (382 files, 210 KB) or Piano-roll (2.0 MB)
- extract downloaded files,
- next, move this extracted files to music-rnn/rnn_lstm_jzs1_eng/data like below.
```
music-rnn
└── rnn_lstm_jzs1_eng
    ├── data
    │   ├── JSB Chorales
    │   │   ├── test
    │   │   ├── train
    │   │   └── valid
    │   ├── MuseData
    │   │   ├── test
    │   │   ├── train
    │   │   └── valid
    │   ├── Nottingham
    │   │   ├── test
    │   │   ├── train
    │   │   └── valid
    │   └── Piano-midi.de
    │       ├── test
    │       ├── train
    │       └── valid
```
- for example, to use JSB_Chorales set,
- edit source codes (block of setting Data Set) of train_piano.py like below codes
```python
# ================================================================================
#
# when you wanna train model with all midi files at once
#

DIR_DATA_SRCs = ["/data/JSB_Chorales", "/data/MuseData", "/data/Nottingham", "/data/Piano-midi.de"]
DIR_TTV = ["/test", "/train", "/valid"]

# examples 1
# when u want to use "JSB_chorales/train" data for training - uncomment next 2 lines
path_train = os.getcwd() + DIR_DATA_SRCs[0] + DIR_TTV[1]
path_test = os.getcwd() + DIR_DATA_SRCs[0] + DIR_TTV[0]

# examples 2
# when use only bach`s midi files in /data/MuseData/
# target_str = "bach"
# path_train = os.getcwd() + DIR_DATA_SRCs[1] + DIR_TTV[1]
# path_test = os.getcwd() + DIR_DATA_SRCs[1] + DIR_TTV[0]

# examples 3
# when use midi files in /data/Nottingham/
# path_train = os.getcwd() + DIR_DATA_SRCs[2] + DIR_TTV[1]
# path_test = os.getcwd() + DIR_DATA_SRCs[2] + DIR_TTV[0]


# ================================================================================
#
# set directory name what is including data files which you wanna use at triaing
# set string(target_str) what is included in data files which you wanna use at triaing
#
# target_str = ""                         # if u use all files at certain directory, don`t set any letters
# TARGET_FOLDER = "waltzes"               # directory name which is containing data files for training
# path_train = "./data_for_train/" + TARGET_FOLDER

# init paths of Waltzes
# DIR_WEIGHTS = "./wts_Waltzes/"                      # save weights file
# DIR_RESULTS = "./predict_Waltzes/"                  # save debug log
# DIR_PREDICTED_MIDI = "./predMidi_Waltzes/"          # save predicted(created) midi file
DIR_WEIGHTS = "./wts_JSB/"                      # save weights file
DIR_RESULTS = "./predict_JSB/"                  # save debug log
DIR_PREDICTED_MIDI = "./predMidi_JSB/"          # save predicted(created) midi file

# file name to save
filename_result_predict = DIR_RESULTS + 'rnn_lstm_predict_{0}.txt'.format(datetime.now().strftime("%Y.%m.%d.%H:%M:%S"))
# ================================================================================

```
- in addition, if you want to use files that contain same name in a folder, insert the same name in ```target_str = "shared_name"```
  * for example, in a folder, there are files named 'bach001.mid', 'bach002.mid', etc, modify target_str variable as ```target_str = "bach"```
