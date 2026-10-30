# Case Study 53: Food Waste Monitoring System
# Heading: Calculate Daily Leftovers and Food Waste Percentage

days = int(input("Enter number of days to record: "))

if days <= 0:
    print("Number of days must be positive.")

else:
    prepared_list = []
    served_list = []
    waste_percentages = []

    for day in range(1, days + 1):
        print(f"\nDay {day}")

        prepared = int(input("Meals prepared: "))
        served = int(input("Meals served: "))

        if prepared < 0 or served < 0 or served > prepared:
            print("Invalid meal quantities.")
            continue

        leftover = prepared - served

        if prepared > 0:
            percentage = leftover / prepared * 100
        else:
            percentage = 0

        prepared_list.append(prepared)
        served_list.append(served)
        waste_percentages.append(percentage)

        print("Leftover meals:", leftover)
        print(f"Waste percentage: {percentage:.2f}%")

    print("\nFood Waste Summary")

    total_prepared = sum(prepared_list)
    total_served = sum(served_list)
    total_leftovers = total_prepared - total_served

    print("Total meals prepared:", total_prepared)
    print("Total meals served:", total_served)
    print("Total leftover meals:", total_leftovers)

    if waste_percentages:
        print(
            "Highest daily waste percentage:",
            f"{max(waste_percentages):.2f}%"
        )
