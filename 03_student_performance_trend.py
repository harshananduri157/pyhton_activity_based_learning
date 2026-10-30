# Case Study 17: Student Performance Trend Analysis
# Heading: Compare Marks Across Examinations

subjects = input(
    "Enter subject names separated by commas: "
).split(",")

subjects = [subject.strip() for subject in subjects]

first_marks = []
second_marks = []

for subject in subjects:
    first = float(input(f"Enter {subject} marks in Exam 1: "))
    second = float(input(f"Enter {subject} marks in Exam 2: "))

    first_marks.append(first)
    second_marks.append(second)

print("\nPerformance Report")
print("------------------")

for i in range(len(subjects)):
    change = second_marks[i] - first_marks[i]

    if change > 0:
        status = "Improved"
    elif change < 0:
        status = "Declined"
    else:
        status = "No change"

    print(
        f"{subjects[i]}: {first_marks[i]} -> "
        f"{second_marks[i]} | {status} ({change:+.1f})"
    )

if len(subjects) > 0:
    average1 = sum(first_marks) / len(first_marks)
    average2 = sum(second_marks) / len(second_marks)

    print(f"Exam 1 average: {average1:.2f}")
    print(f"Exam 2 average: {average2:.2f}")
