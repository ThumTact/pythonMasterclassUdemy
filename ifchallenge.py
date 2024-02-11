name = input("What is your name? ")
age = int(input("How old are you {}? ".format(name)))

if 18 <= age < 31:
    print("Welcome {}, to the holiday!".format(name))
else:
    print("Unfortunately, we'll have to leave you behind {}".format(name))
