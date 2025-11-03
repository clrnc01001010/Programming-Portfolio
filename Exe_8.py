nlist = ["Jake","Zac","Ian","Ron","Sam","Dave"]
user_input = input("Name that you are looking for:")

if user_input.capitalize() in nlist:
    print("It is in the List of Names")
else:
    print("It is not in the List of Names")

