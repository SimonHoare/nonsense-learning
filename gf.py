# Creates a variable and assigns it the value of the user input
gender_identity = raw_input("What gender are you? (male/female) ")

# Creates a variable and assigns it a value on based on gender_identity 
gender = 'woman' if gender_identity == ('female' or 'woman') else 'man'

# Creates a variable and assigns it the value of user input as an integer
your_age = int(raw_input("How old are you? "))

# Creates a variable and assigns it the value of user input as an integer
girlfriend_age = int(raw_input("And how old is your sweetheart? "))

# Creates a variable and assigns it the value of your_aged halved plus 6
acceptable_minimum = (your_age/2) + 6

# If/else arguments to provide conditional repsonses based on age
if (girlfriend_age < 18) and (your_age >= 18):
    print "You should be in jail, you sicko!"
elif girlfriend_age < acceptable_minimum: 
    print "You dirty old %s!" % gender 
else:
    print "I wish you both much happiness!"
