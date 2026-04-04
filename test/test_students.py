import unittest
from src.models import Student
from src.app import App
from src.validation import ValidationError

class TestStudentRegistry(unittest.TestCase):
    def setUp(self):
        self.app = App()

    def test_add_student_success(self):
        self.app.add_student(2026, "Abdoulaziz Ridwan", "77123456", 85, 90)
        self.assertIn(2026, self.app.students)

    def test_duplicate_id_error(self):
        self.app.add_student(2026, "User1", "77111111", 80, 80)
        with self.assertRaises(ValidationError):
            self.app.add_student(2026, "User2", "77222222", 70, 70)

    def test_invalid_grade_range(self):
        with self.assertRaises(ValidationError):
            self.app.add_student(101, "Test", "77000000", 150, 90)

    def test_term_grade_math(self):
        student = Student(1, "Calc Test", "000", 70, 90)
        # (70 * 0.4) + (90 * 0.6) = 82.0
        self.assertEqual(student.term_grade(), 82.0)

