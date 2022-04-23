#Enter a username 
user_name = (input("what is your username?: "))

#If the User is Dave then print message indicating him to get off of the computer 
if user_name == "Dave":
    print("Get off of my computer")

#If enterd name is angela_87 then it is possibly dave using someone else's account to access the computer so print a message indicating that you know it's Dave
if user_name == "angela_87":
    print("I know it's you Dave!!!")
    
else:
    print("Hello User: " + user_name)