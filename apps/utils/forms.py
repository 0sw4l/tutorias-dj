from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils.translation import ugettext, ugettext_lazy as _


class BaseUserCreationForm(UserCreationForm):
    title = None
    email = forms.EmailField(label=_('email address'))

    class Meta:
        model = User
        exclude = (
            'last_login',
            'date_joined',
            'groups',
            'user_permissions',
            'password',
            'is_active',
            'is_staff',
            'is_superuser',
        )
        fields = '__all__'


class FormAllFields(forms.ModelForm):

    form_title = 'None'

    class Meta:
        model = None
        fields = '__all__'

