# wordsquirt ✒️💦
 Python based text snippet expander for macos. My grandfather used to call writing implements "word squirters". Written in Python for macOS.

## Python Package requirements (one day I'll learn to package my software):

```
tinydb
rumps
pynput
py2app
```

## Sources:
~~Based originally off this article:
[https://chrisrosser.net/posts/2017/01/02/macos-system-wide-snippet-database/](Macos System Wide Snippet Database - chrisrosser.net)~~

Current iteration is from scratch.  

## Set up
Compile with:

``py2applet --make-setup wordsquirt/wordsquirt.py``

Then run the resulting app. Since this program monitors and controls the keyboard you will need to give it Keyboard Monitoring and Accessibility permissions when macOS prompts. On my machine I get what appear to be errors about missing modules during build but an app is still produced and runs fine.

Also in my experience, when using rumps and pynput together the app would crash when it would attempt to control the keyboard. Works as expected when compiled and run as a .app. On that note, I also had to delete and manually regrant Accessibility and Keyboard Monitoring whenever I made a new build. Otherwise the expansion wouldn't trigger, with no apparent errors.

## Todo:
- Implement drop down menu to delete existing expansions.
- Make procedure for adding a new expansion more robust.
- Possibly monitor the config and expansions file for updates to allow autoreload.
- Add icon and other cosmetic features.
- Add prompt to edit trigger string.
- Add menu item displaying current trigger string.
- Add menu to trigger expansions from dropdown.
