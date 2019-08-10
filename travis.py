known_users =["Niloy","Anik","Rajon","Ditta","Sony","Joyonti","Anika","Rafisa"]

print(known_users)

while True:
    print("Hi my name is travis")
    name = input("What is your name?: ").strip().capitalize()

    if name in known_users:
        print("Hello {} your name is recognized".format(name))
        remove = input("Would you like to remove yourself from the system (y/n)? ").strip().lower()

        if remove == 'y':
            known_users.remove(name)
            print(known_users)
            
        elif remove == 'n':
            print("No problem {}.You are always in our list..".format(name))
        
    else:
        print("Your name is NOT recognized")
        add = input("Would you want to add yourself to the system (y/n)? ").strip().lower()

        if add == 'y':
            known_users.append(name)
            print(known_users)

        elif add == 'n':
            print("No problem {}.See you again!!".format(name))
