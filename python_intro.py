# print('Hello, She Codes!')

# ---- if elif else

# if
if 3 > 2:
    print('it works!')

# else
if 5 > 2:
    print('5 is greater than 2')
else:
    print('5 is not greater than 2')

# elif else:
    # if TRUE then print
    # if FALSE, then check elif
    # elif TRUE then print
    # elif FALSE, then action else
    # else print
name = 'Sonja'
if name == "Kristy":
    print("Hey Kristy!")
elif name == "Sonja":
    print("Hey Sonja!")
else:
    print("Hey Anonymous!")

# if elif(s) else
volume = 57
if volume < 20:
    print("It's kinda quiet.")
elif 20 <= volume < 40:
    print("It's nice for background music")
elif 40 <= volume < 60:
    print("Perfect, I can hear all the details")
elif 60 <= volume < 80:
    print("Nice for parties")
elif 80 <= volume < 100:
    print("A bit loud!")
else:
    print("My ears are hurting! :(")