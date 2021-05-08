# tensorflow-shakespeare-poem-generator
<img src="https://github.com/koflerm/tensorflow-shakespeare-poem-generator/blob/master/text.png?raw=true"/>
</br>
generates new poem using a Tensorflow RNN
Read more about it on  Medium: https://medium.com/@m_ko/deep-learning-with-tensorflow-part-3-music-and-text-generation-370cf37bb071

The basis of this project comes from Martin Gorner, I just added a small portion to it.
Original project: https://github.com/martin-gorner/tensorflow-rnn-shakespeare

Code for the Recurrent Neural Network in the presentation "Tensorflow and deep learning - without a PhD, Part 2" from Google. 
The presentation itself is available here:

* [Video](https://t.co/cIePWmdxVE)
* [Slides](https://goo.gl/jrd7AR)

## Usage:

```
> python3 rnn_train.py
```
The script **rnn_train.py** trains a language model on the complete works of William Shakespeare.
This takes hours, so be careful!
Please make sure you redownload the checkpoint files if you don't want to train the model first
   
[Fully trained](https://drive.google.com/file/d/0B5njS_LX6IsDc2lWTmtyanRpOHc/view?usp=sharing)
on Shakespeare or Tensorflow Python source.   
   
[Partially trained](https://drive.google.com/file/d/0B5njS_LX6IsDUlFsMkdhclNSazA/view?usp=sharing)
to see how they make progress in training.

Simply extract the files into the "checkpoints" directory

```
> python3 rnn_play.py
``` 
   
The script **rnn_play.py** uses a trained checkpoint to generate a new "Shakespeare" play. 
You can see the output in the terminal as well as in the file "output_generated.txt"

Have fun!


## Some generated Shakespeare poem
```
         TITUS ANDRONICUS


ACT I
 
SCENE III	An ante-chamber. The COUNT's palace.
 
[Enter CLEOMENES, with the Lord SAY]
 
Chamberlain
    Let me see your worshing in my hands.
 
LUCETTA
    I am a sign of me, and sorrow sounds it.
 
[Enter CAPULET and LADY MACBETH]
 
What manner of mine is mad, and soon arise?
 
JULIA
    What shall by these things were a secret fool,
    That still shall see me with the best and force?
 
Second Watchman
    Ay, but we see them not at home: the strong and fair of thee,
    The seasons are as safe as the time will be a soul,
    That works out of this fearful sore of feather
    To tell her with a storm of something storms
    That have some men of man is now the subject.
    What says the story, well say we have said to thee,
    That shall she not, though that the way of hearts,
    We have seen his service that we may be sad.
 
[Retains his house]
ADRIANA What says my lord the Duke of Burgons of Tyre?
 
DOMITIUS ENOBARBUS
    But, sir, you shall have such a sweet air from the state,
    There is not so much as you see the store,
    As if the base should be so foul as you.
 
DOMITIUS ENOY
    If I do now, if you were not to seek to say,
    That you may be a soldier's father for the field.
 
[Exit]
 ```
