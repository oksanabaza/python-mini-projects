name = input("Type your name: ")
print("Welcome", name, "to this adventure!")

answer = input(
    "You are on a dirt road, it has come to an end and you can go left or right. Which way would you like to go? "
).lower()
if answer == "left":
    answer = input(
        "You come to a river, you can walk around or swim accross? Type walk to walk around and swim to swim accross: "
    )
    if answer == "swim":
        print("You swam accross and were eaton by an alligator.")
    elif answer == "walk":
        print("You walked a many miles, ran out of water and you lost the game.")
    else:
        print("Not a valid option. You lose.")

elif answer == "right":
    answer = input("You come to a bridge, it looks wobbly, do you want to cross it or head back (cross/back)? ")
    if answer == "back":
        print("You go back and lose")
    elif answer == "cross":
        answer = input("You cross the bridge and meet a stranger. do you want to talk to them (yes/no)? ")
        if answer == "yes":
            print("You talk to the stranger and they give you gold.", name, "You WIN!")
        elif answer == "no":
            print("You ignore the stranger and they offended an you lose.")
        else:
            print("Not a valid option. You lose.")
    else:
        print("Not a valid option. You lose.")
else:
    print("Not a valid option. You lose.")
