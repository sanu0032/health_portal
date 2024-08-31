from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile,BlogPost, Category


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    profile_picture = forms.ImageField(required=False)
    address_line1 = forms.CharField(max_length=255)
    city = forms.CharField(max_length=100)
    state = forms.CharField(max_length=100)
    pincode = forms.CharField(max_length=10)
    user_type = forms.ChoiceField(choices=Profile.USER_TYPES)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'first_name', 'last_name', 'profile_picture', 'address_line1', 'city', 'state', 'pincode', 'user_type']


class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'image', 'category', 'summary', 'content', 'draft']

        widgets = {
            'summary': forms.Textarea(attrs={'rows': 2}),
            'content': forms.Textarea(attrs={'rows': 5}),
        }