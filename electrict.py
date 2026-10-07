def calculate_bill(units_consumed, cost_per_unit):
    bill = units_consumed * cost_per_unit
    return bill

units = float(input("Enter units consumed: "))
cost = float(input("Enter cost per unit: "))
bill = calculate_bill(units, cost)
print("Electricity Bill =", bill)
