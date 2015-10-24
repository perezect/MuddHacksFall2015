# Author: Felis Perez
# song picker.py
#

import numpy as np
import soundfile as sf
import sys

class songData:
	"""
	Class to hold the song name, file name, and integer array of amplitudes.
	"""

	def __init__ (amplitudes, samplerate, name):
		"""
		Initiatlize the data of a song from a list of it's amplitudes, it's soundfile
		and it's file name
		"""
		self.amplitudes = amplitudes
		self.samplerate = samplerate
		self.name = name


def importSong(songFile):
	""" 
	Import a song and put it within a songData file.
	"""
	

	data, samplerate = song.read(soundfile)

	newSong = songData(data, samplerate, songFile)

	return newSong

def findBPM (song):
	"""
	TODO
	FFT the audio data to get the BPM
	"""
	return 0

def main():

	songList = []

	newDict = {}

	member = None

	for song in songList:
		member = importSong(song)

		newDict[self.findBPM(member)] = member

	print newDict


# 	options = sys.argv

# if __name__ == '__main__':
# 	main()







