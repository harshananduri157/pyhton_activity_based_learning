# Case Study 42: Student Marks Matrix Analysis
# Heading: Analyse Student Marks Using a Nested List

students = int(input("Enter number of students: "))
subjects = int(input("Enter number of subjects: "))

if students <= 0 or subjects <= 0:
    print("Numbers must be positive.")

else:
    marks = []

    for i in range(students):
        row = []

        print(f"\nEnter marks for Student {i + 1}:")

        for j in range(subjects):
            mark = float(
                input(f"Enter marks for Subject {j + 1}: ")
            )
            row.append(mark)

        marks.append(row)

    print("\nStudent Totals and Averages")

    for i in range(students):
        total = sum(marks[i])
        average = total / subjects

        print(f"Student {i + 1}: Total = {total:.2f}")
        print(f"Average = {average:.2f}")

    print("\nSubject Averages")

    for j in range(subjects):
        total = 0

        for i in range(students):
            total += marks[i][j]

        average = total / students
        print(f"Subject {j + 1}: {average:.2f}")

    averages = [sum(row) / subjects for row in marks]
    top_index = averages.index(max(averages))

    print(
        f"Top performer: Student {top_index + 1}, "
        f"Average = {averages[top_index]:.2f}"
    )
