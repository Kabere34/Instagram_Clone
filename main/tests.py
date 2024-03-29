from django.test import TestCase
from .models import *
# Create your tests here.
class PostTestCase(TestCase):
  # set up method
    def setUp(self):
      self.profile_test = Profile(name='ivy', user=User(username='mikey'))
      self.profile_test.save()

      self.image_test = Post(image='default.png', name='test', caption='default test', user=self.profile_test)

    def test_instance(self):
        self.assertTrue(isinstance(self.image_test, Post))

    def test_save_image(self):
        self.image_test.save_image()
        images = Post.objects.all()
        self.assertTrue(len(images) > 0)

    def test_delete_image(self):
        self.image_test.delete_image()
        after = Profile.objects.all()
        self.assertTrue(len(after) < 1)


class ProfileTestCase(TestCase):
    def setUp(self):
        self.user = User(username='ivy')
        self.user.save()

        self.profile_test = Profile(id=1, name='image', profile_picture='default.jpg', bio='this is a test profile',
                                    user=self.user)

    def test_instance(self):
        self.assertTrue(isinstance(self.profile_test, Profile))

    def test_save_profile(self):
        self.profile_test.save_profile()
        after = Profile.objects.all()
        self.assertTrue(len(after) > 0)


    