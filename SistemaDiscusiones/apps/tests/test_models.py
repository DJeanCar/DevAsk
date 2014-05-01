from django.test import TestCase

from apps.users.models import User
from apps.discuss.models import Question

class SimpleTest(TestCase):

	def test_save_slug(self):
		user = User.objects.create_user(username='JeanCarlos',email='jean@hotmail.com')
		question = Question.objects.create(user=user,
				title='pregunta numero 1',
				description='esta es la descripcion')
		self.assertEqual(question.slug , 'pregunta-numero-1')