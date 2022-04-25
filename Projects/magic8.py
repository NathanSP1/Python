#Declare a name variable and assign it to a person that will be asking the question
name = input("Enter Name: ")

#Declare a question variable
question = input(name + " Asks: ")

#Variable that stores the answer
answer = "The Magic 8 Ball's Answer is: "

#Importing a module to generate a random number
import random

#Creates a variable that stores the randomly generated value
random_number = random.randint(1,9)

print(random_number)

#Creating If/Elif/Else and assigning them values 
if random_number == 1:
    print(answer + "Yes - definitely")
elif random_number == 2:
    print(answer + "It is decidedly so.")
elif random_number == 3:
    print(answer + "Without a doubt.")
elif random_number == 4:
    print(answer + "Reply is hazy, try again.")
elif random_number == 5:
    print(answer + "Ask again later.")
elif random_number == 6:
    print(answer + "Better not tell you now.")
elif random_number == 7:
    print(answer + "My sources say no.")
elif random_number == 8:
    print(answer + "Outlook not so good.")
elif random_number == 9:
    print(answer + "Very doubtful.")
else: 
    print("Error...Outside of designated values")
    