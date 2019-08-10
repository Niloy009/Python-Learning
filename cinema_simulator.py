flims = { "Monpura": [15,10],
          "Tarzan": [10,10],
          "3Idiots": [12,12],
          "Titanic":[18,15]
    }

while True:
    choose = input("Which flim do you want to see? ").strip().title()

    if choose in flims:
        age = int(input("How old are you? ").strip())

        #check age

        if age >= flims[choose][0]:

            #check seats

            num_seats = flims[choose][1]

            if num_seats > 0:
                print("Enjoy the flim")
                flims[choose][1] = flims[choose][1] - 1
                
            else:
                print("Sorry!! We are sold out!!")
                
        else:
            print("You are too young to watch this movie...")
    else:
        print("We do not have that flim yet...")
        
