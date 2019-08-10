#get user email

email = input('What is your Email address?: ').strip()

#slice username from the email

username = email[:email.index("@")]

#slice out the domain name from the email name

domain = email[email.index('@')+1:]

#format the message

output = "Your username is {} & your domain name is {}"

fullOutput = output.format(username,domain)

#display the messages

print(fullOutput)
