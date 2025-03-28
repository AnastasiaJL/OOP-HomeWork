class Student:
    #описание Студента
    def __init__(self, name, surname, gender): # метод инициализации, self присутствует всегда
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
 
    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def lecturer_grade(self, lecturer, course, grade):
        # Для решения задачи мы создали метод, который будет проверять,
        # что оценка выставляется именно экземпляру класса Lecturer,
        # при этом преподаватель должен быть прикреплен к соответствующему курсу,
        # а студент должен его проходить. Только в таком случае оценка будет добавляться в словарь,
        # иначе будем получать ошибку.
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
        
    
    def average_grade_st(self):
    # Ищем среднюю оценку
        for x, y in self.grades.items():
            result_ST = sum(y)/len(y)
        return result_ST


    def __str__ (self):
    # Перезагружаем метод __str__
        return (f"""Имя: {self.name}
Фамилия: {self.surname}
Средняя оценка за домашние задания: {self.average_grade_st()}
Курсы в процессе изучения: {', '.join(self.courses_in_progress)}
Завершенные курсы: {' '.join(self.finished_courses)}""")
    
    def __gt__ (self, other):
    # Сравниваем средние оценки лекторов
        if isinstance (other, Student):
            return self.average_grade_st() > other.average_grade_st()
        return False  
    

 



class Mentor:
    #описание Преподавателя
    def __init__(self, name, surname):
        # метод для описания имени, фамилии, какой курс преподается
        self.name = name
        self.surname = surname
        self.courses_attached = []
        
    def rate_hw(self, student, course, grade):
        # Для решения задачи мы создали метод, который будет проверять,
        # что оценка выставляется именно экземпляру класса Student,
        # при этом преподаватель должен быть прикреплен к соответствующему курсу,
        # а студент должен его проходить. Только в таком случае оценка будет добавляться в словарь,
        # иначе будем получать ошибку.
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
        

class Lecturer (Mentor):
    # Лектор, основа взята из Преподавателя (Mentor)
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}


    def average_grade_le(self):
    # Ищем среднюю оценку
        for i, z in self.grades.items():
            result_LE = sum(z)/len(z)
        return result_LE


    def __str__ (self):
    # Перезагружаем метод __str__
        return (f"""Имя: {self.name}
Фамилия: {self.surname}
Средняя оценка за лекции: {self.average_grade_le()}""")
    
    def __gt__ (self, other):
    # Сравниваем средние оценки лекторов
        if isinstance (other, Lecturer):
            return self.average_grade_le() > other.average_grade_le()
        return False 
    
    def average_lecturer_grade(lecturers, course):
        total_grades = 0
        total_count = 0
        for lecturer in lecturers:
            if course in lecturer.grades:
                total_grades += sum(lecturer.grades[course])
                total_count += len(lecturer.grades[course])
        return round(total_grades / total_count, 2) if total_count else 0


    
class Reviewer (Mentor):
    # Эксперт, основа взята из Преподавателя (Mentor)
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        return super().rate_hw(student, course, grade)
    
    def __str__ (self):
    # Перезагружаем метод __str__
        return (f"""Имя: {self.name}
Фамилия: {self.surname}""")


#Задали Эксперта №1
some_reviewer = Reviewer('Mark', 'Print')
print (some_reviewer)

#Задали Эксперта №2
some_reviewer2 = Reviewer('Misha', 'Green')
print (some_reviewer2)

cool_mentor = Mentor('Phil', 'Loren')
cool_mentor.courses_attached += ['Python']

#Задали студента №1
some_student = Student('Ruoy', 'Eman', 'man')
some_student.finished_courses += ['Введение в програмирование']
some_student.courses_in_progress += ['Python']
some_student.courses_in_progress += ['Git']

#Проставили студенту №1 оценки
cool_mentor.rate_hw(some_student, 'Python', 2)
cool_mentor.rate_hw(some_student, 'Python', 10)
cool_mentor.rate_hw(some_student, 'Python', 9)

#Задали студента №2
some_student2 = Student('Gerard', 'Liroy', 'man')
some_student2.finished_courses += ['ООП: наследование, инкапсуляция и полиморфизм']
some_student2.courses_in_progress += ['Python']
some_student2.courses_in_progress += ['Java']

#Проставили студенту №2 оценки
cool_mentor.rate_hw(some_student2, 'Python', 2)
cool_mentor.rate_hw(some_student2, 'Python', 2)
cool_mentor.rate_hw(some_student2, 'Python', 2)

print (some_student)
print (some_student2)
print (some_student > some_student2)
 

#Задали лектора №1
some_lecturer = Lecturer('Sasha', 'Smith')
some_lecturer.courses_attached += ['Python']
some_lecturer.courses_attached += ['Excel']

#Проставили лектору №1 оценку
some_student.lecturer_grade(some_lecturer, 'Python', 9)
some_student.lecturer_grade(some_lecturer, 'Python', 6)
some_student.lecturer_grade(some_lecturer, 'Python', 3)


#Задали лектора №2
some_lecturer2 = Lecturer('Masha', 'Lotus')
some_lecturer2.courses_attached += ['Python']
some_lecturer2.courses_attached += ['Java']

#Проставили лектору №2 оценку
some_student.lecturer_grade(some_lecturer2, 'Python', 2)
some_student.lecturer_grade(some_lecturer2, 'Python', 2)
some_student.lecturer_grade(some_lecturer2, 'Python', 8)

print (some_lecturer)
print (some_lecturer2)
print (some_lecturer < some_lecturer2)



def average_student_grade(students, course):
    total_grades = 0
    total_count = 0
    for student in students:
        if course in student.grades:
            total_grades += sum(student.grades[course])
            total_count += len(student.grades[course])
    return round(total_grades / total_count, 2) if total_count else 0


def average_lecturer_grade(lecturers, course):
    total_grades = 0
    total_count = 0
    for lecturer in lecturers:
        if course in lecturer.grades:
            total_grades += sum(lecturer.grades[course])
            total_count += len(lecturer.grades[course])
    return round(total_grades / total_count, 2) if total_count else 0


students = [some_student, some_student2]
lecturers = [some_lecturer, some_lecturer2]
print(f"Средняя оценка студентов по курсу Python: {average_student_grade(students, 'Python')}")
print(f"Средняя оценка лекторов по курсу Python: {average_lecturer_grade(lecturers, 'Python')}")
