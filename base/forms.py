from django import forms
# from .models import User

# class RegistrationForm(forms.ModelForm):
#     password = forms.CharField(widget=forms.PasswordInput)

#     class Meta:
#         model = User
#         fields = ['first_name', 'last_name', 'email', 'password']

#     def clean_username(self):
#         username = self.cleaned_data.get('first_name') + self.cleaned_data.get('last_name')
#         return username.lower()
