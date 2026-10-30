# Case Study 38: ATM Menu-Driven Banking Simulation
# Heading: Create a Menu-Based ATM Program

balance = 1000.0

while True:
    print("\n--- ATM MENU ---")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        print(f"Available balance: Rs. {balance:.2f}")

    elif choice == "2":
        amount = float(input("Enter deposit amount: "))

        if amount > 0:
            balance += amount
            print("Deposit successful.")
        else:
            print("Amount must be positive.")

    elif choice == "3":
        amount = float(input("Enter withdrawal amount: "))

        if amount <= 0:
            print("Amount must be positive.")

        elif amount <= balance:
            balance -= amount
            print("Withdrawal successful.")

        else:
            print("Insufficient balance.")

    elif choice == "4":
        print("Thank you for using the ATM simulation.")
        break

    else:
        print("Invalid choice. Select 1, 2, 3, or 4.")
