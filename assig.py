#START
#ASK the user how much money they currently have
#STORE the input
#IF input is less than 1000
#    DISPLAY "It’s still too early to buy a new phone."
#ELSE IF input is less than 2000
#    DISPLAY "You should save a little more!"
#ELSE IF input is less than 3200
#    DISPLAY "You are almost there!"
#ELSE
#    DISPLAY "Congratulations! You can go and buy a new phone!"
#END

money = int(input("How much money do you have? Enter the current amount:"))
if money < 1000:
    print("It’s still too early to buy a new phone.")
elif money < 2000:
    print("You should save a little more!")
elif money < 3200:
    print("You are almost there!")
else:
    print("Congratulations! You can go and buy a new phone!")
    