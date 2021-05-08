## lgcommander.py
lgcommander.py is a python script for controlling your Smart Lg TV with your PC.
It can be used for gaining access to hidden menus and modes.

## Supported models:
Lg has released two TV remote control apps for android smartphones in Google Play app store; each with a list of supported models. One for 2012 models and the other for some earlier models. If your TV is not on those lists, it may not be controllable through a network connection and these scripts may not work for you.

## To use it you need:
A PC, with python 3.x installed, connected to the same network as your Lg TV.

## Some useful codes:

* for EZ_ADJUST menu enter 255
* for IN START menu enter 251
* for Installation menu enter 207
* for POWER_ONLY mode enter 254

Warning: do not enter 254 if you do not know what POWER_ONLY mode is. You can find additional information about menus and modes here: <http://openlgtv.org.ru>   
 
As long as you do not "factory reset" your TV, pairing key doesn't change. You can use an editor to modify the line:

    lgtv["pairingKey"] = "DDGWAF"    

to suit your TV's actual pairing key.  This will eliminate the pairing key acquisition stage.

## Problem with latest LG firmware:
If you upgrade your TV firmware to 05.12.05 or later, "Tool Option 3" may be greyed out and you may not be able to make changes.  Please e-mail me if you have a solution to this problem (other than not upgrading).
#### "Quinny" says:
>Thanks for LG Commander!
>I've just managed to sort out the Options3 greyed out issue.
>Follow the instructions here: http://www.avforums.com/forums/lg-forum/1651400-official-lg-lw550t-3d-led-thread-part-9-a.html

## Windows users:
You can avoid the black console window if you change the "py" file extension to "pyw".

## Newer LG Smart TV (year 2012) models:
#### Benke Tamás says: 
"I wanted to use your lgcommander script, but i realized that its not working with lg 2012 smart tv series. I made some changes, now its working with the new series, but lg changed the keycodes too. Now, there are keycodes above 255 and ez-adjust, in-start code changed too, but i dont know them yet. I attached my version, if you want to improve yours."

#### I added Benke's version of the script as lg_2012_commander.py 

#### Ajay Ramaswamy says:
quote:

Hi,

Thanks for your lgcommander script. I was playing around with my 2012 55LM6200
TV and LG has provided a Android App Smart TV which provides a remote control
app.

I ran that app thru unzip, dex2class and JD-GUI and found the file 
com/lge/tv/remoteapps/Base/RemoteKeyIndex.class contains these key mappings


        KEY_IDX_3D=400;
        KEY_IDX_ARROW_DOWN=2;
        KEY_IDX_ARROW_LEFT=3;
        KEY_IDX_ARROW_RIGHT=4;
        KEY_IDX_ARROW_UP=1;
        KEY_IDX_BACK=23;
        KEY_IDX_BLUE=29;
        KEY_IDX_BTN_1=5;
        KEY_IDX_BTN_2=6;
        KEY_IDX_BTN_3=7;
        KEY_IDX_BTN_4=8;
        KEY_IDX_CH_DOWN=28;
        KEY_IDX_CH_UP=27;
        KEY_IDX_ENTER=20;
        KEY_IDX_EXIT=412;
        KEY_IDX_EXTERNAL_INPUT=47;
        KEY_IDX_GREEN=30;
        KEY_IDX_HOME=21;
        KEY_IDX_MUTE=26;
        KEY_IDX_MYAPPS=417;
        KEY_IDX_NETCAST=408;
        KEY_IDX_PAUSE=34;
        KEY_IDX_PLAY=33;
        KEY_IDX_POWER_OFF=1;
        KEY_IDX_PREV_CHANNEL=403;
        KEY_IDX_RED=31;
        KEY_IDX_STOP=35;
        KEY_IDX_VOL_DOWN=25;
        KEY_IDX_VOL_UP=24;
        KEY_IDX_YELLOW=32;

I have tried all these codes on my TV and they work OK

I hope you find this useful and someone else can test and confirm, and speed up
the search for the Service Menu codes.

Thanks & best regards

Ajay

unquote

#### Nikolay Sukharev [has commented:](https://github.com/ubaransel/lgcommander/issues/9#issuecomment-135912720)
quote

i found undocumented code range 418-470 that has response 200 most of codes displays only message with X except four:
```
458 - prompt for channel scanning
419,432,445 - set dtv channel 0
```
unquote

See his [comment](https://github.com/ubaransel/lgcommander/issues/9#issuecomment-135912720) for images.

#### s-e-v-e-n [has commented:](https://github.com/ubaransel/lgcommander/issues/9#issuecomment-135969965)
Hi there, the mapping from Ajay Ramaswamy didn't work for my 47LM640S-ZA.
I just tried every number, [here is what i found:](https://github.com/ubaransel/lgcommander/issues/9#issuecomment-135969965)

#### Robin Schneider's Version
Robin Schneider has developed a unified version of these scipts with command-line options. 
I am not able to test & verify his work which can be found here:
<https://github.com/ypid/lgcommander>

## This software was developed with inspiration and/or information taken from:

*   <http://python.org>


*   <http://openlgtv.org.ru>


*   An application written in ruby where you can find a comprehensive list of command codes:    
<https://github.com/dreamcat4/lgremote>
