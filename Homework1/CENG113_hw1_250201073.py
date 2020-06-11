### 250201073 ###

coffee_list = ["Espresso", "Cappuccino", "Americano", "Macchiato", "Mocha", "Filter", "Turkish"] #Defining coffee list
price_list = [5.50, 7.75, 7.25, 9.50, 9.25, 5.75, 6] #Defining price list
cup_size_list = ["Tall", "Grande", "Venti"] #Defining types of cup sizes
client_counter = 9 #We will use this for free order
total_price = 0 #We will use this for the calculate total income
total_cup = 0 #We will use this to learn how many cups we sold totally
while True:
    coffee_type = input("Please enter the coffee type that you would like to drink: ") #Getting input from user about coffee type
    coffee_type = coffee_type.title() #Making coffee type case insensitive
    for i in range(len(coffee_list)):
            if coffee_type == coffee_list[i]:      
                variable = i
                break
    if coffee_type == "x" or coffee_type == "X": #Breaking the while loop to get total income and the total number of cups
        break
    if coffee_type in coffee_list and coffee_type != coffee_list[6]: #Except Turkish coffee
        cup_size = input("Please enter the cup size that you would like to get: ") #Getting input from user about cup size
        cup_size = cup_size.title() #Making cup size case insensitive
        while cup_size not in cup_size_list: #Asking again and again until getting a valid cup size
            cup_size = input("Please enter a valid cup size: ") 
            cup_size = cup_size.title()
        while cup_size in cup_size_list: #When we get a valid cup size
            number_of_cups = input("Please enter the number of cups that you want to order: ") #Getting input for number of cups
            while number_of_cups.isdigit() == False or int(number_of_cups) <= 0: #Asking again and again for a valid input
                cup_size = input("Please enter a valid number for number of cups: ") 
                cup_size = cup_size.title()
            number_of_cups = int(number_of_cups) #Converting number of cups variable to integer
            if cup_size == "Grande":
                temp_price = (price_list[variable] + 1) * number_of_cups #1 more TL for Grande
            elif cup_size == "Venti":
                temp_price = (price_list[variable] + 1.5) * number_of_cups #1.5 more TL for Venti
            else:
                temp_price = price_list[variable] * number_of_cups #Normal price for Tall
            if temp_price > 20 :
                temp_price = temp_price * 0.9 #Discount for more than 20 TL orders
            print ("You ordered", number_of_cups, cup_size, "cups of", coffee_type, "and the price is", temp_price, "TL") #Output
            client_counter += 1 #Counting clients
            total_price += temp_price #Adding the price to total price
            total_cup += number_of_cups #Adding the number of cups to total number of cups
            break #breaking while loop at line 24
    elif coffee_type in coffee_list and coffee_type == coffee_list[6]: #For Turkish coffee
        cup_size = "Tall" #Cup size must be Tall so we don't ask to user cup size
        number_of_cups = input("Please enter the number of cups that you want to order: ") #Getting input for number of cups
        while number_of_cups.isdigit() == False or int(number_of_cups) <= 0: #Asking again and again for a valid input
            number_of_cups = input("Please enter a valid number for number of cups: ")
        
        number_of_cups = int(number_of_cups) #Converting number of cups variable to integer
        temp_price = price_list[variable] * number_of_cups
        if temp_price > 20 :
            temp_price = temp_price * 0.9
        print ("You ordered", number_of_cups, cup_size, "cups of", coffee_type, "and the price is", temp_price, "TL")
        client_counter += 1 #Counting clients
        total_price += temp_price  #Adding the price to total price
        total_cup += number_of_cups #Adding the number of cups to total number of cups
    else:
        print("Please enter a valid coffee type") #For invalid coffee type
    if client_counter % 10 == 0: #Free order
        total_price -= temp_price #Subtracting the price of order from total price because it's free order
        total_cup -= number_of_cups #Subtracting the number of cups from the total number of cups because it's free order
        print ("Your order is free!")

print ("We have sold", total_cup, "coffees and our total sale is", total_price, "TL.") #End of the day output 