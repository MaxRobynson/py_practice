"""if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input("enter the name to query: ")
    
    
    if query_name in student_marks:
        average_marks = sum(student_marks[query_name]) / len(student_marks[query_name])
        print("{:.2f}".format(average_marks))
    else:
        print("Student not found.")"""
        
if __name__ == '__main__':
    try:
        n = int(input("Enter the number of students: "))
        student_marks = {}
        
        # Input student names and scores
        for _ in range(n):
            name, *line = input().split()
            scores = list(map(float, line))
            student_marks[name] = scores

        query_name = input("Enter the name to query: ")

        if query_name in student_marks:
            average_marks = sum(student_marks[query_name]) / len(student_marks[query_name])
            print("{:.2f}".format(average_marks))
        else:
            print("Student not found.")

    except ValueError:
        print("Error: Please enter a valid number.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    
    
