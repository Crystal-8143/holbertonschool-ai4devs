def get_passing_students(students):
    passing_students = []

    for student in students:
        if student["score"] > 50:
            passing_students.append(student["name"])

    return passing_students

students = [
    {"name": "Alice", "score": 80},
    {"name": "Bob", "score": 50},
    {"name": "Charlie", "score": 65},
    {"name": "Diana", "score": 45}
]

passing = get_passing_students(students)

print("Passing students:", passing)