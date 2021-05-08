## Set up

1. Clone to your computer: 

		% git clone git@github.com:shkh/TrainingAssistant.git

2. Add Jcrop: 

		% cd TrainingAssistant
		% git submodule init
		% git submodule update
		% cd static/Jcrop
		% git checkout master

3. Install python modules
		
		% pip install -r freezed.txt

4. Add images into `static/img`

## Run server

    % python views.py

This command starts the Flask server on port 5000, visit `http://localhost:5000`.

![リス可愛い](http://farm9.staticflickr.com/8334/8131692997_6cd40c380a_z.jpg)

After all images will be processed, you will get `info.dat` and `bg.txt`; Respectively the list of `positive` samples and the list of `negative` samples.
