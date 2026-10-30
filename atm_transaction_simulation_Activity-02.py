# Case Study 13: ATM Transaction Sequence Simulation
# Heading: Simulate Deposits and Withdrawals in an ATM

balance = float(input("Enter opening balance: "))
transactions = input(
    "Enter transactions (example: D500,W200,D100): "
).upper().split(",")

if balance < 0:
    print("Opening balance cannot be negative.")
else:
    valid_count = 0

    for transaction in transactions:
        transaction = transaction.strip()

        if len(transaction) < 2:
            print("Invalid transaction:", transaction)
            continue

        kind = transaction[0]

        try:
            amount = float(transaction[1:])
        except ValueError:
            print("Invalid transaction:", transaction)
            continue

        if amount <= 0:
            print("Amount must be positive.")

        elif kind == "D":
            balance += amount
            valid_count += 1
            print(f"Deposited Rs. {amount:.2f}")

        elif kind == "W":
            if amount <= balance:
                balance -= amount
                valid_count += 1
                print(f"Withdrawn Rs. {amount:.2f}")
            else:
                print("Rejected: Insufficient balance.")

        else:
            print("Unknown transaction type:", transaction)

    print("Valid transactions:", valid_count)
    print(f"Final balance: Rs. {balance:.2f}")
