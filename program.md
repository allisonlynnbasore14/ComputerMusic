---
title: The Program
layout: template
filename: /program
--- 
### How to get started:


First, to make computer generated music, you need to fork and clone the GITHUB respitory at the following link:

[Link to Repo](https://github.com/msausville/Computer-Generated-Music)

Next, in order to make some music you need an instrument. For python, that instrument is Sonic Pi. This application is made to translate python code into musical notes. To download Sonic Pi, navigate to the below link and download the app or type the following into the command terminal. 


```
$ sudo add-apt-repository ppa:sonic-pi/ppa
$ sudo apt-get update
$ sudo apt-get install sonic-pi
```

![Image of Sonic Pi Logo](http://sonic-pi.net/images/logo.png)


Then run the following in the terminal:
```
$ pyton3 WebMusicApp.py
```
After doing this a link will appear in the terminal that will lead you to the user interface for music generation. From there, you simply pick a song from the drop down list and hit play. If you have Sonic Pi open, the song will play immediately. 

### How it works:

Here is a general diagram of the architecture of our program. 

![Image of Program Diagram](/ComputerMusic/Overview.png?raw=true)

Below is a more specific diagram of the basic structure of our program.
 
 
 ![Image of Program Diagram](/ComputerMusic/Screenshot from 2017-04-16 08-34-00.png?raw=true)
   
 
 
 A major compoent of the program are the class definitions. Below is a piece of the program code that shows the two classes. These class definitions set up a framework for note and song objects that we created. This allowed us to keep these type of objects consistent. Each song object has a list of notes intervals to play the notes in. The note class specifies that every note has a tone, a duration, and a volume.
   
![Image of Program Diagram](/ComputerMusic/pictures/Classes.png?raw=true)

 *****

### MIDI Files

A MIDI file is essentially a set of instructions to piece together a song. It has signals of “Note on” and “Note off.” When a "Note off" signal is set for a specific note for a specific song, this note will not play. Therefore, there are much more "Note off" signals than "Note on." The songs also has volumes for the series of notes that make up a song. It then requires an application, like Sonic Pi, to interpret that message and play the correct melody. MDI files are useful, not just for computer manipulation, but also for situations with limited storage space. A MIDI file is much small than an MP3 file. Overall, MIDI files are perfect for our purposes. We use the MIDI files as a base for our new computer music.

### Markov Chain:
Markov Chain is a process of analyzing a current state to find patterns that can be a template for other states. For example, the individual pedals of a flower are not identical, yet they all follow a similar shape, color, and size. Essentially, Markov chain counts each time an object ( a note in our case) is next to a different note for all combinations of notes. It then uses the most prominent patterns to create a new set of objects. In this way, we eliminated any outliers notes and focused on the core, repeating melody. Markov chain analysis has been applied to numerous files such as word analysis in literature and population statistics. Below is a link to more about Markov Chains.

[Link to Markov Chain Information](https://en.wikipedia.org/wiki/Markov_chain)

### Sonic Pi:
Sonic Pi is an open source app designed for aiding in beginners projects in Python. It has many features, such as setting the instrument to play the notes with. This program allows us to play our new song directly from python. Below is a link to more information about Sonic Pi.

[Link to Markov Chain Information](http://sonic-pi.net/)


![Diagram about Sonic Pi](/ComputerMusic/HowSonicPiWorks.png?raw=true)
