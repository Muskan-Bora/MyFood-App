from typing import Any, Mapping
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList
from .models import Profile, CusOrders, CusRatingFeedback

class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']

# profile form One
# --------------------------------------------------------
        
class ProfFormEditing(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['user', 'image', 'location', 'user_type']

# profile form Two
# --------------------------------------------------------
        
class ProfFormCreating(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['user', 'image', 'location', 'user_type']

# Customers Orders UPDATE
# -------------------------------------------------------

class CusOrdersUpd(forms.ModelForm):
    class Meta:
        model = CusOrders
        fields = ['quantity']

# Customer Rating Feedback
# -------------------------------------------------------
        
class CusRatFeedForm(forms.ModelForm):
    class Meta:
        model = CusRatingFeedback
        fields = ['ratings', 'feedback']

    def __init__(self, *args, **kwargs):
        super(CusRatFeedForm, self).__init__(*args, **kwargs)
        self.fields['ratings'].widget.attrs['placeholder'] = 'ratings'
        self.fields['feedback'].widhet.attrs['placeholder'] = 'feedback'
        