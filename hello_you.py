# ask user name

name = input("What is your name?: ")

#ask user age

age = input("What is your age?: ")

#ask user city

city = input("Where do you live in?: ")

#ask user what they enjoy?

love = input("What do you love to do?: ")

#create output

string = "Your name is {} and you are {} years old. You are from {} & you love {}."
output = string.format(name,age,city,love)

#Print the output to screen

print(output)
