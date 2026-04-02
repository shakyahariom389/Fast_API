def generate_sql(question):

    q = question.lower()

    courses = [
        "Mathematics",
        "Physics",
        "History",
        "Computer Science",
        "English"
    ]

    # detect course name from question
    for course in courses:
        if course.lower() in q:
            return f"""
            SELECT COUNT(*)
            FROM enrollments e
            JOIN courses c
            ON e.course_id = c.id
            WHERE c.name = '{course}'
            """

    if "total students" in q:
        return "SELECT COUNT(*) FROM students"

    if "courses" in q:
        return "SELECT * FROM courses"

    return "SELECT 1"