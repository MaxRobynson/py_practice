if __name__ == '__main__':
    # Get the number of students
    N = int(input())

    # Initialize a list to store student records
    students = []

    # Input student names and grades
    for _ in range(N):
        name = input()
        grade = float(input())
        students.append([name, grade])

    # Find the second lowest grade
    grades = set([student[1] for student in students])
    second_lowest_grade = sorted(grades)[1]

    # Find students with the second lowest grade and sort their names alphabetically
    result_students = sorted([student[0] for student in students if student[1] == second_lowest_grade])

    # Print the result
    for student in result_students:
        print(student)
