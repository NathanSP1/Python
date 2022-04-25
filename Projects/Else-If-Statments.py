#Grades recieved based on score

grade = input("Enter the grade recieved: ")
grade = int(grade)

if grade >= 90 :
    print("You recieved a 'A' for a grade")
elif grade >= 80:
    print("You recieved a 'B' for a grade")
elif grade >= 70:
    print("You recieved a 'C' for a grade")
elif grade >= 60:
    print("You recieved a 'D' for a grade")
else:
    print("You recieved a 'F' for a grade")

