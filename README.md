# wordsquirt ✒️💦
 Python3 based text shortcut expander for macos. My grandfather used to call writing implements "word squirters". This program monitors your keyboard input until you type a trigger and keyword. Then wordsquirt erases the keyword you just typed and replaces it with your predefined text.

## Requirements:
Recent masOS with [python3](https://www.python.org/downloads/) and [git](https://git-scm.com/download/mac) installed. I recommend using the [official python3 installer](https://www.python.org/downloads/), I had issues building with homebrew provided python3.

## Install Instructions:

This repo includes the source code for wordsquirt, and a script which will build and install the app to your /Applications folder.

```
$ git clone https://github.com/ostcrom/wordsquirt.git
$ cd wordsquirt;
$ ./install.sh
```
Then just run "wordsquirt" from your Applications folder/launcher and allow accessibility and input monitoring permissions when prompted.

## How to Use
1. After opening wordsquirt, click the '✒️💦' icon in the mac system bar.
2. Click 'Add New Text Expansion' in the drop down. When prompted enter the keyword to trigger your text shortcut, then enter the string of text you want to appear. For example you could enter 'addr' as a trigger and your street address as the expanded text.
3. Switch to another application, then type two commas in a row followed by your keyword (eg: ',,addr'). Your shortcut will be replaced by the expanded text. As you can see, the default short cut trigger is two commas but this can be edited by clicking 'Edit Config File' in the wordsquirt system bar dropdown. Obviously something very short that you would never type otherwise is desirable as a trigger.
4. Congrats! You've created a text shortcut and you're using wordsquirt!

![](doc/img/demo.gif)
