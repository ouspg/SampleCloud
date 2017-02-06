from django.contrib.auth.models import User
from django.test import TestCase


class UserTests(TestCase):


    def setUp(self):

        self.user = User.objects.create_user(username="testuser",
                                             email="testuser@example.com",
                                             password="passwd")


    def test_create_user(self):

        self.user.refresh_from_db()

        self.assertEqual(self.user.username, "testuser")
        self.assertEqual(self.user.email, "testuser@example.com")


    def test_update_user(self):


        self.user.username = "updateduser"

        self.user.save()

        self.user.refresh_from_db()

        self.assertNotEquals(self.user.username, "testuser")
        self.assertEqual(self.user.username, "updateduser")

    def test_delete_user(self):

        val = self.user.delete()

        self.assertEqual(val[0], 1)