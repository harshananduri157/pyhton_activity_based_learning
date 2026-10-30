# Case Study 12: Attendance Recovery Computation
# Heading: Calculate the Minimum Classes Needed to Reach Attendance Eligibility

attended = int(input("Enter classes attended: "))
conducted = int(input("Enter total classes conducted: "))
target = float(input("Enter required attendance percentage: "))

if conducted <= 0 or attended < 0 or attended > conducted or target <= 0 or target > 100:
    print("Invalid input.")
else:
    current = attended / conducted * 100
    print(f"Current attendance: {current:.2f}%")

    needed = 0
    while (attended + needed) / (conducted + needed) * 100 < target:
        needed += 1

    print("Minimum consecutive classes to attend:", needed)
    final_attendance = (attended + needed) / (conducted + needed) * 100
    print(f"Attendance after attending them: {final_attendance:.2f}%")
