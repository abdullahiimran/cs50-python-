def main():
    bill = input("How much was your bill? ")
    bill = float(bill.replace('$',''))
    percentage = input("How much tip do you want to give? ")
    percentage = float(percentage.replace('%',''))
    tip =float(bill * percentage / 100)
    print(f"Leave ${tip:.2f} as a tip.")

main()