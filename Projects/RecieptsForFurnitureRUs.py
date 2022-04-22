#Discription of the FurnitureStore
furniture_R_US_Seat = "FurnitureRUS has Tufted polyester blend on wood furniture that is 32 inches in hight x 40 inches in width x 30 inches in deepth in the colors Red or white."

#Define the price of the furniture
furniture_R_US_Seat_Price = 240

#Describes the other kind of furniture that the company offers
furniture_R_US_Stylish = "FurnitureRUS offers a stylish faux leather on birch that is 29.50 inches in height by 54.75 inches in width by 28 inches in depth and comes in the color black"

#Defines the price of the stylish piece of furniture
furniture_R_US_Stylish_Price = 180.50

#Decribes the lamp product that furnitureRUS offers
furniture_R_US_Lamp = "FurnitureRUS offers a luxurious lamp made of glass and iron that is 36 inches in heght in the color Brown with a Cream shade"

#Defines the price of the lamp
furniture_R_US_Lamp_Price = 52.15

#Defines the sales tax for the purchase 
sales_tax = 0.088

#Defines the expense of the first customer 
customer_one_total = 0

#This will list the items that the customer is purchasing 
customer_one_itemization = ""

#The customer one has decided to buy the seat
customer_one_total += furniture_R_US_Seat_Price

#Tracking the purchase of the seat from customer one by using the description
customer_one_itemization += furniture_R_US_Seat

#Customer one has decided to buy the lamp, Adds the price to the last item purchased
customer_one_total = furniture_R_US_Seat_Price + furniture_R_US_Lamp_Price

#Updates the Items list that includes the second purchase 
customer_one_itemization += furniture_R_US_Seat + furniture_R_US_Lamp

#Calculates the sales tax to the total of customer one
customer_one_tax = customer_one_total * sales_tax

#Adds the sales tax and the total of customer one
customer_one_total += sales_tax

#This will print out the reciept 
print("Customer one items: " + customer_one_itemization)

print("The customers total owed is: " , customer_one_total)
