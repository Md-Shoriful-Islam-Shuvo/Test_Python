#Data transformer
def transform_dataset(data):
    # Your solution here
    
    # Step 1: Calculate average grade for each student and filter qualified students
    # (students with all grades above 70)
    qulified_students = {}
    for student in data:
        if all(grade > 70 for grade in student['grades']):
            average_grade= round(sum(student['grades']) / len(student['grades']),2)
            qulified_students[student['student_id']] = average_grade
    subject_summary = {}
    # Step 2: Create a summary of subjects taken by qualified students
    for student in data:
        if student['student_id'] in qulified_students:
            for subject in student['subjects']:
                if subject not in subject_summary:
                    subject_summary[subject] = 0
                subject_summary[subject] += 1
    
    # Step 3: Return the final dictionary with qualified_students and subject_summary
    return {
        "qualified_students": qulified_students,
        "subject_summary": subject_summary
    }

# Example input data
data=[
    {
        "student_id": "S123", 
        "grades": [88, 92, 85], 
        "subjects": ["Math", "Science", "History"]
    },
    {
        "student_id": "S124", 
        "grades": [65, 95, 80], 
        "subjects": ["Math", "Science", "English"]
    },
    {
        "student_id": "S125", 
        "grades": [91, 89, 92], 
        "subjects": ["Math", "Physics", "History"]
    }
]
print(transform_dataset(data))

