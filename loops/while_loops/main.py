start_number = 5
countdown_values = []
current = 5
#Use a while loop to count down from start_number to 1 (inclusive), decrementing by 1 each iteration
while start_number >= 1:
    print(f"Current number: {start_number}")
#During each iteration, append the current countdown value to the countdown_values list.
    countdown_values.append(current)
    start_number -= 1
    current = current - 1
#After the loop completes, print Discount countdown complete! and then print the countdown_values list.    
    print(f"Discount countdown complete! {countdown_values}")