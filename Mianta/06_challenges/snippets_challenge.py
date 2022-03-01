print("Challenge 3.1: Debug code snippets")
#Debug each snippet in order

#this creates s[ace when printing
print()

print("Snippet 1:")

u = 5
v = 2

if u * v == 10: 
#added the 2nd "="
    print(f"The product of u ({u}) and v ({v}) is 10")
else:
    print(f"The product of u ({u}) and v ({v}) is not 10")
# see above and below comments about this
print()

print("Snippet 2:")
x = 15
y = 25

z = 30

if z < x:
    print("z is less than x")

elif z > x and z < y:
    print("z is between x and y")

else:
    print("z is greater than y")

#this is here to create space when printed
print()

print("Snippet 3:")

#modify the comparison operator below so the assert statement passes

#update the print statement to reflect changes to the code

a = 1 
b = 1
c = (a == b) #Added the 2nd "=" 
print(True == 1.0)
print(f"The value of c is True since a is equal to  b.")
assert(c == True) #Do not change this line

#these create an extra space when printed so everything is readable and not stacked ontop of each other. 
print()

print("Snippet 4:")

#modify exactly one boolean operator in the assignment of d, so that d evaluates to False

d = (5 < 7) or not (8 < 20)
# The d is set to False because of the " or not" this makes both sides of the comparison false since htey both are being compared under d and not individually.
assert(d == False) #Do not change this line

print()


print("Snippet 5:")

#modify the comparison operator so o evalutes to true
#update the print statement to reflect the changes

m = "GOAT"
n = "goat"

o = (m < n)

print (f"The value of o is True since Python is case-sensitive.")
assert(o == True) #Do not change  this line
# see comment above about this
print()
print("CHALLENGE COMPLETE!")