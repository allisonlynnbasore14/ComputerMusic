"""
This is the page setting up the webapp for Olin College Software Design Project: Music Generation 
The there are two HTML tempates assocaited with this web app:
Toolbox.HTML and UserInterface.HTML.

In order to run, you must download and open "SONIC PI" 
"""

from  MusicGeneration import main
from flask import Flask, request, render_template, url_for, flash, redirect
app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def profile():
	if request.method == 'POST':
		song = request.form['song'] #gets the requested song from the first web page
		#The Best Song Ever Midi doe not currently work

		#Below are the song options and their associated pictures
		#the pic is a picture related to the song
		#the call to the main function calls the MusicGeneration.py to make the song
		if song == "The Best Song Ever":
			main('UpAllNight.mid')
			pic = "https://i.kinja-img.com/gawker-media/image/upload/s--qn6H3zL3--/c_scale,fl_progressive,q_80,w_800/jiszvtpozcrbbzxrxmq6.jpg"
		elif song == "Twinkle Twinkle Little Star":
			main('TwinkleTwinkleLittleStar.mid')
			pic = "http://img.clipartall.com/yellow-star-border-clip-art-clipart-panda-free-clipart-images-yellow-star-clipart-552_599.png"
		elif song == "What Makes You Beautiful":
			main('WhatMakesYouBeautiful.mid')
			pic = "http://www.billboard.com/files/stylus/1977869-one-direction-brisbane-617-409.jpg"
		elif song == "Up All Night":
			main('UpAllNight.mid')
			pic = "https://cdn.gobankingrates.com/wp-content/uploads/One-Direction.png"
		else:
			pic = "https://scstylecaster.files.wordpress.com/2016/01/one-direction-breaking-up.jpg"

		#This sets the template up with the recieved variables of song and picture	
		return render_template("UserInterface.html", song = song, pic = pic)
	
	#Renders the second pape template
	return render_template("Toolbox.html")




if __name__ == "__main__":
	app.run().run()