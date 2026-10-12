#START 
#ASK the user about the current hour
#STORE the input
#IF hour(input) is less than 21
#   DISPLAY "Plenty of time. You can go for another episode."
#ELSE IF hour(input) is 22
#   DISPLAY "One more episode is probably fine."
#ELSE IF hour(input) is more than 22
#   DISPLAY "Time to go to bed."
#END

hour = int(input("What time is it? Enter the current hour:"))
if hour < 21:
    print("Plenty of time. You can go for another episode.")
elif hour < 22:
    print("One more episode is probably fine.")
else:
    print("Time to go to bed.")