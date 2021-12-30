from collections import ChainMap


words = [
    {'english':'apple', 'persian':'sib'},
    {'english':'tree', 'persian':'derakht'},
    {'english':'i', 'persian':'man'},
]

def show_menu():
    print("1- add new word")
    print("2- translation english2persian")
    print("3- translation persian2english")
    print("4- show dictionary")
    print("5- Exit")

DICTIONARY = []
print("Loading...")
myfile = open('/home/shahin/Desktop/Sajjad project/Assignment-7/project_python_Assignment_7/dictionary.txt', 'r+')
data = myfile.read().lower().split('\n')
for i in range(len(data)):
    if i%2==0:
        dic={}
        dic["english"] = data[i]
    else:
        dic["persian"] = data[i]
        DICTIONARY.append(dic)
english = [] 
persian = [] 

def add_word():
    #my_dic= {}
    #my_dic['english']= str(input("please enter english word: "))
    #my_dic['persian']= str(input("please enter persian word: "))
    #words.append(my_dic)
    while True:
        Add_Request = input("Do You Want Add word to dictionary?  y/n: ")
        if(Add_Request == "y"):
                       
            english = [item for item in input("Enter the english items : ").split()]
            persian = [item for item in input("Enter the persian items : ").split()]
            # using naive method
            # to convert lists to dictionary
            dict1 = {"english": english[i] for i in range(len(english))}
            dict2 = {"persian": persian[i] for i in range(len(persian))}
            newdict = {k:v for somedict in (dict1,dict2) for k, v in somedict.items()}
            DICTIONARY.append(newdict)
            print ("Resultant dictionary is : " +  str(newdict))           
        elif(Add_Request == "n"):
            break

def show_dict():
    for i in range(len(words)):
        print(words[i])

def toPersian():
    while True:
        demand = input("Do You Want Translate Again?   y/n:")
        if demand == "y":
            englishWord = input('Please Enter English Text: ')
            englishSplit = englishWord.lower().split(".")
            for i in range(len(english)):
                englishFor = englishSplit[i].split(" ")
                for j in range(len(englishFor)):
                    for k in range(len(DICTIONARY)):
                        if DICTIONARY[k]["english"] == englishFor[j]:
                            english.append(DICTIONARY[k]["persian"])
                            break
                        elif DICTIONARY[k]["english"] == ".":
                            len(DICTIONARY) - 1
                            english.append("\b.")
            print(" ".join(map(str,english)))
            english.clear()
        elif demand == "n":
            break

def toEnglish():
    while True:
        demand = input("Do You Want Translate Again?   y/n:")
        if demand == "y":
            persianWord = input('Please Enter Persian Text: ')
            persianDemand = persianWord.lower().split(".")
            for i in range(len(persianDemand)):
                persianFor = persianDemand[i].split(" ")
                for j in range(len(persianFor)):
                    for k in range(len(DICTIONARY)):
                        if DICTIONARY[k]["persian"] == persianFor[j]:
                            persian.append(DICTIONARY[k]["english"])
                            break
                        elif DICTIONARY[k]["persian"] == ".":
                            len(DICTIONARY) - 1
                            persian.append("\b.")
            print(" ".join(map(str,persian)))
            persian.clear()
        elif demand == "n":
            break

def save():
    write_file = open('/home/shahin/Desktop/Sajjad project/Assignment-7/project_python_Assignment_7/dictionary.txt','w')
    for i in range(len(DICTIONARY)):
        data_save = DICTIONARY[i]["english"] + "\n" + DICTIONARY[i]["persian"]
        write_file.write(str(data_save))
        if i < len(DICTIONARY)-1:
            write_file.write("\n")
    write_file.close()

show_menu()
choice = int(input("please choose a number: "))

if choice == 1:
    add_word()
elif choice == 2:
    toPersian()
elif choice == 3:
    toEnglish()
elif choice == 4:
    show_dict()
elif choice == 5:
    save()
