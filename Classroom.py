class Student:
    def __init__(self, name, courses, grades):
        self.name = name
        self.courses = courses
        self.grades = grades

    def gpa(self):
        sum = 0
        for grade in self.grades:
            sum = sum + grade
        gpa = sum / len(self.grades)
        return gpa

    # Returns if two students share a class
    def shared_classes(self, other):
        for course in self.courses:
            for other_course in other.courses:
                if (course == other_course):
                    print("You share a course: " + course)
                    return
        print("You do not share a course")
        

george = Student("George", ["Computer Science", "Geometry", "English"], [85, 92, 83])
rafal = Student("Rafal", ["Computer Science", "History", "Calculus"], [90, 95, 92])
kevin = Student("Kevin", ["Art", "Chemistry", "Music Theory"], [99, 87, 88])