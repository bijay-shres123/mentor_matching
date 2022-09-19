from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Student, Mentor

# Create your tests here.

class UserAccountTests(TestCase):

    def test_new_superuser(self):
        db = get_user_model()
        super_user = db.objects.create_superuser('email@email.com', 'username', 'password')
        self.assertEqual(super_user.email, 'email@email.com')
        self.assertEqual(super_user.username, 'username')
        self.assertTrue(super_user.is_superuser)
        self.assertTrue(super_user.is_staff)
    

    def test_new_user(self):
        db = get_user_model()
        user = db.objects.create_user('email@email.com', 'username', 'password')
        self.assertEqual(user.email, 'email@email.com')
        self.assertEqual(user.username, 'username')
        self.assertFalse(user.is_superuser)
        self.assertFalse(user.is_staff)
        self.assertEqual(str(user), "email@email.com")
        self.assertEqual(user.get_full_name(), "username")
        self.assertEqual(user.get_short_name(), "username")

        with self.assertRaises(ValueError):
            db.objects.create_user('', 'username', 'password')
    
    def test_new_user_api(self):
        db = get_user_model()
        user = db.objects.create_user_api('email@Email.com', 'username', 'STUDENT', 'password')
        self.assertEqual(user.email, 'email@email.com')
        self.assertEqual(user.username, 'username')
        self.assertEqual(user.user_type, 'STUDENT')
        self.assertFalse(user.is_superuser)
        self.assertFalse(user.is_staff)

        with self.assertRaises(ValueError):
            db.objects.create_user_api('', 'username', 'STUDENT', 'password')
    
    

class StudentProfileTestCases(TestCase):
    
    def test_student_model(self):
        db = get_user_model()
        user = db.objects.create_user("email@email.com", "username", "STUDENT", "password")
        student = Student.objects.create(user=user, gender="MALE")