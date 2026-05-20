#Create a list meat with the values: "Ham", 3.99, 50, "Sliced"
meat = ["Ham", 3.99, 50, "Sliced"]
#Create a list cheese with the values: "Cheddar", 5.49, 100, "Sharp"
cheese = ["Cheddar", 5.49, 100, "Sharp"]
#Create a list condiment with the values: "Mustard", 1.99, 75, "Spicy"
condiment = ["Mustard", 1.99, 75, "Spicy"]

#Combine meat, cheese, and condiment lists into a single list called deli_dept
deli_dept = [meat, cheese, condiment]

#If "Ham" is in the meat list and its quantity is less than 100, update its quantity to 100
if "Ham" in meat and meat[2] < 100:
    meat[2] = 100

#Create a list seasonal_meat with the values: "Turkey", 4.50, 100, "Sliced"
seasonal_meat = ["Turkey", 4.50, 100, "Sliced"]
deli_dept.append(seasonal_meat)

#Print the initial state of deli_dept with the message: "Initial Deli List: <$deli_dept>".
print("Initial Deli List:", deli_dept)

#Remove the condiment list from deli_dept
deli_dept.remove(condiment)

deli_dept.sort()

#print the updated state of deli_dept with the message: "Updated Deli List: <$deli_dept>".
print("Updated Deli List:", deli_dept)