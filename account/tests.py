from django.test import TestCase
from django.core.urlresolvers import reverse 
from django.contrib.auth.models import User
from account.views import get_actionlist
from actions.models import Action
import bookmarks.settings as settings 

class UserViewTest(TestCase):
    
#     def test_user_list_with_active_users(self):
#         """
#             Only active users should be displayed
#         """
#         response = self.client.get(reverse("account:user_list"))
#         self.assertEqual(response.status_code, 200)
#         
#     def test_get_actionlist_with_particular_user(self):
#         """
#             Only particular user action should be selected 
#         """
#         f = open('log.txt', 'w')
#         f.write('Start\n')
#         user = User.objects.get(id=2)
#         
#         f.write(str(user) + '\n')
#         function_result = get_actionlist(user, user)
#         f.write(str(function_result) + '\n')
#         select_result = Action.objects.filter(user = user)
#         f.write(str(select_result) + '\n')
#         self.assertEqual(function_result, select_result)


        def test_test(self):
            users = User.objects.all()
            f = open('log.txt', 'w')
            f.write('Start\n')
            f.write(str(users))
            self.assertEqual(users, 0)