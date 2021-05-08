# Overwatch - Sound export
This usefool tool + tutorial gets you all the sound files extracted from the overwatch data files.

## Quick tutorial
1. Grab git contents
2. Get Tools
3. Get Python
4. Extract CASC
5. Run Python Script
6. Enjoy the sound files / contribute

### 1. Grab git contents
Just download & place in a folder of your choice.

### 2. Get Tools
This project depends on three tools.
* ww2ogg -> converts wem format to ogg. http://hcs64.com/files/ww2ogg019.zip
* revorb -> fixes ogg headers. http://yirkha.fud.cz/progs/foobar2000/revorb.exe
* casc tools -> helps us export contents from blizzard archive files. http://www.zezula.net/en/casc/main.html

Once downloaded, place the following files directly into the tools folder:

* ww2ogg -> ww2ogg.exe
* ww2ogg -> packed_codebooks_aoTuV_603.bin
* revorb.exe

(tools folder is projectfolder/tools)

### 3. Get Python
This project runs on Python 2.7.
Grab it from here: https://www.python.org/downloads/

### 4. Extract CASC
* Use the casc tool to open (OPEN STORAGE) Overwatch\data\casc\config\52\6a\ whatever files is in there.
* In the casc folder structure, select the folder "unknown".
* Extract the whole unknown folder to projectfolder/casc

### 5. Run Python script.
Run the main script.

#### 5a. How?
If you don't know too much about python, open up the attached run_extract.bat file with a text editor, and check if the path to python.exe is correct. (compare it to the place where you installed Python 2.7)
Then, just run the bat file. It will launch the python script.

It will check every exported file's header, and if it's wem format, converts it to ogg.
Checks against a list of hashes to sort the sound files.

NOTE: By default, this will not extract all files. Visit config.json and change "full_extract" from false to true to get all the ogg files.

By default the script stops after 1000 unknown sound files.

Current list has ~1000 sound files categorized. Total amount of sounds should be around 17.5k

### 6. Contribute
If you have the time, please get the next batch of audio files & categorize them.

Running the python script will generate an "unknowns.csv" file that contains all the sound files to be categorized.

NOTE: definitely leave in the 1k limit to make sure you don't get a huge csv file that your editor might not handle

db/fingerprints_noise.csv has all the files I considered non-interesting/noise

db/fingerprints_important.csv is everything else.

Structure is always the same in these two files:

hash of the file (find it in unknowns.csv) + path to place at.

you CAN rename in the fingerprints file the sound file to anything (like hanzo_pain_01.ogg). Right now please also leave in the ID you receive in the unknowns.csv (522_hanzo_pain_01.ogg or something)

You can either make a pull request for the fingerprint files if you categorized some more stuff, or send a csv file to me /u/blindmancs
