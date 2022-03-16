print('My playlist challenge!')
# run your functions here

# 1 Import all the functions in playlist_functions.py
from playlist_functions import *
import numpy as np 
print()
# This code initializes your playlist as an empty list. no songs in it yet!
my_playlist = []
print()
# 2 Check what is in your playlist using the display_playlist() function
# HINT: the display_playlist() function in playlist_functions.py to figure out how to use it
# print('Question 2')
display_playlist(my_playlist)#NOTE we are calling the function and add 'my_playlist'. NOTE: this is the variable that we are working on. 
# 3 Add a song to my_playlist using the add_song() function
# The song that you add should be a dictionary, with the following key-value pairs
# 'artist' (string)
# 'title' (string)
'''
example_song = {'artist': 'Lauryn Hill', 'title': 'Everything Is Everything'}
'''
print()
song_1 = {'artist': 'J. Cole', 'title': 'Amari'}

song_2 = {'artist': 'Masego', 'title': 'Tadow'}

song_3 = {'artist': 'Rhianna', 'title': 'Desperado'}


print('Question 4')
#Check that you've added the song by running the display_playlist() function again
# display_playlist(my_playlist)
# print('Question 5')
#Add 2 more songs to my_playlist, then display it again using the display_playlist() function
song_4 = {'artist': 'Rhianna', 'title': 'Skin'}
song_5 = {'artist': 'Kendrick, Lamar', 'title': "Alright"}
song_6 = {'artist': 'Kendrick, Lamar', 'title': "King Kunta"}
song_7 = {'artist': 'Lil, Wayne', 'title': "Mona Lisa"}

# 6 In playlist_functions.py, define a function called get_playlist_length()
# See playlist_functions.py for details on how to define this function
add_song(my_playlist, song_1)
add_song(my_playlist, song_2)
add_song(my_playlist, song_3)
add_song(my_playlist, song_4)
add_song(my_playlist, song_5)
add_song(my_playlist, song_6)
add_song(my_playlist, song_7)
# THEN, call that function in this script to get the length of my_playlist
display_playlist(my_playlist)
print()
print('Question 6')
# 7 At the top of this script, import numpy using the usual alias
print(get_playlist_length(my_playlist))
print()
print('Question 8')
# 8: Using numpy, calculate the average monthly plays for a song
monthly_plays = [127030, 274920, 232453, 98278, 500301, 235462]
# TODO: using the mean() function from numpy, calculate the average of monthly_plays
print()
print(np.mean(monthly_plays))
print()
# BONUS In playlist_functions.py, define a new function called play_track()
# See playlist_functions.py for details on how to define this function
# Then play a few tracks, and run display_playlist() again to make sure it works
print('BONUS QUESTION!!!!')
play_track(my_playlist, 3)
