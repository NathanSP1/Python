print("I have information for the following planets:\n")

print("   1. Venus   2. Mars    3. Jupiter")
print("   4. Saturn  5. Uranus  6. Neptune\n")

planet = range(1, 6)
planet = int(input("Enter the Planet number you're wanting to know the weight of 1-6: "))
weight = int(input("Enter your weight here: "))

# Write an if statement below:
if planet == 1:
    weight = weight * 0.91
elif planet == 2:
    weight = weight * 0.382
elif planet == 3:
    weight = weight * 2.34
elif planet == 4:
    weight = weight * 1.06
elif planet == 5:
    weight = weight * 0.92
elif planet == 6:
    weight = weight * 1.19


print(planet)
print(weight)

print("Planet chosen: ", planet)
print("Your weight on the planet is:", weight)
