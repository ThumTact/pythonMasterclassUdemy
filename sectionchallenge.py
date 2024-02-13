# simpler than what I do below with the nested while trues and conditionals
# put the selection var and menu generator at the end of the singular while true
selection = "-"
while selection != "0":
    print("Please choose your option from the list below:")
    print("1.\tLearn Python\n2.\tLearn Java\n3.\tGo Swimming"
          "\n4.\tHave dinner\n5.\tGo to bed\n0.\tExit")
    while True:
        selection = input("Choose your option: ")
        if selection in "12345":
            print("Option selected was {}.".format(selection))
        elif selection == "0":
            print("Option selected was {}.  Goodbye!".format(selection))
            break
        else:
            print("Invalid option selected.")
            break
# Instead of while True why not do while selection != 0?
