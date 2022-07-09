import statistics

#Task_1
class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def feedback(self, lecturer, course, grade):
        if isinstance (lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.course_attached:
            if course in lecturer.student_feedback:
            lecturer.student_feedback[course] += [grade]
            else:
            lecturer.student_feedback[course] = [grade]
        else:
            print('Ошибка.')

    def average_rating(self, grade):
        av_rate = []
        courses = []
        for key, value in self.grades.items():
            av_rate += value
        if key not in courses:
            courses.append(key)
        else:
            courses += key
            print(statistics.mean(av_rate))
        if grade == 'grade':
            print(statistics.mean(av_rate))
        else:
            print('Ошибка')

    def __str__(self):
        grade = 'grade'
        list_courses_with_grade = 'list courses'
        print(f"Имя: {self.name}")
        print(f"Фамилия: {self.surname}")
        print(f"Средняя оценка за домашние задания: {self.average_rating(grade)}")
        print(f"Курсы в процессе изучения: {', '.join(self.courses_in_progress))}")
        print(f"Завершенные курсы: {', '.join(self.finished_courses)}")

    def __lt__(self, other):
        grade = 'grade'
        if not isinstance(other, Lecturer):
            print('He is not a Lecturer')
            return
            return self.average_rating(grade) < other.average_feedback()

    def __gt__(self, other):
        grade = 'grade'
        if not isinstance(other, Lecturer):
            print('He is not a Lecturer')
            return
            return self.average_rating(grade) > other.average_feedback()

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []



class Lecturer(Mentor):

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.grades = []

    def average_feedback(self):
        av_fb_list = []
        for key, value in self.student_feedback.items():
            av_fb_list += value
        print(statistics.mean(av_fb_list))

    def __str__(self):
        print(f"Имя:  {self.name}")
        print(f"Фамилия: {self.surname}")
        print(f"Средняя оценка за лекции: {self.average_feedback()}")


class Reviewer(Mentor):
    def __init__(self, name, surname, grades):
        self.name = name
        self.surname = surname
        self.grades = {}

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return "Ошибка"

def average_rating_students(course, *students):
  list_s = []
  for student in students:
    if student.grades.get(course):
      list_s.extend(student.grades[course])
  print(statistics.mean(list_s))

  def average_feedback_lecturers(course, *lecturers):
      list_l = []
      for lecturer in lecturers:
          if lecturer.student_feedback.get(course):
              list_l.extend(lecturer.student_feedback[course])
      print(statistics.mean(list_l))

#Students
student_1 = Student('Reiner, 'Braun')
student_2 = Student('Eren', 'Jager')

#What`s in progress
student_1.courses_in_progress += ['Python']
student_2.courses_in_progress += ['Python']
student_1.courses_in_progress += ['Git']
student_2.courses_in_progress += ['Git']

#What`s finished
student_1.finished_courses += ['English']
student_2.finished_courses += ['English']

#Lecturers
lecturer_1 = Lecturer('Sherlock', 'Holmes')
lecturer_2 = Lecturer('John', 'Watson')

#Courses
lecturer_1.course_attached += ['Python']
lecturer_1.course_attached += ['Git']
lecturer_2.course_attached += ['Python']
lecturer_2.course_attached += ['Git']

#grades for lecturers
student_1.feedback(lecturer_1, "Python", 9)
student_1.feedback(lecturer_2, "Python", 9)
student_1.feedback(lecturer_1, "Git", 10)
student_1.feedback(lecturer_2, "Git", 9)
student_2.feedback(lecturer_1, "Python", 9)
student_2.feedback(lecturer_2, "Python", 10)
student_2.feedback(lecturer_1, "Git", 10)
student_2.feedback(lecturer_2, "Git", 10)

#Reviewers
reviewer_1 = Reviewer('Mikasa', 'Akkerman')
reviewer_2 = Reviewer('Sasha', 'Abrams')

#courses of reviewers
reviewer_1.course_attached += ['Python']
reviewer_1.course_attached += ['Git']
reviewer_1.course_attached += ['English']
reviewer_2.course_attached += ['Python']
reviewer_2.course_attached += ['Git']

#grades of reviewers
reviewer_1.grade_homework(student_1, 'Python', 9)
reviewer_1.grade_homework(student_1, 'Python', 8)
reviewer_2.grade_homework(student_2, 'Python', 10)
reviewer_2.grade_homework(student_2, 'Python', 9)
reviewer_1.grade_homework(student_1, 'Git', 10)
reviewer_1.grade_homework(student_1, 'Git', 10)
reviewer_2.grade_homework(student_2, 'Git', 9)
reviewer_2.grade_homework(student_2, 'Git', 8)


#Task_2
print(f" {student_1.name} получил(а) следующие оценки: {student_1.grades}")
print(f" {lecturer_1.name} получил оценки {lecturer_1.student_feedback}")

#Task_3
print(reviewer_1)
print(lecturer_1)
print(student_1)

print(student_1 < lecturer_1)
print(student_1 > lecturer_1)

#Task_4
course = "Git"
print(average_rating_students(course, student_1, student_2))
print(average_feedback_lecturers(course, lecturer_1, lecturer_2))


