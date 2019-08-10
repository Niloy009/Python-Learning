students = {
    "male" : ["Niloy","Sudipto","Pranto",'Rafi','Fahim'],
    "female" : ['Promita','Anika','Joya',"Momo",'Anne']
    }

for key in students.keys():
    for name in students[key]:
        if "a" in name.lower():
            print(name)
