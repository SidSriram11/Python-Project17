valid = False
while not valid:
    try:
        bill = float(input("Enter the total bill amount: "))
        discount_pct = float(input("Enter the discount percentage: "))
        people = int(input("Enter the number of people: "))

        discount_amount = bill * (discount_pct / 100)
        final_bill = bill - discount_amount
        share = final_bill / people

    except ValueError:
        print("Error: Please type numbers only.")
    except ZeroDivisionError:
        print("Error: The number of people cannot be 0.")
    else:
        print(f"Final bill: ${final_bill:.2f}")
        print(f"Each person pays: ${share:.2f}")
        valid = True
    finally:
        print("Attempt finished.")
