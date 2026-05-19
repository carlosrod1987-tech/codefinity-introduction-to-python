# Input variables
days_until_expiration = 5  # Example value
stock_level = 60  # Example value
product_type = "Perishable" # Can be "Perishable"or "Non-Perishable"

#run an if statement on product_type to equal the term "perishable'
if product_type == "Perishable":
#Apply a 30% discount if the product expires in 3 days or less and the stock level is over50 unit
    if days_until_expiration <= 3 and stock_level > 50:
        print("30% discount applied")
#Apply a 20% discount if the product expires in 4 to 6 days and the stock level is over50 units
    elif days_until_expiration > 3 and days_until_expiration <=6 and stock_level > 50:
        print("20% discount applied")
#Apply a 10% discount if the product expires in 7 days or more, or if the stock level is 50 units or less
    elif days_until_expiration > 6 and stock_level <= 50:
        print("10% discount applied")
#No discount if the product is not "Perishable".
else:
    print("No discount available for non-perishable items.")