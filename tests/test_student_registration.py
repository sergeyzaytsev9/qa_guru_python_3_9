from demoqa_tests.model.data.Student import Student,Hobby
from demoqa_tests.model.pages.registration_form import PracticePage
from datetime import date

practice_form = PracticePage()


def test_student_registration_form():
    student = Student(
        first_name='Sergey',
        last_name='Zaytsev',
        email='test@demoqa.com',
        phone='1234567890',
        address='Pushkina 8',
        birthday=date(1994, 5, 2),
        gender='Male',
        subject='Computer Science',
        hobby=[Hobby.Music, Hobby.Sports],
        image='Toolsqa.jpg',
        state='NCR',
        city='Delhi')
    practice_form.open()
    practice_form.fill(student).submit()
    practice_form.assert_results_registration(student)