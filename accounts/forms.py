from django import forms
from django.contrib.auth import authenticate


class CollegeUserLoginForm(forms.Form):
    user_id = forms.CharField(label='User ID', max_length=50)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        user_id = cleaned_data.get('user_id')
        password = cleaned_data.get('password')

        if user_id and password:
            user = authenticate(user_id=user_id, password=password)
            if not user:
                raise forms.ValidationError("Invalid User ID or password.")
            elif not user.is_active:
                raise forms.ValidationError("This account is inactive.")

        return cleaned_data
