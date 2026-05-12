# The item's discount and stock status have been defined
discounted = False
lowStock = True
#Determine if the product is moving
movingProduct = discounted or lowStock
#Determine if item is eligible for promotion
promotion = not discounted and not lowStock
#print if item is eligible for promotion
print("Is the item eligible for promotion?", promotion)