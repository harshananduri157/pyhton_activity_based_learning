# Case Study 31: String-Based Examination Answer Evaluation
# Heading: Compare Student Answers with an Answer Key

answer_key = input(
    "Enter answer key (example: ABCD): "
).upper().replace(" ", "")

student_answers = input(
    "Enter student answers (use - for unanswered): "
).upper().replace(" ", "")

if len(answer_key) != len(student_answers):
    print("Error: Both answers must have the same length.")

else:
    correct = 0
    incorrect = 0
    unanswered = 0

    negative_mark = float(
        input("Enter negative marks per incorrect answer: ")
    )

    if negative_mark < 0:
        print("Negative marks cannot be less than zero.")

    else:
        for i in range(len(answer_key)):
            if student_answers[i] == "-":
                unanswered += 1

            elif student_answers[i] == answer_key[i]:
                correct += 1

            else:
                incorrect += 1

        score = correct - incorrect * negative_mark

        print("\nExamination Result")
        print("Correct answers:", correct)
        print("Incorrect answers:", incorrect)
        print("Unanswered:", unanswered)
        print(f"Final score: {score:.2f}")
