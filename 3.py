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




def add_word():
    #my_dic= {}
    #my_dic['english']= str(input("please enter english word: "))
    #my_dic['persian']= str(input("please enter persian word: "))
    #words.append(my_dic)
    while True:
        new= []
        Add_Request = input("Do You Want Add word to dictionary?  y/n: ")
        if(Add_Request == "y"):
            english = [] 
            
            persian = [] 
            
            english = [item for item in input("Enter the english items : ").split()]
            persian = [item for item in input("Enter the persian items : ").split()]
            # using naive method
            # to convert lists to dictionary
            dict1 = {"english": english[i] for i in range(len(english))}
            dict2 = {"persian": persian[i] for i in range(len(persian))}
            newdict = {k:v for somedict in (dict1,dict2) for k, v in somedict.items()}
            print ("Resultant dictionary is : " +  str(newdict))
            a= new.append(newdict)
            dict(ChainMap(*new))
            
        elif(Add_Request == "n"):
            break

def show_dict():
    for i in range(len(words)):
        print(words[i])



show_menu()
choice = int(input("please choose a number: "))

if choice == 1:
    add_word()
elif choice == 4:
    show_dict()
