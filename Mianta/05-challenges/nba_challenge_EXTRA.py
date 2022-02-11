# READ THE INSTRUCTIONS FILE (nba_challenge_instructions.md) FIRST
# EXTRA: This challenge is not required for a grade!

#2.1 Created variables for each player 3pt shots made
jamal_m_3pt = 46
fred_v_3pt = 43
james_h_3pt = 37

#2.2 Created variable to track number of 3-pt shot attempts by all 3 players
print(f"In the 2020 NBA playoffs, Jamal Murray made {jamal_m_3pt} 3-point shots")
print(f"In the 2020 NBA playoffs, Fred VanVleet made{fred_v_3pt} 3-point shots")
print(f"In the 2020 NBA playoffs, James Harden made{james_h_3pt} 3-point shots")


#2.3 Created variables of 3pt attempts for each player
jamal_m_3pts_attempted = 93
fred_v_3pts_attempted = 110
james_h_3pts_attempted =  109

#2.4 Created a statement to declare the made 3pt shots and the attepmted 3pt shots
print(f"In the 2020 NBA playoffs, Jamal Murray made {jamal_m_3pt} 3-point shots, out {jamal_m_3pts_attempted} shot attempts")
print(f"In the 2020 NBA playoffs, Fred VanVleet made {fred_v_3pt} 3-point shots, out {fred_v_3pts_attempted} shot attempts")
print(f"In the 2020 NBA playoffs, James Harden made {james_h_3pt} 3-point shots, out {james_h_3pts_attempted} shot attempts")

#2.5: printing the three point percentage for each player
jamal_m_percentage = 46 / 93
fred_v_percentage = 43 / 110
james_h_percentage = 37 / 109
# 3.1: Printed out the paragraph but with only 1 sentence per line
lakers_info ='The Lakers went all in this offseason and swung a deal for former Pelicans forward Anthony Davis. They sent a package of Brandon Ingram, Lonzo Ball, Josh Hart, and 3 first-round picks to New Orleans to land Davis. Those three have made good developments with the Pelicans, especially Brandon Ingram. But, the deal is still a huge win for the Lakers as Lebron, Davis, and company have put together an incredible season. Los Angeles has ridden James and Davis, along with a supporting cast built around them, to the second-best record in the NBA. The Lakers ended the season atop the Western Conference with a record of 49-14. They were narrowly behind the Bucks for the best record in the league. Davis proved to the final piece necessary for the Lakers to rebound from missing the playoffís last year. Los Angeles was a dominant club on both sides of the ball and are in a position to have another successful year next season.'
print(lakers_info.replace('.', '/n'))

# 3.2: Printed out the paragraph but with only 1 sentence per line
print(lakers_info.replace('.', '/n'))
print(lakers_info.upper())

# 3.3
# made a variable called `lakers_are_best` to indicate this
lakers_are_best = False
#printed out the variable in an f-string to convey my opinion on the lakers
print(f"'The Lakers are the best basketball team in the NBA' is {lakers_are_best}!")

#3.4: Type Conversion
#Converted your `lakers_are_best` variable to an integer, and printed
print(int(lakers_are_best))
#Converted your `lakers_are best` variable to a float, and printed 
print(float(lakers_are_best)) 

#3.5: Type Conversion Part 2
#Attempted to take each player's 3-point percentage and convert it to a string, and print them out.
#I  was unable to convert it because only intergers can be converted to strings
print(str(jamal_m_percentage))
print(str(fred_v_percentage))
print(str(james_h_percentage))
#took each player's 3-point percentage and converted it to a string, but noticed it was rounded down to "0" there is no whole number to
# round up to. The larger numbers that could be rounded are after the decimal point.
print(int(jamal_m_percentage))
print(int(fred_v_percentage))
print(int(james_h_percentage))
