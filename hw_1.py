class Person:
    def __init__(self, full_name, age, is_married):
        self.full_name = full_name
        self.age = age
        self.is_married = is_married

    def introduce_myself(self):
        print(f'My name is {self.full_name}, I am {self.age} years old. I am {self.is_married}.')

class Student(Person):
    def __init__(self, full_name, age, is_married, marks):
        super().__init__(full_name, age, is_married)
        self.marks = marks

    def average_mark(self):
        all_marks = sum(self.marks.values())
        return all_marks / len(self.marks)

class Teacher(Person):
    base_salary = 20000
    def __init__(self, full_name, age, is_married, experience):
        super().__init__(full_name, age, is_married)
        self.experience = experience


    def calculate_base_salary(self):
        if self.experience > 3:
            bonus = (self.experience - 3) * 0.05 * Teacher.base_salary
        else:
            bonus = 0
        return bonus + Teacher.base_salary


teacher = Teacher('Sadyr Nurgozhoevich', 28, 'married', 5)
teacher.introduce_myself()
salary = teacher.calculate_base_salary()
print(f'Salary with bonus is: {teacher.calculate_base_salary()}')
print()

def create_students():
    student_1 = Student('Adilet Askerov', 16, 'not married',
        {'Math': 5, 'English': 4, 'Chemistry': 5, 'Biology': 3, 'Physics': 3})
    student_2 = Student('Aman Mamytov', 15, 'not married',
                        {'Math': 3, 'English': 5, 'Chemistry': 4, 'Biology': 5, 'Physics': 4})
    student_3 = Student('Adilet Askerov', 16, 'not married',
                        {'Math': 5, 'English': 4, 'Chemistry': 5, 'Biology': 4, 'Physics': 5})
    return [student_1, student_2, student_3]

students = create_students()
for student in students:
    student.introduce_myself()
    print(f'Marks: {student.marks}')
    print(f'Average mark: {student.average_mark()}\n')

