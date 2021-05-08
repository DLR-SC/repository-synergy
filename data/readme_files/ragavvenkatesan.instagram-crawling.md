# Crawling Down Instagram - A python code.

This is a code to crawl down instagram. You can use it
to crawl down in a breadth first search from some starting user
and also collect the MIT popularity score along with every image. 
This also collects edges between each user therefore builds following 
and follower network along with capturing comments, hash tags and other 
information along with the images. 

## Reason for this code. 
I was briefly using this code, when I was getting a lot of rejects on my
research and was searching for new project ideas. I took this course called
'social media mining' and as a class project I thought I would investigate 
emotions and sentiment on instagram images. I wanted a code to be able to crawl
down instagram starting from a user along with user-user relationship information
images, hastags of images, comments on images, image caption and along with images,
the MIT media popularity score for each image [1].

## Setup. 

To run this code you need the following:

    1. [InstagramAPI](https://github.com/Instagram/python-instagram)
    2. urllib2
    3. json


Go to [Instagram Developer Page](https://instagram.com/developer/) and setup yourself as a developer and create an app.
sure to google this out and find out what is your `client_id`, `client_secret` and also setup a `redirect_uri`. 

Supply these properly on the boiler plate in this section of the code within the `' '`:

    client_id = ' '         
    client_secret = ' '     
    redirect_uri = 'http://localhost'    
    
Other data is self-referential. 

## Outputs. 

The outputs are saved in many files. In the `media` folder, you'll find all images for different users being saved as `.jpg` files. 
You'll also find number of comments, number of likes, the MIT popularity score[1], what filter is being used, the image_id and the
acutal link to image saved in the 'data.csv' file for each user. 

In the `profilepictures` folder you'll find the profile picture at the time of crawling of each person. In the file `edges.csv`
you'll find pair-wise edges for each user. In the `found_nodes` you'll find the nodes we have 'visited' and in the `known_nodes` you'll
find a list of nodes, we already know from BFS.

In the file `user_details.csv`, you'll find details about the userid, username, user full name, number of media uploaded,
number of followers, number of people being followed and the popularity score of the profilepicture[1]. 


## References

[1] [A. Khosla, A. D. Sarma, and R. Hamid. What makes an image
popular? In International World Wide Web Conference
(WWW), Seoul, Korea, April 2014](http://popularity.csail.mit.edu/)


