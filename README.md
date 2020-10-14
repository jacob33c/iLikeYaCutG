# I Like your cut G, automatic tiktok tracker


[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger) 
Track how many shares your recent tiktok has, and then make it play a sound.

This repo was heavily requested by my TikTok followers because of the following video .
# Requirements!

  - Macbook/Mac Desktop. This script only works with MacOS because of the built in afplay command.
  - Must have python installed on your computer
  - must have the following python library installed on your computer 
  https://github.com/davidteather/TikTok-Api

  
### Installation

- Clone this repo to your local machine. Open a terminal and copy & paste the below line of code
- Make sure the repo is installed where you keep your python scripts
 ```sh
$ git clone https://github.com/jacob33c/iLikeYaCutG.git
```
- **NOTE**: Google "How to clone a github repository" if you are not familiar with this step.
- **REQUIRED** install the unofficial github API wrapper below
https://github.com/davidteather/TikTok-Api


### Setup
1. Open iLikeYaCutG.py and change  ```api.byUsername('jayspanks', count=1)``` to your tiktok username.
2. Open terminal and CD to where the script is stored. 
3. Use the following line of code to run the script. 
```sh
$ python3 iLikeYaCutG.py
```
-**NOTE**: you my have to change permissions on the file to run the script (google chmod file access).
### Customization
- Open  ``` iLikeYaCutG.py``` in a text editor and replace the audio with the sound of your choice.

