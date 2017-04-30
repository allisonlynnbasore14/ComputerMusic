---
title: The Program
layout: template
filename: /program
--- 
### How to get started:



First, to make computer generated music, you need to fork and clone the GITHUB repository with the program files.
To fork and clone the GITHUB repository, follow the following instructions: 

 Notice---The repository that this website is attached to is not the complete repository. Due to large music files, a GITHUB website could not be made.--
 
 1) Click on the following link:

[Link to Repo](https://github.com/msausville/Computer-Generated-Music)

2) Click “Fork” in the top right hand corner.
3) Copy the link the follows the HTTPS: form field.
4) Go to your command terminal and move to the directory you want to clone the files into.
5) Paste the following in the terminal, replacing the current https with the one you copied from the git website.

Now, you just need to install a few dependencies to run the programs.

If you do not currently have python3 install put the following into your termianl:

```
$ sudo apt-get install -y python3 python3-pip python3-tk python3-dev

```

Install the following, by pasting them into your command terminal:

 at the following link:



```
$ pip3 install --upgrade pip
$ sudo apt-get update
$ sudo apt-get upgrade
$ sudo apt-get install -y python python-pip python-tk python-dev git build-essential
```

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
After doing this a link will appear in the terminal that will lead you to the user interface for music generation. The link will look something like this:
```
* Running on http://127..../
```
From there, you simply pick a song from the drop down list and hit play. If you have Sonic Pi open, the song will play immediately. 

### How it works:

Here is a general diagram of the architecture of our program. 

![Image of Program Diagram](/ComputerMusic/Overview.png?raw=true)

Below is a more specific diagram of the basic structure of our program.
   

 A major compoent of the program are the class definitions. These class definitions set up a framework for note and song objects that we created. This allowed us to keep these type of objects consistent. Each song object has a list of notes intervals to play the notes in. The note class specifies that every note has a tone, a duration, and a volume.
   
 *****
## Program Architecture 

Below is a further description of how our program makes a song, from the user input to the creation of a new melody. 

### User Chooses a song:

To begin making music, a user will chose a song the user interface. This interface is a web app that is complied by a web browser on by the users own computer once they run the program. We used Flask to power the program to make a web app. Flask is framework specifically made for powering web application with python. The reason we chose Flask as opposed to other similar frameworks like Django or Pyramid, was for Flack’s simplicity. Since we were generally beginners in making web applications, we decided a simple framework would fit our needs best. Using CSS (Cascade Style Sheets), we styled a simple interface form where the user can pick a song and launch program that makes a new song.

### Import MIDI files:

In order to use the MIDI files, we needed to extract certain information. First we found the number of ticks per beat, which is the units for the change in time between beats. Essentially, ticks represent how many time units to wait for each note to play. Next, we extract the beats per minute, the tempo, key, and the specific notes of the song that makes up the melody. 

### Organize file data:

Next, we organized the data form the MIDI files by making classes of objects. Each file makes a song class that is made up of notes that are in a note class.  In order to be considered a song, the object must have a list of notes, a list of durations, and a list of intervals. To be a note, an object must have a tone, a duration, and volume. All of these properties are important for the objects in order to perform Markov Chain analysis.

### Make Markov dictionary of song notes: 

This process prepared our program to perform Markov Chain analysis on the song. Markov Chain analysis is essentially observing the patterns in a series of objects. In our case, the Markov Chain algorithm counts how many times certain objects are found together. For example, if a C# note often follows a D# in the input song, the output song would be more likely to have a C# following a D#. This algorithm is made with weights applied to each pattern and then randomly selected to make a new song. The more times a pattern shows up, the more likely that it will be in the new song. Our program performs this analysis on the duration, note sequence, and intervals of each input song.

### Music theory analysis:

In addition to Markov analysis, we wanted to include a way to make the semi-randomly generated music more harmonious. Music theory is the study of the practices of composers to make music audibly attractive. Certain songs are catcher than other songs and music theory is the study of that phenomenon. We choose to apply some of the ideas of music theory into our algorithm in the form of making a bassline riff. A riff is essentially, a melody or rhythm that is repeated in a song. A bassline is the rhymic part of a song that is often played in a low pitch. There are four options for a base in our program. Two of them are based on traditional pop songs and the second two are the inverses of the first two. This additon is made to match the current use of the Markov Chain output.

Lastly, the information from the music theory analysis is made into a form that the Sonic Pi application understands and the song begins to play. 
 
***** 
## Parts of the Program

Below is a further description of all the elements to our program.

### MIDI Files

A MIDI file is essentially a set of instructions to piece together a song. It has signals of “Note on” and “Note off.” When a "Note off" signal is set for a specific note for a specific song, this note will not play. Therefore, there are much more "Note off" signals than "Note on." The songs also has volumes for the series of notes that make up a song. It then requires an application, like Sonic Pi, to interpret that message and play the correct melody. MDI files are useful, not just for computer manipulation, but also for situations with limited storage space. A MIDI file is much small than an MP3 file. Overall, MIDI files are perfect for our purposes. We use the MIDI files as a base for our new computer music.

### Markov Chain:
Markov Chain is a process of analyzing a current state to find patterns that can be a template for other states. For example, the individual pedals of a flower are not identical, yet they all follow a similar shape, color, and size. Essentially, Markov chain counts each time an object ( a note in our case) is next to a different note for all combinations of notes. It then uses the most prominent patterns to create a new set of objects. In this way, we eliminated any outliers notes and focused on the core, repeating melody. Markov chain analysis has been applied to numerous files such as word analysis in literature and population statistics. Below is a link to more about Markov Chains.

[Link to Markov Chain Information](https://en.wikipedia.org/wiki/Markov_chain)

### Sonic Pi:
Sonic Pi is an open source app designed for aiding in beginners projects in Python. It has many features, such as setting the instrument to play the notes with. This program allows us to play our new song directly from python. Below is a link to more information about Sonic Pi.

[Link to Sonic Pi Information](http://sonic-pi.net/)


![Diagram about Sonic Pi](/ComputerMusic/HowSonicPiWorks.png?raw=true)
