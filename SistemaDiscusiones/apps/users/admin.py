from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm
from .models import User

class MyUserCreationForm(UserCreationForm):

	def clean_username(self):
		username = self.cleaned_data['username']
		try:
			User._default_manager.get(username=username)
		except User.DoesNotExist:
			return username

	class Meta(UserCreationForm.Meta):
		model = User


class UserAdmin(UserAdmin):
	
	add_form = MyUserCreationForm
	fieldsets = (
		('User', {'fields' : ('username', 'password')}),
		('Persona Info' , {'fields' : ('first_name',
										'last_name',
										'email',
										'avatar')}),
		('Permissions' , {'fields' : ('is_active',
										'is_staff',
										'is_superuser',
										'groups',
										'user_permissions')}),

		)


admin.site.register(User, UserAdmin)

