# NOTE: these first two functions do not have to be edited

#prints out what is in your playlist
# takes one argument: 'playlist' (a list)NOTE: this prints everything on the playlist and is a parameter
from turtle import title

def display_playlist(playlist):
	if len(playlist) == 0:
		print('Playlist is empty!')
	else:
		for i in range(len(playlist)):
			print(f'Track {i+1}: {playlist[i]["plays"]} plays \
				  \n\t-{playlist[i]["title"]} by {playlist[i]["artist"]}')

#function to add a song to the playlist
# takes two arguments: 'playlist' (a list), and 'song' (a dictionary)
def add_song(playlist, song):
	# automatically initialize play count of song to 0
	song['plays'] = 0
	playlist.append(song)

#This function should have one parameter called 'playlist'
'''
The function should return an integer value indicating how many songs there are
'''
def get_playlist_length(playlist):#TODO (Question 6):define a function called get_playlist_length()
	return len(playlist)
#TODO (BONUS): define a function called play_track()
# It should have two parameters-'playlist' (a list)-'track' (an integer) - this should be optional, and by default play track 1

#This function should 'play' the song corresponding to the input track 

def play_track(playlist, track = 1):
	for i in range(len(playlist)):
		if track == i+1:
			print(f'Now playing track {track}, {playlist[i]["title"]} by {playlist[i]["artist"]}')
			playlist[i]['plays'] += 1
