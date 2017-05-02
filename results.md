---
title: Results
layout: template
filename: /results
--- 
### Results:

Overall, our finished product was a web app that allows to user to chose a song to make a new song using Markov Chain analysis and music theory. Please see the video below for a demonstration followed by the evolution of the user interface and finally a description of the roadblocks we encountered.

[Video Demo](https://youtu.be/oGneS7-ZUNU)

### The Graphical User Interface Evolution

The user interface progressed over the course of our project. This advancement exemplifies the progress of the music we created. It started out as a bare minimum, but was eventually morphed into something beautiful. Below is a picture of the final User Interface, the previous user interfaces are shown below that picture.

Here, users are able to use the click down to find a song they want to base their new song on. The user should then hit play to hear thier new song play through Sonic Pi.


## Page 1
![Image of Second User Interface](/ComputerMusic/NewScreenPart1.png?raw=true)

![Image of Second User Interface](/ComputerMusic/NewScreen2.png?raw=true)

# Page 2
![Image of Second User Interface](/ComputerMusic/Page2Screen2.png?raw=true)
![Image of Second User Interface](/ComputerMusic/Screen2Page22.png?raw=true)



#### Below is a picture of the second user interface. The click down box allows users to choose a song of thier likeing.



![Image of Main User Interface](/ComputerMusic/pictures/mainpage.png?raw=true)




#### Below is a picture of the third user interface page that appears after you choose a song. Depending on the song, diffrent images will appear with a picture of the band.



![Image of Second User Interface](/ComputerMusic/pictures/main2.png?raw=true)



#### Here is an up close look at the options for choosing a song. We ended up with 5 song options.


![Zoomed Image of User Interface](/ComputerMusic/pictures/File_000.jpeg?raw=true)


#### Origially, the plan was to use this graphical user interface using Tkinter, which is a simple graphical user interfacae package. However, since a web app was more asstetically appealing we decided to transiton. Below is a picture of the GUI.


![GUI Draft](/ComputerMusic/pictures/GUIDRAFT.png?raw=true)

### RoadBlocks

Over the course of this project, we encountered a few issues that we had to work through. The application Sonic Pi was initially difficult to download and start for the whole project team It turns out that when Sonic Pi is running on a device, the device’s audience system is “taken over” in that nothing else can be playing in order for Sonic Pi to work.

We also had some difficulty in arranging the output of our algorithm to output two notes at once. We were not sure if Sonic Pi was able to play two notes at once. To make music sounding more like produced music, we needed to have two notes playing.

Another roadblock we encountered was reading the MIDI files and converting them into a uniform arrangement. Of the MIDI files we wanted to use, some of them used volume control to turn off notes rather than the “Note On” or “Note Off” message. On those particular files, essentially all the notes were playing at the same time, only most of them had a volume of zero. We identified a couple solutions to this problem. We could either import a file, code a function that would identify if the file uses volume control to turn notes on and off, and then add the proper on/off messages. Another solution would be to have our program identify if the file uses volume control and to direct that file to a different function from the other files that would accommodate the zero volume.


