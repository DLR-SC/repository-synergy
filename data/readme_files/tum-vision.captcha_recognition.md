#CAPTCHA Recognition with Active Deep Learning


> Fabian Stark, Caner Hazirbas, Rudolph Triebel, and Daniel Cremers,
> **CAPTCHA Recognition with Active Deep Learning**,
> in *GCPR Workshop on New Challenges in Neural Computation*, 2015. [[bib](https://vision.in.tum.de/research/deeplearning?key=stark-gcpr15)]

## Code Structure

    -- CAPTCHA Recognition    
        |
        -- doc              ; related conference paper and thesis      
        |
        -- code             ; sources of the code
            |
            -- results      ; The program writes all of its output and logs into this folder
                |
                -- 00-3_layers-10000_initial_images-correct_mostuncertain         ; One example of a possible output
            |
            -- src          ; The program code
            |
            -- temp         ; Temporary folder where the program saves temp files which are deleted at the end of execution

## How To Run
### Required Hardware/Software

To be able to run the code you need a computer with

* Linux OS
* Python installed
* The Caffe Framework installed with Python wrapper
* php5, php5-gd, php5-cgi packages installed (necessary as we are creating the CAPTCHA images with a PHP script.)

### Download Code
Once libraries are installed, you can download the source from github:

    git clone https://github.com/tum-vision/captcha_recognition.git

### Configure
* Adjust $caffe variable in src/iterate.sh to point to your correct caffe foler
* If you are using Caffe with Cuda, make sure that your LD LIBRARY PATH is set correctly, or uncomment the following line in *src/iterate.sh* and enter the correct path to your Cuda library:

        export LD_LIBRARY_PATH=/usr/local/cuda-7.0/targets/x86_64-linux/lib

### Run

To run the program in the background, execute the file run_iterate.sh from the command line:

    chmod +x run_iterate.sh
    ./run_iterate.sh

All logs and outputs are written to the folder *results/<test_name>/log.txt* and *log2.txt*  
You can find one example output in *results/00-3_layers-10000_initial_images-correct_mostuncertain*. Note: To keep the repository small, only the first 3 folders (5000, 10000 and 15000) and the last folder (520000) for the confusion matrices and histograms that the program outputs were added.

**Important:** If you want to start the program for a second test, make sure that you change the $name in the file  *src/iterate.sh*. If the program is started for the second time with the same name, it tries to resume from the point where it was interrupted. NEVER EVER start two iterations with the same name at the same time ;)

## Possible Improvements

* Write a Caffe output layer that is able to learn several digits and the length of the sequence at once (compare also: [https://github.com/BVLC/caffe/pull/523](https://github.com/BVLC/caffe/pull/523)). At the moment we learn every digit independently which is not the most elegant way.
* Adjust the program to detect variable length CAPTCHAs. At the moment we have fixed the length to 6 for simplicity.
* Stop learning if the accuracy does not increase anymore, or even decreases. At the moment the program always trains for a predefined number of iterations. It would be better to use early stopping. Therefore one could for example use Python to start the training and test the accuracy from time to time and stop training if the accuracy has decreased compared to the previous test.
