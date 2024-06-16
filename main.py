# A mobile phone service provider has 3 different subscription packages for
# its customers. 
# Package A: For $39.99 a month, 450 minutes are provided. Additional minutes
# are $0.45 per minute
# Package B: For $59.99 a month, 900 minutes are provided. Additional minutes
# are $0.40 per minute
# Package C: For $69.99 per month, unlimited minutes are provided.
# Write a program that calculates a customer's monthly bill. It should ask the
# user to enter the letter of the package the customer has purchased and the
# number of minutes that were used. The program should display the total
# charges.
# Calculate and display the amount of money Package A customers would save
# if they purchased Package B or C, and the amount of money Package B customers
# would save if they purchased Package C. If there would be no savings, no
# message should be printed.

# variables for base prices, minutes, and cost per extra minute
package_A_base_price = 39.99
package_B_base_price = 59.99
package_C_base_price = 69.99

package_A_minutes = 450
package_B_minutes = 900

package_A_extra_price_per_min = 0.45
package_B_extra_price_per_min = 0.40

# ask customer which package they purchased
customer_package = input("Enter the letter of the package you purchased. ").lower()

# if the customer chooses package a or b, ask them how many minutes they used
if (customer_package == "a" or customer_package == "b"):
    customer_minutes = int(input("Enter the number of minutes that were used. "))
    extra_minutes_A = customer_minutes - package_A_minutes
    extra_minutes_B = customer_minutes - package_B_minutes

# PACKAGE A
# calculate package A total if A is chosen
if (customer_package == "a" and extra_minutes_A > 0):
    package_A_total = package_A_base_price + (extra_minutes_A * package_A_extra_price_per_min)
    print(f"Your total for package A is ${package_A_total:.2f}")
elif (customer_package == "a" and extra_minutes_A <= 0):
    package_A_total = package_A_base_price
    print(f"Your total for package A is ${package_A_total:.2f}")

# if applicable, print the aount the customer would save if they purchased
# package B instead of A
if (customer_package == "a" and customer_minutes < package_B_minutes):
    savings = package_A_total - package_B_base_price
    if (savings > 0):
        print(f"You would have saved ${savings:.2f} by purchasing package B")
elif (customer_package == "a" and customer_minutes > package_B_minutes):
    package_B_total = package_B_base_price + (extra_minutes_B * package_B_extra_price_per_min)
    savings = package_A_total - package_B_total
    if (savings > 0):
        print(f"You would have saved ${savings:.2f} by purchasing package B")

# if applicable, print the amount the customer would save if they purchased
# package C instead of A
if (customer_package == "a" and package_A_total > package_C_base_price):
    savings = package_A_total - package_C_base_price
    print(f"You would have saved ${savings:.2f} by purchasing package C")    

# PACKAGE B
# calculate package B total if B is chosen
if (customer_package == "b" and extra_minutes_B > 0):
    package_B_total = package_B_base_price + (extra_minutes_B * package_B_extra_price_per_min)
    print(f"Your total for package B is ${package_B_total:.2f}")
elif (customer_package == "b" and extra_minutes_B <= 0):
    package_B_total = package_B_base_price
    print(f"Your total for package B is ${package_B_total:.2f}")

# if applicable, print the amount the customer would save if they purchased
# package C instead of B
if (customer_package == "b" and package_B_total > package_C_base_price):
    savings = package_B_total - package_C_base_price
    print(f"You would have saved ${savings:.2f} by purchasing package C")

# PACKAGE C
# if package C is chosen, print the total
if (customer_package == "c"):
    package_C_total = package_C_base_price
    print(f"Your total for package C is ${package_C_total:.2f}")
    
    
