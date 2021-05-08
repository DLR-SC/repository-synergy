
# Managed VMs OpenCV Sudoku Solver

## About

This sample application demonstrates the use of [OpenCV][1] run on App
Engine Managed VMs, to implement a Sudoku solver. The app allows you to capture an image of a
sudoku puzzle using your laptop's or phone's camera— or using a pre-existing image— and send it
to the app to be solved.  The app then solves the puzzle, using OpenCV to do OCR, and displays the
solution superimposed on the original image.
OpenCV does not run on traditional App Engine instances due to their sandboxing restrictions.

This app uses two [Modules](https://cloud.google.com/appengine/docs/python/modules/),
defined in `app.yaml` (the default module) and `backend.yaml` (the 'solver' module).
The default module uses "traditional" App Engine instances, and the `solver`
module specifies Managed VMs.

The app uses Task Queues to buffer solve requests.
The frontend instances in the default module receive user requests to solve a puzzle.
These requests are converted to tasks and added to a push queue,
with the task handlers run on the Managed VM instances.

This repo also contains a "minimal" version of a sudoku solver, which runs on
traditional (non-Managed VM) App Engine instances and does not use OCR.  Instead, it
takes as input a string of numbers that represents the puzzle's starting grid.
This app is in the `minimal_api` directory.

### OCR and Training Data

This app creates an OCR model based on training data. (The data is in the files
`samples_pixels2.data` and `feature_vector_pixels2.data`).
The model needs to both identify where the numbers are in a grid, and correctly identify each
number.
The model is currently not general enough to
work with the font & grid in every puzzle book.  In a follow-on version of this app, we'll include
a training script that you can use to improve the model.

We've included a couple of example puzzle image files that you can use to test the app.
They're in the `test_puzzles` directory.

Code was used and modified from the following sources:

- [OpenCV Python Tutorials blog][2]
- [Peter Norvig's blog][3]
- [OpenCV's square detector sample][4]


## Project Setup

Create a billing enabled project and install the Google Cloud SDK as described [here](https://cloud.google.com/appengine/docs/python/managed-vms/#install-sdk) (this includes [installing Docker](https://cloud.google.com/appengine/docs/python/managed-vms/#install-docker))

### Installing boot2docker on Linux

First install VirtualBox if you do not already have it:

```
$ sudo apt-get install VirtualBox
```

Next download the [latest boot2docker release](https://github.com/boot2docker/boot2docker-cli/releases) and then start the daemon:

```
$ <path_to_download>/boot2docker-<version>-linux-<processor> init
$ <path_to_download>/boot2docker-<version>-linux-<processor> up

```

Then continue with the Docker installation as described above.

### Enabling Google Cloud Storage

This app saves its images to Google Cloud Storage. To enable this you must first [create a bucket](https://cloud.google.com/storage/docs/cloud-console#_creatingbuckets) in Google Cloud Storage. Your app will automatically have write permission for this bucket if you create it within the project you created for your app. Otherwise, you must [set up a service account](https://developers.google.com/storage/docs/authentication#service_accounts) for your app, and add that service account to your [bucket's ACL](https://cloud.google.com/storage/docs/cloud-console#_bucketpermission).

Finally, edit the bucket name in `config.py` to match the name of the Google Cloud Storage bucket you created.

## Deploying

After successfully setting up your project, you can either [run locally](https://cloud.google.com/appengine/docs/python/managed-vms/sdk#run-local), or [deploy to production](https://cloud.google.com/appengine/docs/python/managed-vms/sdk#deploy).




[1]: http://opencv.org/
[2]: http://opencvpython.blogspot.com/
[3]: http://norvig.com/sudoku.html
[4]: https://github.com/Itseez/opencv/blob/master/samples/python2/squares.py
