print("Welcome to the Tip Calculator!!")
total_bill = float(input("What is the total bill? ₹"))
tip = float(input("What percentage tip would you like to give? 10, 12 or 15? "))
people = int(input("How many people to split the bill? "))

tip_amount = total_bill * (tip / 100)

final_bill = total_bill + tip_amount

each_to_pay = final_bill / people

round(each_to_pay, 2)

print(f"Each person has to pay: ₹{each_to_pay}")
