#Deines the weight variable 
weight = 4.8

#Ground Shipping
if weight <= 2:
    ground_cost = weight * 1.5 + 20
elif weight <= 6:
    ground_cost = weight * 3 + 20
elif weight <=10:
    ground_cost = weight * 4.00 + 20
else:
    ground_cost = weight * 4.75 + 20
    
print("The cost of the shipping your package using ground shipping would be: $" , ground_cost)

#Premium Shipping Price
premium_shipping = 125.00

print("The premium Shipping cost is: $" , premium_shipping)

#Drone Shipping 
if weight <= 2:
    drone_cost = weight * 4.5 + 0
elif weight <= 6:
    drone_cost = weight * 9.00 + 0
elif weight <=10:
    drone_cost = weight * 12.00 + 0
else:
    drone_cost = weight * 14.25 + 0

print("The cost of the shipping your package using Drones would be: $" , drone_cost)
