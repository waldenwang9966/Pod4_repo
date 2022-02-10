# 2.1
jamal_m_3pt = 46
fred_v_3pt = 43
james_h_3pt = 37

# 2.2
print(f"Jamal Murray made {jamal_m_3pt} 3-point shots, Fred VanVleet made {fred_v_3pt} 3-point shots, and James Harden made {james_h_3pt} 3-point shots!")

# 2.3
j_m_3pt_attempt = 93
f_v_3pt_attempt = 110
j_h_3pt_attempt = 109

# 2.4
print(f"Jamal Murray attempted {j_m_3pt_attempt} 3-point shots and made {jamal_m_3pt} of them.")
print(f"Fred VanVleet attempted {f_v_3pt_attempt} 3-point shots and made {fred_v_3pt} of them.")
print(f"James Harden attempted {j_h_3pt_attempt} 3-point shots and made {james_h_3pt} of them.")

# 2.5
j_m_percentage = 46 / 93
f_v_percentage = 43 / 110
j_h_percentage = 37 / 109


# 3.1
lakers_info = 'The Lakers went all in this offseason and swung a deal for former Pelicans forward Anthony Davis. They sent a package of Brandon Ingram, Lonzo Ball, Josh Hart, and 3 first-round picks to New Orleans to land Davis. Those three have made good developments with the Pelicans, especially Brandon Ingram. But, the deal is still a huge win for the Lakers as Lebron, Davis, and company have put together an incredible season. Los Angeles has ridden James and Davis, along with a supporting cast built around them, to the second-best record in the NBA. The Lakers ended the season atop the Western Conference with a record of 49-14. They were narrowly behind the Bucks for the best record in the league. Davis proved to the final piece necessary for the Lakers to rebound from missing the playoffís last year. Los Angeles was a dominant club on both sides of the ball and are in a position to have another successful year next season.'
print(lakers_info.replace('.', '\n'))

# 3.2 
print(lakers_info.replace('.', '\n').upper())

# 3.3
lakers_are_best = False
print(f"'The Lakers are the best basketball team in the NBA' is {lakers_are_best}!")

# 3.4
print(int(lakers_are_best))
# I think it takes the "0" value because 0 is false and 1 is true...following the binary system
print(float(lakers_are_best)) 

# 3.5
print(str(j_m_percentage))
print(str(f_v_percentage))
print(str(j_h_percentage))
# The percentages cannot be converted to strings because they are floats. Only integers can be converted to strings.

print(int(j_m_percentage))
print(int(f_v_percentage))
print(int(j_h_percentage))
# The percentages are rounded down to "0" because there is no whole number to round to instead; since the bigger numbers come after the decimal point.
