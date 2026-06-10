# create a list for produce and dairy
produce = ["Tomatoes", "Lettuce"]
dairy = ["Milk", "Cheese"]

# concatinate produce and dairy into one single list called groceries
groceries = [produce, dairy] 

# outer loop should go through each category called section in groceries
for section in groceries:
    for item in section:
        print(f"Item name: {item}")