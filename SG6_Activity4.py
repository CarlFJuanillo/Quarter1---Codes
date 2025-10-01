# get the name of the user
name = input("Enter your full name(First, Middle, Last): ")

# extract the names
First, Middle, Last = name.split(",")

# capitalize the names
First = First.strip().capitalize()
Middle = Middle.strip().capitalize()
Last = Last.strip().capitalize()

# convert middle name to initial
Middle = Middle[0] + "."

# display the formatted name
print("Formatted Name: {}, {} {}".format(Last, First, Middle))
