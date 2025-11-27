import sys
if len(sys.argv) != 2:
    print("Usage: python electricity_bill.py <units>")
    sys.exit(1)

units = int(sys.argv[1])

rate = 5

bill = units * rate

print("\n--- Electricity Bill Calculator ---")
print(f"Units Consumed: Rupees{units}")
print(f"Rate per Unit: Rupess{rate}")
print(f"Final Bill: Rupees{bill}")
