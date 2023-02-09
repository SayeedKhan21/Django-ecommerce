from django.test import TestCase
from django.contrib.auth import get_user_model
from accounts.models import (
    Profile ,
)

def createUser(**payload) : 
    
    data = {
        'username' : 'test@example.com' ,
        'email' : 'test@example.com' ,
        'first_name' : 'abc' ,
        'last_name' : 'xyz'   
    }
    user = get_user_model().objects.create(**data)
    user.set_password('123')

    

class ModelTest(TestCase) : 

    """ Test various model funcitonalities and restrictions """

    def test_user_create_successfull(self) : 

        """ Test user creation """

        createUser()
        users = get_user_model().objects.all()
        self.assertEqual(users.count() ,1)
        user = users[0]
        self.assertEqual(user.email , 'test@example.com')

    def test_user_profile_create_using_signal(self) : 

        """ Test user profile creation using post save signal  """

        createUser()
        users = get_user_model().objects.all()
        self.assertEqual(users.count() ,1)
        user = users[0]
        self.assertEqual(user.email , 'test@example.com')
        profiles = Profile.objects.all()
        self.assertIsNotNone(profiles)
        self.assertEqual(profiles.count() ,1)
        self.assertEqual(profiles[0].user ,user)






